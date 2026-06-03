<template>
  <nav class="bg-white shadow-md sticky top-0 z-[999] font-[Poppins]">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-20 items-center">
        <!-- Logo -->
        <div class="flex-shrink-0">
          <img src="@/assets/logo.png" alt="Logo" class="h-14 w-auto" />
        </div>

        <!-- Desktop Menu -->
        <div class="hidden md:flex space-x-6 text-sm font-medium items-center">
          <router-link to="/landingpage" class="text-gray-700 hover:text-blue-500">Beranda</router-link>
          <router-link to="/spk" class="text-gray-700 hover:text-blue-500">SPK</router-link>
          <router-link to="/history" class="block text-gray-700 hover:text-blue-500">Riwayat</router-link>
          <router-link to="/profil-perusahaan" class="text-gray-700 hover:text-blue-500">Perusahaan</router-link>
          <router-link to="/profil-pengguna" class="text-gray-700 hover:text-blue-500">Profil </router-link>
          <button
            @click='confirmLogout'
            class="bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600 text-white px-4 py-1 rounded transition"
          >
            Keluar
          </button>
        </div>

        <!-- Mobile Menu Button -->
        <div class="md:hidden">
          <button @click="mobileOpen = !mobileOpen">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-700" fill="none"
              viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
      </div>
    </div>

    <!-- Mobile Dropdown Menu -->
    <div v-if="mobileOpen" class="md:hidden bg-white px-6 py-4 space-y-3 shadow">
      <router-link @click="closeMenu" to="/landingpage" class="block text-gray-700 hover:text-blue-500">Beranda</router-link>
      <router-link @click="closeMenu" to="/SPK" class="block text-gray-700 hover:text-blue-500">SPK</router-link>
      <router-link @click="closeMenu" to="/history" class="block text-gray-700 hover:text-blue-500">Riwayat</router-link>
      <router-link @click="closeMenu" to="/profile-perusahaan" class="block text-gray-700 hover:text-blue-500">Perusahaan</router-link>
      <router-link @click="closeMenu" to="/profile-pengguna" class="block text-gray-700 hover:text-blue-500">Profil</router-link>
      <button
        @click="confirmLogout"
        class="w-full text-white bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600 px-4 py-2 rounded"
      >
        Keluar
      </button>
    </div>
  </nav>
</template>

<script>
import Swal from 'sweetalert2'

export default {
  name: 'NavigationBar',
  data() {
    return {
      mobileOpen: false,
    }
  },
  methods: {
    async confirmLogout() {
      const result = await Swal.fire({
        title: 'Konfirmasi Logout',
        text: 'Apakah Anda yakin ingin logout?',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Ya, logout',
        cancelButtonText: 'Batal',
        confirmButtonColor: '#3b82f6',
        cancelButtonColor: '#d33'
      })

      if (result.isConfirmed) {
        localStorage.removeItem('accessToken')
        localStorage.removeItem('tokenType')
        this.$router.push('/login')
        Swal.fire('Berhasil Logout', 'Anda telah keluar dari akun.', 'success')
      }
    },
    closeMenu() {
      this.mobileOpen = false
    }
  }
}
</script>
