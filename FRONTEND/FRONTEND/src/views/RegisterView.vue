<template>
  <div
    class="min-h-screen bg-gradient-to-r from-cyan-500 to-blue-500 flex items-center justify-center px-4 sm:px-6"
  >
    <div class="w-full max-w-md space-y-6">
      <div class="text-center">
        <img
          src="@/assets/logo.png"
          alt="Logo"
          class="mx-auto mb-4 w-16 sm:w-20 h-16 sm:h-20 object-contain"
        />
        <h2 class="text-xl sm:text-2xl font-bold text-white">Buat Akun Baru</h2>
        <p class="mt-1 text-xs sm:text-sm text-white/80">
          Silakan isi data berikut untuk mendaftar
        </p>
      </div>

      <form @submit.prevent="handleRegister" class="space-y-4">
        <!-- Nama Lengkap -->
        <div class="relative">
          <span class="absolute inset-y-0 left-0 pl-3 flex items-center text-cyan-600">
            <!-- Heroicons User -->
            <svg
              class="w-5 h-5"
              fill="none"
              stroke="currentColor"
              stroke-width="1.5"
              viewBox="0 0 24 24"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z"
              />
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M4.5 20.25a8.25 8.25 0 0115 0"
              />
            </svg>
          </span>
          <input
            v-model="nama_lengkap"
            type="text"
            placeholder="Nama Lengkap"
            required
            class="pl-10 w-full py-2 px-3 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-cyan-500"
          />
        </div>

        <!-- Email -->
        <div class="relative">
          <span class="absolute inset-y-0 left-0 pl-3 flex items-center text-cyan-600">
            <!-- Heroicons Mail -->
            <svg
              class="w-5 h-5"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M21.75 6.75v10.5a2.25 2.25 0 01-2.25 2.25H4.5A2.25 2.25 0 012.25 17.25V6.75A2.25 2.25 0 014.5 4.5h15a2.25 2.25 0 012.25 2.25z"
              />
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M2.25 6.75L12 13.5l9.75-6.75"
              />
            </svg>
          </span>
          <input
            v-model="email"
            type="email"
            placeholder="Email"
            required
            class="pl-10 w-full py-2 px-3 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-cyan-500"
          />
        </div>

        <!-- Password -->
        <div class="relative">
          <span class="absolute inset-y-0 left-0 pl-3 flex items-center text-cyan-600">
            <!-- Lock Icon -->
            <svg
              class="w-5 h-5"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M16.5 10.5v-2.25a4.5 4.5 0 00-9 0V10.5M3.75 10.5h16.5M5.25 10.5v7.5a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-7.5"
              />
            </svg>
          </span>
          <input
            v-model="password"
            :type="showPassword ? 'text' : 'password'"
            placeholder="Password"
            required
            class="pl-10 pr-10 w-full py-2 px-3 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-100"
          />
          <span
            class="absolute inset-y-0 right-0 pr-3 flex items-center cursor-pointer text-gray-500"
            @click="togglePasswordVisibility"
          >
            <svg
              v-if="showPassword"
              xmlns="http://www.w3.org/2000/svg"
              class="w-5 h-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
              />
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M2.458 12C3.732 7.943 7.523 5.25 12 5.25c4.477 0 8.268 2.693 9.542 6.75-1.274 4.057-5.065 6.75-9.542 6.75-4.477 0-8.268-2.693-9.542-6.75z"
              />
            </svg>
            <svg
              v-else
              xmlns="http://www.w3.org/2000/svg"
              class="w-5 h-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M13.875 18.825A10.05 10.05 0 0112 19.5c-4.477 0-8.268-2.693-9.542-6.75a10.032 10.032 0 013.143-4.568m3.292-1.868A9.959 9.959 0 0112 4.5c4.477 0 8.268 2.693 9.542 6.75a9.969 9.969 0 01-4.302 5.165M3 3l18 18"
              />
            </svg>
          </span>
        </div>

        <!-- Konfirmasi Password -->
        <div class="relative">
          <span class="absolute inset-y-0 left-0 pl-3 flex items-center text-cyan-600">
            <!-- Lock Icon -->
            <svg
              class="w-5 h-5"
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M16.5 10.5v-2.25a4.5 4.5 0 00-9 0V10.5M3.75 10.5h16.5M5.25 10.5v7.5a2.25 2.25 0 002.25 2.25h9a2.25 2.25 0 002.25-2.25v-7.5"
              />
            </svg>
          </span>
          <input
            v-model="confirmPassword"
            :type="showConfirmPassword ? 'text' : 'password'"
            placeholder="Konfirmasi Password"
            required
            class="pl-10 pr-10 w-full py-2 px-3 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-blue-100"
          />
          <span
            class="absolute inset-y-0 right-0 pr-3 flex items-center cursor-pointer text-gray-500"
            @click="toggleConfirmPasswordVisibility"
          >
            <svg
              v-if="showConfirmPassword"
              xmlns="http://www.w3.org/2000/svg"
              class="w-5 h-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"
              />
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M2.458 12C3.732 7.943 7.523 5.25 12 5.25c4.477 0 8.268 2.693 9.542 6.75-1.274 4.057-5.065 6.75-9.542 6.75-4.477 0-8.268-2.693-9.542-6.75z"
              />
            </svg>
            <svg
              v-else
              xmlns="http://www.w3.org/2000/svg"
              class="w-5 h-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M13.875 18.825A10.05 10.05 0 0112 19.5c-4.477 0-8.268-2.693-9.542-6.75a10.032 10.032 0 013.143-4.568m3.292-1.868A9.959 9.959 0 0112 4.5c4.477 0 8.268 2.693 9.542 6.75a9.969 9.969 0 01-4.302 5.165M3 3l18 18"
              />
            </svg>
          </span>
        </div>

        <button
          type="submit"
          class="w-full py-2 bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600 text-white rounded-md font-semibold transition-colors"
        >
          Daftar
        </button>

        <p v-if="errorMessage" class="text-red-600 text-sm text-center">{{ errorMessage }}</p>
        <p v-if="successMessage" class="text-green-600 text-sm text-center">{{ successMessage }}</p>
      </form>

      <p class="text-center text-sm text-gray-700">
        Sudah punya akun?
        <router-link to="/login" class="font-bold text-blue-500 hover:underline"
          >Masuk di sini</router-link
        >
      </p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2'
