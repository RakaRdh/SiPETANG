<template>
  <div
    class="min-h-screen bg-gradient-to-r from-blue-600 to-cyan-400 flex items-center justify-center px-4 sm:px-6 md:px-8">
    <div class="w-full max-w-md bg-white border shadow-xl rounded-2xl p-6 space-y-6 transition-all duration-300">
      <div class="text-center">
        <img src="@/assets/logo.png" alt="Logo"
          class="mx-auto mb-4 w-16 sm:w-20 h-16 sm:h-20 object-contain drop-shadow-md" />
        <h2 class="text-xl sm:text-2xl font-bold text-black">Selamat Datang Kembali</h2>
        <p class="mt-1 text-xs sm:text-sm text-gray-600">Masukkan kredensial untuk masuk ke akun Anda</p>
      </div>


      <form @submit.prevent="handleLogin" class="space-y-4">
        <div class="relative">
          <span class="absolute inset-y-0 left-0 pl-3 flex items-center text-cyan-600">
            <!-- Heroicons Mail -->
            <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25H4.5A2.25 2.25 0 012.25 17.25V6.75A2.25 2.25 0 014.5 4.5h15a2.25 2.25 0 012.25 2.25z" />
              <path stroke-linecap="round" stroke-linejoin="round" d="M2.25 6.75L12 13.5l9.75-6.75" />
            </svg>
          </span>
          <input v-model="username" type="text" placeholder="Masukkan email atau NIM" required
            class="pl-10 w-full py-2 px-3 bg-white text-black placeholder-gray-500 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-500" />
        </div>

        <div class="relative">
          <span class="absolute inset-y-0 left-0 pl-3 flex items-center text-cyan-600">
            <!-- Heroicons Lock -->
            <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M16.5 10.5v-2.25a4.5 4.5 0 00-9 0V10.5M3.75 10.5h16.5M5.25 10.5v7.5a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-7.5" />
            </svg>
          </span>
          <input v-model="password" :type="showPassword ? 'text' : 'password'" placeholder="Masukkan password" required
            class="pl-10 pr-10 w-full py-2 px-3 bg-white text-black placeholder-gray-500 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-500" />
          <span class="absolute inset-y-0 right-0 pr-3 flex items-center text-gray-600 cursor-pointer"
            @click="togglePasswordVisibility">
            <svg v-if="showPassword" xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M2.458 12C3.732 7.943 7.523 5.25 12 5.25c4.477 0 8.268 2.693 9.542 6.75-1.274 4.057-5.065 6.75-9.542 6.75-4.477 0-8.268-2.693-9.542-6.75z" />
            </svg>
            <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
              stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M13.875 18.825A10.05 10.05 0 0112 19.5c-4.477 0-8.268-2.693-9.542-6.75a10.032 10.032 0 013.143-4.568m3.292-1.868A9.959 9.959 0 0112 4.5c4.477 0 8.268 2.693 9.542 6.75a9.969 9.969 0 01-4.302 5.165M3 3l18 18" />
            </svg>
          </span>
        </div>

        <button type="submit"
          class="w-full py-2 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600 text-white rounded-lg font-semibold transition duration-200 shadow-md">
          Masuk
        </button>

        <p v-if="errorMessage" class="text-red-600 text-sm text-center">{{ errorMessage }}</p>
      </form>

      <p class="text-center text-sm text-gray-700">
        Belum punya akun?
        <router-link to="/register" class="font-bold text-blue-500 hover:underline">Daftar di sini</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2'
// PERUBAHAN: Impor jwt-decode untuk membaca isi token
import { jwtDecode } from 'jwt-decode'

// Gunakan alamat backend lokal Anda
const API_BASE_URL = 'http://rather-blogger.gl.at.ply.gg:28663'

export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '',
      showPassword: false,
    }
  },
  methods: {
    async handleLogin() {
      this.errorMessage = ''
      const formData = new URLSearchParams()
      formData.append('username', this.username)
      formData.append('password', this.password)

      try {
        const response = await axios.post(`${API_BASE_URL}/auth/login`, formData)

        const { access_token } = response.data
        // Simpan token ke localStorage
        localStorage.setItem('accessToken', access_token)

        // --- LOGIKA PENGALIHAN BERBASIS PERAN (ROLE) ---
        // 1. Dekode token untuk mendapatkan payload-nya
        const decodedToken = jwtDecode(access_token)

        // 2. Simpan peran (type) ke localStorage untuk digunakan oleh Navigation Guard
        if (decodedToken.type) {
          localStorage.setItem('userType', decodedToken.type)
        }

        // Tampilkan notifikasi sukses
        await Swal.fire({
          icon: 'success',
          title: 'Login Berhasil!',
          timer: 1500,
          showConfirmButton: false,
        })

        // 3. Arahkan berdasarkan peran
        if (decodedToken.type === 'admin') {
          this.$router.push('/admin/dashboard') // Arahkan ke dasbor admin
        } else {
          this.$router.push('/landingpage') // Arahkan ke dasbor SPK untuk user biasa
        }
      } catch (error) {
        Swal.fire({
          icon: 'error',
          title: 'Gagal Login',
          text: error.response?.data?.detail ?? 'Terjadi kesalahan pada server.',
        })
      }
    },
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword
    },
  },
}
</script>
