<template>
  <div class="dashboard-page bg-white min-h-screen text-black">
    <NavigationBar />
    <div class="max-w-7xl mx-auto px-4 sm:px-6 py-8">
      <!-- Header -->
      <header class="flex justify-between items-center mb-6">
        <div>
          <h1 class="text-xl sm:text-2xl font-bold">Halo, {{ user.nama_lengkap || 'Pengguna' }}</h1>
          <p class="text-sm text-gray-600">Email: {{ user.email || '-' }}</p>
        </div>
      </header>
      <section class="bg-blue-50 border border-blue-200 text-sm sm:text-base p-6 rounded-lg shadow-sm mb-8">
        <h2 class="text-blue-600 font-semibold text-base sm:text-lg mb-3">Tips Menggunakan Aplikasi</h2>
        <ul class="list-disc list-inside text-gray-700 space-y-2">
          <li>
            <strong>Urutkan Kriteria:</strong> Gunakan fitur drag-and-drop untuk mengatur prioritas kriteria berdasarkan
            preferensimu.
          </li>
          <li>
            <strong>Klik "Dapatkan Rekomendasi":</strong> Sistem akan menghitung dan memberikan urutan perusahaan
            terbaik sesuai kriteria kamu.
          </li>
          <li>
            <strong>Interpretasi Hasil:</strong> Perusahaan dengan skor tertinggi (angka utilitas terbesar) dianggap
            paling ideal berdasarkan urutan kriteria kamu.
          </li>
          <li>
            <strong>Ingin Detail?</strong> Klik nama perusahaan pada hasil rekomendasi untuk melihat profil lengkapnya.
          </li>
        </ul>
      </section>

      <main class="grid grid-cols-1 lg:grid-cols-2 gap-6">

        <!-- Kriteria -->
        <section class="bg-white border border-gray-200 p-6 rounded-lg shadow-sm">
          <h2 class="text-lg sm:text-xl font-semibold mb-2 text-blue-600">Pilih Prioritas Kriteria</h2>
          <p class="text-sm text-gray-500 mb-4">Seret dan urutkan sesuai prioritasmu.</p>

          <ul v-if="kriteriaList.length > 0">
            <li v-for="(kriteria, index) in kriteriaList" :key="kriteria.id_kriteria" :draggable="true"
              @dragstart="dragStart(index)" @dragover.prevent="dragOver" @dragleave="dragLeave" @drop="drop(index)"
              class="mb-3 p-4 rounded-md border transition cursor-move bg-gray-50" :class="getDragClass(index)">
              <strong class="block text-sm sm:text-base text-blue-800">
                {{ index + 1 }}. {{ kriteria.nama_kriteria }} ({{ kriteria.tipe_kriteria }})
              </strong>
              <p class="text-xs sm:text-sm text-gray-500 mt-1">{{ kriteria.deskripsi_singkat }}</p>
            </li>
          </ul>
          <p v-else class="text-gray-400">Memuat data kriteria...</p>

          <button @click="handlePerhitungan" :disabled="loading || kriteriaList.length === 0"
            class="w-full mt-5 py-2 rounded-md font-semibold transition bg-gradient-to-r from-blue-500 to-cyan-500 text-white hover:from-blue-600 hover:to-cyan-600 disabled:opacity-50">
            <span v-if="loading">Menghitung...</span>
            <span v-else>Dapatkan Rekomendasi</span>
          </button>
        </section>

        <!-- Hasil -->
        <section class="bg-white border border-gray-200 p-6 rounded-lg shadow-sm">
          <h2 class="text-lg sm:text-xl font-semibold mb-4 text-blue-600">Hasil Rekomendasi</h2>
          <table v-if="hasilPerhitungan.length > 0" class="w-full text-sm sm:text-base">
            <thead>
              <tr class="bg-gray-100 text-left text-gray-600">
                <th class="p-2">Peringkat</th>
                <th class="p-2">Perusahaan</th>
                <th class="p-2 text-right">Skor</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="h in hasilPerhitungan" :key="h.id_alternatif" class="border-b hover:bg-gray-50 transition">
                <td class="p-2 text-center font-bold text-blue-700">{{ h.peringkat }}</td>
                <td class="p-2">
                  <router-link :to="{ name: 'profilperusahaan', query: { highlight: h.id_alternatif } }"
                    class="text-blue-600 hover:underline">
                    {{ h.nama_perusahaan }}
                  </router-link>
                </td>

                <td class="p-2 text-right">{{ h.skor_utilitas.toFixed(5) }}</td>
              </tr>
            </tbody>
          </table>
          <p v-else class="text-gray-400">Belum ada hasil.</p>
        </section>
      </main>
    </div>
    <FooTer />
  </div>
