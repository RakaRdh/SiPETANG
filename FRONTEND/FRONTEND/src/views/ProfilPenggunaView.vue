<template>
  <div class="bg-white min-h-screen text-black">
    <NavigationBar />

    <div class="max-w-3xl mx-auto px-6 py-12">
      <h1 class="text-2xl font-bold text-blue-500 mb-6 text-center">Profil Pengguna</h1>

      <!-- Loading & Error States -->
      <div v-if="loading" class="text-center text-gray-400 py-10">Memuat data profil...</div>
      <div
        v-else-if="error"
        class="bg-red-100 border border-red-300 text-red-700 p-4 rounded mb-4 text-center"
      >
        {{ error }}
      </div>

      <!-- Konten Profil -->
      <div v-else class="bg-gray-50 shadow rounded-lg p-6 space-y-6">
        <div class="flex items-center space-x-4">
          <div
            class="w-16 h-16 rounded-full bg-blue-100 flex items-center justify-center text-2xl font-bold text-blue-500"
          >
            {{ user.nama_lengkap.charAt(0).toUpperCase() }}
          </div>
          <div>
            <h2 class="text-xl font-semibold">{{ user.nama_lengkap }}</h2>
            <p class="text-sm text-gray-600">Email: {{ user.email }}</p>
          </div>
        </div>

        <hr />

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-sm">
          <div>
            <p class="text-gray-500">Status Akun</p>
            <p class="font-semibold text-green-600" v-if="user.is_active">Aktif</p>
            <p class="font-semibold text-red-500" v-else>Tidak Aktif</p>
          </div>
          <div>
            <p class="text-gray-500">Tanggal Terdaftar</p>
            <p class="font-semibold">{{ formatDate(user.created_at) }}</p>
          </div>
        </div>

        <!-- Tombol Aksi Baru -->
        <div class="border-t pt-6">
          <button
            @click="handleDeactivateAccount"
            class="w-full bg-red-500 hover:bg-red-600 text-white font-bold py-2 px-4 rounded-md transition-colors duration-200"
          >
            Hapus Akun Saya
          </button>
          <p class="text-xs text-gray-500 mt-2 text-center">
            Tindakan ini akan menonaktifkan akun Anda. Anda tidak dapat masuk lagi setelah ini.
          </p>
        </div>
      </div>
    </div>

    <FooterBar />
  </div>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2'
import { format, parseISO } from 'date-fns'
import { id } from 'date-fns/locale'
import NavigationBar from '@/components/NavigationBar.vue'
import FooterBar from '@/components/FooterBar.vue'

const API_BASE_URL = 'http://rather-blogger.gl.at.ply.gg:28663' // Sesuaikan dengan URL API Anda

export default {
  name: 'ProfilPenggunaView',
  components: {
    NavigationBar,
    FooterBar,
  },
  data() {
    return {
      user: {},
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
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })

    this.fetchUserProfile()
  },
  methods: {
    async fetchUserProfile() {
      try {
        const response = await this.api.get('/users/me')
        this.user = response.data
      } catch (err) {
        this.handleApiError(err, 'Gagal memuat data pengguna.')
      } finally {
        this.loading = false
      }
    },
    // PERBAIKAN: Fungsi format tanggal yang lebih andal
    formatDate(dateString) {
      if (!dateString) return 'N/A'
      try {
        const date = parseISO(dateString)
        if (isNaN(date.getTime())) {
          throw new Error('Invalid date value')
        }
        return format(date, 'dd MMMM yyyy', { locale: id })
      } catch (error) {
        console.error('Gagal memformat tanggal:', dateString, error)
        return 'Format Salah'
      }
    },
    // FUNGSI BARU: Untuk menangani penonaktifan akun
    async handleDeactivateAccount() {
      const result = await Swal.fire({
        title: 'Anda Yakin?',
        text: 'Anda akan menonaktifkan akun Anda secara permanen. Anda tidak bisa mengurungkan tindakan ini.',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Ya, hapus akun saya!',
        cancelButtonText: 'Batal',
      })

      if (result.isConfirmed) {
        try {
          await this.api.delete('/users/me/deactivate')

          await Swal.fire(
            'Berhasil!',
            'Akun Anda telah dinonaktifkan. Anda akan dialihkan ke halaman login.',
            'success',
          )

          // Logout pengguna setelah berhasil
          localStorage.removeItem('accessToken')
          localStorage.removeItem('userType')
          this.$router.push('/login')
        } catch (err) {
          this.handleApiError(err, 'Gagal menonaktifkan akun.')
        }
      }
    },
    handleApiError(err, defaultMessage) {
      const errorMessage = err.response?.data?.detail || defaultMessage
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: errorMessage,
      })
      if (err.response?.status === 401) {
        localStorage.removeItem('accessToken')
        localStorage.removeItem('userType')
        this.$router.push('/login')
      }
      console.error(err)
    },
  },
}
</script>
