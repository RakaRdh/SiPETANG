<template>
  <div>
    <NavigationBar />

    <!-- Hero Section -->
    <section class="bg-gradient-to-r from-blue-600 to-cyan-500 py-16 text-white text-center">
      <div class="max-w-3xl mx-auto px-4">
        <h1 class="text-3xl sm:text-4xl font-bold mb-4">Tentang Kami</h1>
        <p class="text-sm sm:text-base"></p>
      </div>
    </section>

    <!-- Tentang Sistem -->
    <section class="bg-white py-12 px-4 sm:px-6">
      <div class="max-w-5xl mx-auto text-center">
        <h2 class="text-xl sm:text-2xl font-bold text-blue-600 mb-4">Apa itu SiPETANG?</h2>
        <p class="text-gray-700 text-sm sm:text-base leading-relaxed text-justify">
          SiPETANG yang merupakan singkatan dari Sistem Pemilihan Tempat Magang adalah sistem yang dirancang untuk membantu mahasiswa dalam memilih tempat magang yang paling sesuai dengan preferensi dan kebutuhan mereka. Dengan memanfaatkan metode Additive Ratio Assessment (ARAS), sistem ini mengevaluasi berbagai alternatif lowongan berdasarkan kriteria penting seperti lokasi, benefit, reputasi perusahaan, dan lainnya.
        </p>
      </div>
    </section>

    <!-- Fitur Unggulan -->
    <section class="bg-gray-50 py-14 px-4 sm:px-6">
      <div class="max-w-6xl mx-auto">
        <h2 class="text-xl sm:text-2xl font-bold text-blue-600 text-center mb-8">Fitur Unggulan</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          <div class="p-6 bg-white border rounded-lg shadow hover:shadow-md transition">
            <div class="flex justify-center mb-4">
              <svg class="w-10 h-10 text-blue-500" fill="none" stroke="currentColor" stroke-width="2"
                viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M9.75 6.75h4.5M12 3v10.5m-7.5 0a9 9 0 1118 0 9 9 0 01-18 0z" />
              </svg>
            </div>
            <h3 class="font-semibold text-base text-blue-600 text-center mb-2">Perhitungan Rekomendasi Otomatis</h3>
            <p class="text-sm text-gray-700 text-center">Sistem memberikan rekomendasi tempat magang terbaik berdasarkan urutan kriteria yang Anda pilih.</p>
          </div>

          <div class="p-6 bg-white border rounded-lg shadow hover:shadow-md transition">
            <div class="flex justify-center mb-4">
              <svg class="w-10 h-10 text-blue-500" fill="none" stroke="currentColor" stroke-width="2"
                viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M9 17v1a3 3 0 006 0v-1m2 0a2 2 0 002-2v-4a2 2 0 00-2-2h-1V7a5 5 0 00-10 0v2H5a2 2 0 00-2 2v4a2 2 0 002 2h2" />
              </svg>
            </div>
            <h3 class="font-semibold text-base text-blue-600 text-center mb-2">Akses Mudah & Aman</h3>
            <p class="text-sm text-gray-700 text-center">Login aman, data pengguna terlindungi, dan akses sistem dari mana saja.</p>
          </div>

          <div class="p-6 bg-white border rounded-lg shadow hover:shadow-md transition">
            <div class="flex justify-center mb-4">
              <svg class="w-10 h-10 text-blue-500" fill="none" stroke="currentColor" stroke-width="2"
                viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round"
                  d="M3 10h2l1 2 1-2h2m6 0h2l1 2 1-2h2m-6 4h2l1 2 1-2h2M4 14h16" />
              </svg>
            </div>
            <h3 class="font-semibold text-base text-blue-600 text-center mb-2">Mitra Perusahaan Terverifikasi</h3>
            <p class="text-sm text-gray-700 text-center">Setiap lowongan berasal dari mitra terpercaya dengan profil yang jelas dan terverifikasi.</p>
          </div>
        </div>
      </div>
    </section>

    <!-- Optional: Tim Pengembang -->
    <section class="bg-white py-14 px-4 sm:px-6">
      <div class="max-w-5xl mx-auto text-center">
        <h2 class="text-xl sm:text-2xl font-bold text-blue-600 mb-4">Tim Pengembang</h2>
        <p class="text-sm sm:text-base text-gray-700 leading-relaxed mb-6">
          Sistem ini dikembangkan oleh tim mahasiswa Teknik Informatika yang peduli dengan kemudahan proses pemilihan tempat magang yang tepat dan berkualitas.
        </p>
        <div class="flex flex-wrap justify-center gap-6">
          <div class="w-40 text-center">
            <img src="https://ui-avatars.com/api/?name=I+M" class="w-20 h-20 mx-auto rounded-full mb-2" />
            <p class="text-sm font-medium text-gray-800">Ismail Muhammad</p>
          </div>
          <div class="w-40 text-center">
            <img src="https://ui-avatars.com/api/?name=R+K" class="w-20 h-20 mx-auto rounded-full mb-2" />
            <p class="text-sm font-medium text-gray-800">Raka Herdika Ramadhan</p>
          </div>
          <div class="w-40 text-center">
            <img src="https://ui-avatars.com/api/?name=C+R" class="w-20 h-20 mx-auto rounded-full mb-2" />
            <p class="text-sm font-medium text-gray-800">Cinta Ramadhanti Putri Dini</p>
          </div>
        </div>
      </div>
    </section>

    <FooterBar />
  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import FooterBar from '@/components/FooterBar.vue'

export default {
  name: 'TentangKamiView',
  components: {
    NavigationBar,
    FooterBar
  }
}
</script>