</template>


<script>
import axios from 'axios'
import Swal from 'sweetalert2'
import NavigationBar from '@/components/NavigationBar.vue'
import FooTer from '@/components/FooterBar.vue'
const API_BASE_URL = 'http://rather-blogger.gl.at.ply.gg:28663'

export default {
  name: 'SPKView',
  components: {
    NavigationBar,
    FooTer,
  },
  data() {
    return {
      user: {},
      kriteriaList: [],
      hasilPerhitungan: [],
      loading: false,
      error: '',
      draggedIndex: null,
      dragOverIndex: null,
    }
  },
  async created() {
    const token = localStorage.getItem('accessToken')
    if (!token) {
      this.$router.push('/login')
      return
    }
    this.api = axios.create({
      baseURL: API_BASE_URL,
      headers: { Authorization: `Bearer ${token}` },
    })
    this.fetchUserProfile()
    this.fetchKriteria()
  },
  methods: {
    // --- Data Fetching Methods ---
    async fetchUserProfile() {
      try {
        const response = await this.api.get('/users/me')
        this.user = response.data
      } catch (err) {
        this.handleApiError(err, 'Gagal mengambil data profil.')
      }
    },
    async fetchKriteria() {
      try {
        const response = await this.api.get('/kriteria/')
        this.kriteriaList = response.data
      } catch (err) {
        this.handleApiError(err, 'Gagal mengambil daftar kriteria.')
      }
    },

    // --- Drag & Drop Methods ---
    dragStart(index) {
      this.draggedIndex = index
    },
    dragOver(event) {
      // Find the element being hovered over
      const targetElement = event.target.closest('li')
      if (targetElement) {
        const allItems = Array.from(targetElement.parentElement.children)
        this.dragOverIndex = allItems.indexOf(targetElement)
      }
    },
    dragLeave() {
      this.dragOverIndex = null
    },
    drop(targetIndex) {
      if (this.draggedIndex === null || this.draggedIndex === targetIndex) {
        this.draggedIndex = null
        this.dragOverIndex = null
        return
      }
      // Reorder the array
      const draggedItem = this.kriteriaList.splice(this.draggedIndex, 1)[0]
      this.kriteriaList.splice(targetIndex, 0, draggedItem)
      // Reset state
      this.draggedIndex = null
      this.dragOverIndex = null
    },
    getDragClass(index) {
      if (this.draggedIndex === index) {
        return 'bg-white opacity-50 scale-105 shadow-2xl text-blue-500'
      }
      if (this.dragOverIndex === index) {
        return 'bg-white'
      }
      return 'bg-white'
    },

    // --- Calculation Method ---
    async handlePerhitungan() {
      this.loading = true
      this.error = ''
      this.hasilPerhitungan = []

      const peringkat_kriteria_kode = this.kriteriaList.map((k) => k.kode_kriteria)
      const payload = { peringkat: peringkat_kriteria_kode }

      try {
        const response = await this.api.post('/perhitungan/', payload)
        this.hasilPerhitungan = response.data.hasil
      } catch (err) {
        this.handleApiError(err, 'Gagal melakukan perhitungan.')
      } finally {
        this.loading = false
      }
    },

    // --- Utility Methods ---
    handleLogout() {
      localStorage.removeItem('accessToken')
      localStorage.removeItem('tokenType')
      this.$router.push('/login')
    },
    handleApiError(err, defaultMessage) {
      if (err.response && err.response.status === 401) {
        this.error = 'Sesi Anda telah berakhir. Silakan login kembali.'

        Swal.fire({
          icon: 'warning',
          title: 'Session Berakhir',
          text: 'Sesi login Anda telah habis. Silakan login kembali.',
          confirmButtonText: 'OK',
          confirmButtonColor: '#3085d6',
        }).then(() => {
          this.handleLogout()
        })
      } else if (err.response && err.response.data && err.response.data.detail) {
        this.error = err.response.data.detail
        Swal.fire({
          icon: 'error',
          title: 'Terjadi Kesalahan',
          text: this.error,
        })
      } else {
        this.error = defaultMessage
        Swal.fire({
          icon: 'error',
          title: 'Terjadi Kesalahan',
          text: defaultMessage,
        })
      }

      console.error(err)
    }

  },
}
</script>
<style scoped>
li {
  transition:
    background-color 0.3s ease,
    transform 0.3s ease,
    opacity 0.3s ease;
}
</style>