const API_BASE_URL = 'http://rather-blogger.gl.at.ply.gg:28663'

export default {
  name: 'RegisterPage',
  data() {
    return {
      nama_lengkap: '',
      email: '',
      password: '',
      confirmPassword: '',
      showPassword: false,
      showConfirmPassword: false,
      errorMessage: '',
      successMessage: '',
    }
  },
  methods: {
    togglePasswordVisibility() {
      this.showPassword = !this.showPassword
    },
    toggleConfirmPasswordVisibility() {
      this.showConfirmPassword = !this.showConfirmPassword
    },
    async handleRegister() {
      this.errorMessage = ''
      this.successMessage = ''

      if (this.password !== this.confirmPassword) {
        return Swal.fire({
          icon: 'warning',
          title: 'Password Tidak Cocok',
          text: 'Silakan pastikan password dan konfirmasi password sama.',
          confirmButtonColor: '#2b7fff',
        })
      }

      const payload = {
        nama_lengkap: this.nama_lengkap,
        email: this.email,
        password: this.password,
      }

      try {
        await axios.post(`${API_BASE_URL}/auth/register`, payload)
        await Swal.fire({
          icon: 'success',
          title: 'Registrasi Berhasil!',
          text: 'Mengalihkan ke halaman login...',
          timer: 2000,
          showConfirmButton: false,
        })
        this.$router.push('/login')
      } catch (error) {
        Swal.fire({
          icon: 'error',
          title: 'Gagal Registrasi',
          text: error.response?.data?.detail ?? 'Terjadi kesalahan saat registrasi.',
        })
      }
    },
  },
}
</script>
