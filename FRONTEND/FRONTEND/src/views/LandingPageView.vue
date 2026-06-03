<template>
  <div>
    <NavigationBar class="sticky top-0 z-50" />

    <!-- Hero Section -->
    <section class="relative w-full h-[60vh] sm:h-[70vh] overflow-hidden">
      <Swiper
        :modules="modules"
        :autoplay="{ delay: 4000 }"
        effect="fade"
        loop
        class="w-full h-full"
      >
        <SwiperSlide v-for="(image, index) in images" :key="index">
          <img :src="image" class="w-full h-full object-cover opacity-80" alt="Banner" />
        </SwiperSlide>
      </Swiper>

      <div class="absolute inset-0 flex flex-col items-center justify-center text-center px-4 z-10">
        <h1 class="text-xl sm:text-3xl md:text-4xl font-bold text-white mb-4 leading-tight">
          Sistem Pendukung Keputusan Pemilihan Tempat Magang
        </h1>
        <router-link
          to="/spk"
          class="bg-blue-500 hover:bg-blue-600 text-white font-semibold px-4 py-2 sm:px-6 sm:py-3 rounded-md transition duration-300 text-sm sm:text-base"
        >
          Mulai Pilih Tempat Magang
        </router-link>
      </div>
    </section>

    <!-- Mitra Section -->
    <section
      class="bg-white py-10 mt-[-40px] sm:mt-[-50px] rounded-t-[30px] sm:rounded-t-[50px] relative z-10"
    >
      <div class="max-w-6xl mx-auto text-center px-4">
        <h2 class="text-lg sm:text-xl md:text-2xl font-bold text-blue-500 mb-6">Mitra Kami</h2>
        <Swiper
          :modules="modules"
          :slides-per-view="2"
          :space-between="12"
          :autoplay="{ delay: 2000 }"
          loop
          class="px-2 sm:px-4"
          :breakpoints="{
            480: { slidesPerView: 2 },
            640: { slidesPerView: 3 },
            1024: { slidesPerView: 4 },
          }"
        >
          <SwiperSlide v-for="(logo, index) in partners" :key="index">
            <img :src="logo" alt="Mitra" class="h-5 sm:h-8 md:h-10 mx-auto object-contain" />
          </SwiperSlide>
        </Swiper>
      </div>
    </section>

    <!-- Tentang Website -->
    <section class="bg-white py-10 px-4 sm:px-6">
      <div class="max-w-6xl mx-auto flex flex-col md:flex-row items-center gap-20">
        <!-- Teks Penjelasan -->
        <div class="md:w-2/3 text-center md:text-left">
          <h2 class="text-base sm:text-xl font-bold text-blue-500 mb-4">Tentang Website Ini</h2>
          <p class="text-gray-700 text-sm sm:text-md leading-relaxed text-justify">
            Sistem ini bertujuan membantu mahasiswa dalam proses pengambilan keputusan untuk mencari
            tempat magang/internship terbaik yang sesuai dengan kriteria dan preferensi mereka.
            Fokus utama sistem ini adalah meranking lowongan magang yang tersedia berdasarkan
            berbagai kriteria (baik yang bersifat persyaratan maupun preferensi) yang ditentukan
            oleh mahasiswa. Metode yang digunakan adalah Additive Ratio Assessment (ARAS) untuk
            mengevaluasi dan mengurutkan alternatif lowongan berdasarkan seberapa dekat mereka
            dengan "lowongan ideal" menurut preferensi mahasiswa, yang diukur melalui derajat
            utilitas.
          </p>
        </div>

        <!-- Gambar -->
        <div class="md:w-1/3">
          <img
            src="@/assets/about-section.jpg"
            alt="Tentang Website"
            class="w-full rounded-xl shadow-md border-4 border-solid"
          />
        </div>
      </div>
    </section>

    <!-- Metode SPK -->
    <section class="bg-white py-10 px-4 sm:px-6">
      <div class="max-w-4xl mx-auto text-center">
        <h2 class="text-base sm:text-xl font-bold text-blue-500 mb-4">Metode SPK yang Digunakan</h2>
        <p class="text-gray-700 text-sm sm:text-md leading-relaxed text-justify">
          Metode <strong>ARAS (Additive Ratio Assessment)</strong> merupakan salah satu metode dalam
          sistem pendukung keputusan (SPK) yang digunakan untuk menentukan alternatif terbaik dari
          sejumlah pilihan berdasarkan berbagai kriteria. Metode ini menilai setiap alternatif
          dengan cara membandingkannya terhadap alternatif ideal dan menghitung nilai utilitas dari
          setiap alternatif.
        </p>
        <h3 class="text-sm md:text-md font-semibold text-gray-800 mb-2 text-left">
          Langkah-langkah perhitungan menggunakan metode ARAS:
        </h3>
        <ul class="text-gray-700 text-sm md:text-md text-left list-disc list-inside space-y-2">
          <li>
            <strong>Membangun Matriks Keputusan:</strong> Susun tabel yang berisi semua alternatif
            dan nilai pada setiap kriteria.
          </li>
          <li>
            <strong>Menentukan Jenis Kriteria:</strong> Identifikasi apakah setiap kriteria bersifat
            <em>benefit</em> (semakin besar semakin baik) atau <em>cost</em> (semakin kecil semakin
            baik).
          </li>
          <li>
            <strong>Menentukan Alternatif Ideal:</strong> Tambahkan baris alternatif ideal
            (X<sub>0</sub>) dengan nilai terbaik pada setiap kriteria.
          </li>
          <li>
            <strong>Melakukan Normalisasi:</strong>
            <ul class="list-[circle] pl-6">
              <li>Untuk kriteria benefit: x<sub>ij</sub> = x<sub>ij</sub> / ∑x<sub>ij</sub></li>
              <li>Untuk kriteria cost: x<sub>ij</sub> = min(x<sub>j</sub>) / x<sub>ij</sub></li>
            </ul>
          </li>
          <li>
            <strong>Menghitung Matriks Ternormalisasi Terbobot:</strong> Kalikan nilai normalisasi
            dengan bobot kriteria: q<sub>ij</sub> = w<sub>j</sub> × x<sub>ij</sub>
          </li>
          <li>
            <strong>Menghitung Nilai Optimal Setiap Alternatif:</strong> Jumlahkan semua nilai q<sub
              >ij</sub
            >
            pada setiap alternatif.
          </li>
          <li>
            <strong>Menghitung Nilai Utilitas:</strong>
            <br />
            U<sub>i</sub> = S<sub>i</sub> / S<sub>0</sub>, di mana S<sub>0</sub> adalah nilai
            optimal dari alternatif ideal.
          </li>
          <li>
            <strong>Menentukan Peringkat:</strong> Alternatif dengan nilai utilitas tertinggi adalah
            yang paling direkomendasikan.
          </li>
        </ul>
      </div>
    </section>

    <section class="py-10 sm:py-14 bg-white text-center px-4 sm:px-6">
      <div class="max-w-6xl mx-auto grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        <div class="p-6 border rounded-lg shadow-md bg-gray-50 transition hover:shadow-lg">
          <div class="mb-2 flex justify-center">
            <svg
              class="w-10 h-10 text-blue-500 mb-2"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M5.121 17.804A8.001 8.001 0 0112 16a8.001 8.001 0 016.879 1.804M15 11a3 3 0 11-6 0 3 3 0 016 0z"
              ></path>
            </svg>
          </div>
          <h3 class="text-sm sm:text-base font-bold text-blue-500 mb-1">Pengguna Aktif</h3>
          <p class="text-2xl sm:text-3xl font-semibold text-gray-800">{{ animatedCounts.users }}</p>
        </div>
        <div class="p-6 border rounded-lg shadow-md bg-gray-50 transition hover:shadow-lg">
          <div class="mb-2 flex justify-center">
            <svg
              class="w-10 h-10 text-blue-500 mb-2"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M3 21h18M9 8h6M9 12h6M9 16h6M5 21V5a2 2 0 012-2h10a2 2 0 012 2v16"
              ></path>
            </svg>
          </div>
          <h3 class="text-sm sm:text-base font-bold text-blue-500 mb-1">Perusahaan Terdaftar</h3>
          <p class="text-2xl sm:text-3xl font-semibold text-gray-800">
            {{ animatedCounts.companies }}
          </p>
        </div>
        <div class="p-6 border rounded-lg shadow-md bg-gray-50 transition hover:shadow-lg">
          <div class="mb-2 flex justify-center">
            <svg
              class="w-10 h-10 text-blue-500 mb-2"
              fill="none"
              stroke="currentColor"
              stroke-width="2"
              viewBox="0 0 24 24"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.518 4.674a1 1 0 00.95.69h4.91c.969 0 1.371 1.24.588 1.81l-3.975 2.89a1 1 0 00-.364 1.118l1.518 4.674c.3.921-.755 1.688-1.54 1.118l-3.974-2.89a1 1 0 00-1.176 0l-3.974 2.89c-.784.57-1.838-.197-1.54-1.118l1.518-4.674a1 1 0 00-.364-1.118L2.083 10.1c-.783-.57-.38-1.81.588-1.81h4.91a1 1 0 00.95-.69l1.518-4.674z"
              ></path>
            </svg>
          </div>
          <h3 class="text-sm sm:text-base font-bold text-blue-500 mb-1">Tingkat Kepuasan</h3>
          <p class="text-2xl sm:text-3xl font-semibold text-gray-800">
            {{ animatedCounts.satisfaction }}%
          </p>
        </div>
      </div>
    </section>

    <FooterBar />
  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import FooterBar from '@/components/FooterBar.vue'
