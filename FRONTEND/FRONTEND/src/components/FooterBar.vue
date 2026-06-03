<template>
  <footer class="bg-white text-sm font-[Poppins] border-t border-gray-300">
    <div class="max-w-7xl mx-auto px-4 py-10 grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-8">

      <!-- Kolom 1 -->
      <div>
        <img src="@/assets/logo.png" alt="Logo" class="h-16 mb-3" />
        <p class="text-gray-700 text-justify">
          Sistem Pendukung Keputusan untuk Pemilihan Tempat Magang Mahasiswa TIK berbasis metode ARAS.
        </p>
      </div>

      <!-- Kolom 2 -->
      <div>
        <h3 class="font-semibold text-blue-500 mb-2">SiPETANG</h3>
        <router-link to="/tentang-kami" class="text-gray-700 hover:text-blue-500">Tentang Kami</router-link><br>
        <router-link to="/kontak-kami" class="text-gray-700 hover:text-blue-500">Kontak Kami</router-link>
      </div>

      <!-- Kolom 3 -->
      <div>
        <h3 class="font-semibold text-blue-500 mb-2">Alamat</h3>
        <p class="text-gray-700">Jl. Teknologi No. 10</p>
        <p class="text-gray-700">Bandung, Indonesia</p>
      </div>

      <!-- Kolom 4 -->
      <div>
        <h3 class="font-semibold text-blue-500 mb-2">Ikuti Kami</h3>
        <div class="flex space-x-3 mt-4 justify-start sm:justify-start">
          <a
            href="tel:+622150919981"
            aria-label="Telepon"
            class="w-9 h-9 rounded-full bg-blue-500 flex items-center justify-center hover:bg-blue-600 transition"
          >
            <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
              <path
                d="M6.62 10.79a15.054 15.054 0 006.59 6.59l2.2-2.2a1.003 1.003 0 011.01-.24c1.12.37 2.33.57 3.58.57a1 1 0 011 1v3.5a1 1 0 01-1 1C10.52 22 2 13.48 2 3.5a1 1 0 011-1H6.5a1 1 0 011 1c0 1.25.2 2.46.57 3.58a1 1 0 01-.24 1.01l-2.2 2.2z"
              />
            </svg>
          </a>
          <a
            href="#"
            aria-label="Facebook"
            class="w-9 h-9 rounded-full bg-blue-500 flex items-center justify-center hover:bg-blue-600 transition"
          >
            <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
              <path
                d="M22.675 0H1.325C.593 0 0 .593 0 1.325v21.351C0 23.407.593 24 1.325 24h11.495v-9.294H9.691v-3.622h3.129V8.413c0-3.1 1.893-4.788 4.658-4.788 1.325 0 2.466.099 2.798.143v3.24l-1.92.001c-1.504 0-1.795.715-1.795 1.763v2.313h3.587l-.467 3.622h-3.12V24h6.116C23.407 24 24 23.407 24 22.676V1.325C24 .593 23.407 0 22.675 0z"
              />
            </svg>
          </a>
          <a
            href="#"
            aria-label="Twitter"
            class="w-9 h-9 rounded-full bg-blue-500 flex items-center justify-center hover:bg-blue-600 transition"
          >
            <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
              <path
                d="M24 4.557a9.83 9.83 0 0 1-2.828.775 4.932 4.932 0 0 0 2.165-2.724c-.951.564-2.005.974-3.127 1.195a4.916 4.916 0 0 0-8.384 4.482C7.691 8.094 4.066 6.13 1.64 3.161a4.822 4.822 0 0 0-.666 2.475 4.917 4.917 0 0 0 2.188 4.1 4.903 4.903 0 0 1-2.228-.616v.06a4.919 4.919 0 0 0 3.946 4.827 4.996 4.996 0 0 1-2.224.085 4.92 4.92 0 0 0 4.6 3.417A9.867 9.867 0 0 1 0 19.54a13.94 13.94 0 0 0 7.548 2.212c9.142 0 14.307-7.721 13.995-14.646A9.935 9.935 0 0 0 24 4.557z"
              />
            </svg>
          </a>
          <a
            href="#"
            aria-label="Instagram"
            class="w-9 h-9 rounded-full bg-blue-500 flex items-center justify-center hover:bg-blue-600 transition"
          >
            <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
              <path
                d="M12 2.163c3.204 0 3.584.012 4.85.07 1.366.062 2.633.34 3.608 1.316.975.975 1.254 2.242 1.316 3.608.058 1.266.07 1.646.07 4.85s-.012 3.584-.07 4.85c-.062 1.366-.341 2.633-1.316 3.608-.975.975-2.242 1.254-3.608 1.316-1.266.058-1.646.07-4.85.07s-3.584-.012-4.85-.07c-1.366-.062-2.633-.341-3.608-1.316-.975-.975-1.254-2.242-1.316-3.608C2.175 15.747 2.163 15.367 2.163 12s.012-3.584.07-4.85c.062-1.366.341-2.633 1.316-3.608C4.524 2.504 5.791 2.225 7.157 2.163 8.423 2.105 8.803 2.093 12 2.093zm0-2.163C8.741 0 8.332.012 7.052.07 5.772.128 4.634.427 3.678 1.383 2.722 2.339 2.423 3.477 2.365 4.757.012 8.332 0 8.741 0 12c0 3.259.012 3.668.07 4.948.058 1.28.357 2.418 1.313 3.374.956.956 2.094 1.255 3.374 1.313C8.332 23.988 8.741 24 12 24s3.668-.012 4.948-.07c1.28-.058 2.418-.357 3.374-1.313.956-.956 1.255-2.094 1.313-3.374.058-1.28.07-1.689.07-4.948s-.012-3.668-.07-4.948c-.058-1.28-.357-2.418-1.313-3.374C19.366.427 18.228.128 16.948.07 15.668.012 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zm0 10.162a3.999 3.999 0 1 1 0-7.998 3.999 3.999 0 0 1 0 7.998zm6.406-11.845a1.44 1.44 0 1 0 0 2.88 1.44 1.44 0 0 0 0-2.88z"
              />
            </svg>
          </a>
        </div>
      </div>

    </div>
    <div class="text-center py-4 bg-gradient-to-r from-blue-600 to-cyan-400 text-white text-sm">
      &copy; 2025 SPK-Magang. Semua hak dilindungi.
    </div>
  </footer>
</template>

<script>
export default {
  name: 'FooterBar'
}
</script>
