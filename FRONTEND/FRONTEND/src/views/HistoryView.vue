<template>
  <div class="bg-white min-h-screen text-black">
    <NavigationBar />

    <div class="max-w-7xl mx-auto px-6 py-8">
      <!-- Judul -->
      <header class="mb-8">
        <h1 class="text-2xl font-bold text-blue-600">Riwayat Perhitungan Anda</h1>
        <p class="text-sm text-gray-500 mt-1">
          Berikut adalah catatan rekomendasi tempat magang sebelumnya.
        </p>
      </header>

      <!-- Loading -->
      <div v-if="loading" class="text-center text-gray-400 py-10">
        <span class="animate-pulse">Memuat riwayat...</span>
      </div>

      <!-- Error -->
      <div v-else-if="error" class="text-red-600 bg-red-100 border border-red-300 p-4 rounded shadow-sm">
        {{ error }}
      </div>

      <!-- Riwayat Tersedia -->
      <div v-else-if="historyList.length > 0" class="space-y-6">
        <div v-for="item in historyList" :key="item.id_riwayat"
          class="relative border-l-4 border-blue-500 bg-gray-50 hover:bg-gray-100 transition p-6 rounded-lg shadow-sm">
          <!-- Tanggal -->
          <div class="flex items-center text-sm text-gray-500 mb-4">
            <svg class="w-4 h-4 mr-2 text-blue-500" fill="none" stroke="currentColor" stroke-width="2"
              viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M8 7V3m8 4V3m-9 8h10m-11 8h12a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            Dihitung pada: {{ new Date(item.tanggal_perhitungan).toLocaleString('id-ID') }}
          </div>

          <!-- Konten -->
          <div class="grid md:grid-cols-2 gap-6 text-sm">
            <!-- Prioritas -->
            <div>
              <h3 class="font-semibold text-blue-600 mb-2">Prioritas Saat Itu:</h3>
              <ol class="list-decimal ml-5 space-y-1 text-gray-700">
                <li v-for="kode in item.bobot_kriteria.peringkat_user" :key="kode">
                  {{ getKriteriaNameByCode(kode) }}
                </li>
              </ol>
            </div>

            <!-- Hasil -->
            <div>
              <h3 class="font-semibold text-blue-600 mb-2">Hasil Rekomendasi:</h3>
              <ul class="space-y-1">
                <li v-for="hasil in item.hasil_rekomendasi.slice(0, 5)" :key="hasil.id_alternatif"
                  class="flex items-center gap-3">
                  <!-- PERBAIKAN: Menghapus span duplikat. Nama perusahaan sekarang hanya dari router-link. -->
                  <router-link :to="{ name: 'profilperusahaan', query: { highlight: hasil.id_alternatif } }"
                    class="text-black hover:text-blue-600 hover:underline">
                    {{ hasil.nama_perusahaan }}
                  </router-link>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Tidak Ada Riwayat -->
      <div v-else class="text-center text-gray-400 py-10">
        <svg class="w-12 h-12 mx-auto text-gray-300 mb-3" fill="none" stroke="currentColor" stroke-width="1.5"
          viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6l4 2m6 0a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        Belum ada riwayat perhitungan.
      </div>
    </div>

    <FooTer />
  </div>
</template>

<script>
import axios from 'axios'
import NavigationBar from '@/components/NavigationBar.vue'
import FooTer from '@/components/FooterBar.vue'

// Ganti dengan URL API Anda yang sebenarnya jika berbeda
const API_BASE_URL = 'http://rather-blogger.gl.at.ply.gg:28663'

export default {
  name: 'HistoryView',
  components: {
    NavigationBar,
    FooTer,
  },
  data() {
    return {
      historyList: [],
      allKriteria: [],
      loading: true,
      error: '',
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

    // Memuat data secara paralel untuk efisiensi
    await Promise.all([this.fetchAllKriteria(), this.fetchHistory()])
  },
  methods: {
    async fetchAllKriteria() {
      try {
        const response = await this.api.get('/kriteria/')
        this.allKriteria = response.data
      } catch (err) {
        this.handleApiError(err, 'Gagal memuat data master kriteria.')
      }
    },
    async fetchHistory() {
      this.loading = true
      this.error = ''
      try {
        const response = await this.api.get('/riwayat/')
        this.historyList = response.data
      } catch (err) {
        this.handleApiError(err, 'Gagal mengambil data riwayat.')
      } finally {
        this.loading = false
      }
    },
    getKriteriaNameByCode(kode) {
      const kriteria = this.allKriteria.find((k) => k.kode_kriteria === kode)
      return kriteria ? kriteria.nama_kriteria : kode
    },
    handleApiError(err, defaultMessage) {
      if (err.response && err.response.status === 401) {
        this.error = 'Sesi Anda telah berakhir. Silakan login kembali.'
        localStorage.removeItem('accessToken')
        localStorage.removeItem('userType')
        this.$router.push('/login')
      } else if (err.response?.data?.detail) {
        this.error = err.response.data.detail
      } else {
        this.error = defaultMessage
      }
      console.error(err)
    },
  },
}
</script>