import { Swiper, SwiperSlide } from 'swiper/vue'
import { Autoplay, EffectFade } from 'swiper/modules'
import 'swiper/swiper-bundle.css'

import banner1 from '@/assets/carousel1.png'
import banner2 from '@/assets/carousel2.png'
import banner3 from '@/assets/carousel3.png'

import partner1 from '@/assets/mitra/partner7.png'
import partner2 from '@/assets/mitra/partner2.png'
import partner3 from '@/assets/mitra/partner3.png'
import partner4 from '@/assets/mitra/partner4.png'
import partner5 from '@/assets/mitra/partner5.png'
import partner6 from '@/assets/mitra/partner6.png'

export default {
  name: 'LandingPageView',
  components: {
    NavigationBar,
    FooterBar,
    Swiper,
    SwiperSlide,
  },
  setup() {
    return {
      modules: [Autoplay, EffectFade],
    }
  },
  data() {
    return {
      images: [banner1, banner2, banner3],
      partners: [partner1, partner2, partner3, partner4, partner5, partner6],
      targetCounts: {
        users: 52,
        companies: 120,
        satisfaction: 96,
      },
      animatedCounts: {
        users: 0,
        companies: 0,
        satisfaction: 0,
      },
    }
  },
  mounted() {
    this.animateCounts()
  },
  methods: {
    animateCounts() {
      Object.keys(this.animatedCounts).forEach((key) => {
        const target = this.targetCounts[key]
        let current = 0
        const step = Math.ceil(target / 60)
        const interval = setInterval(() => {
          current += step
          if (current >= target) {
            current = target
            clearInterval(interval)
          }
          this.animatedCounts[key] = current
        }, 30)
      })
    },
  },
}
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 1s;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
