<template>
  <div class="min-h-screen bg-white text-black">
    <NavigationBar />
    <div class="max-w-7xl mx-auto px-4 py-10">
      <h1 class="text-2xl font-bold text-blue-500 mb-8 text-center">Profil Perusahaan Mitra</h1>

      <div v-if="loading" class="text-center text-gray-500 py-10">Memuat data perusahaan...</div>
      <div
        v-else-if="error"
        class="text-red-600 bg-red-100 border border-red-300 p-4 rounded text-center"
      >
        {{ error }}
      </div>
      <div v-else class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
        <div
          v-for="(company, index) in companies"
          :key="index"
          class="bg-gray-50 rounded-lg shadow-md hover:shadow-lg transition overflow-hidden"
          :class="{ 'ring-4 ring-blue-400': highlightedCompany == company.id_alternatif }"
        >
          <div class="bg-white p-4 flex justify-center items-center h-36">
            <img
              :src="company.logo_perusahaan || defaultLogo"
              alt="Logo"
              class="h-full max-h-28 object-contain"
            />
          </div>
          <div class="p-4">
            <h2 class="text-blue-500 font-semibold text-lg mb-1">{{ company.nama_perusahaan }}</h2>
            <p class="text-sm text-gray-700 mb-2">{{ company.alamat }}</p>
            <p class="text-sm text-gray-600 line-clamp-3 mb-3">
              {{ company.deskripsi_perusahaan || 'Belum ada deskripsi.' }}
            </p>
            <div class="text-sm text-gray-600">
              <p><strong>Kontak:</strong> {{ company.kontak_email || '-' }}</p>
              <p>
                <strong>Website:</strong>
                <a
                  :href="company.website"
                  target="_blank"
                  class="text-blue-500 hover:underline"
                  v-if="company.website"
                >
                  {{ company.website }}
                </a>
                <span v-else>-</span>
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <FooterBar />
  </div>
</template>

<script>
import axios from 'axios'
import NavigationBar from '@/components/NavigationBar.vue'
import FooterBar from '@/components/FooterBar.vue'

const API_BASE_URL = 'http://rather-blogger.gl.at.ply.gg:28663'

export default {
  name: 'ProfilPerusahaanView',
  components: {
    NavigationBar,
    FooterBar,
  },
  data() {
    return {
      companies: [],
      loading: true,
      error: '',
      highlightedId: null,
      highlightedCompany: null,
      defaultLogo: 'https://via.placeholder.com/100x60?text=Logo',
    }
  },
  async created() {
    const token = localStorage.getItem('accessToken')
    if (!token) {
      return this.$router.push('/login')
    }

    this.api = axios.create({
      baseURL: API_BASE_URL,
      headers: { Authorization: `Bearer ${token}` },
    })

    this.highlightedId = this.$route.query.highlight || null

    try {
      const response = await this.api.get('/alternatif/')
      this.companies = response.data

      // Jika ada highlight, tandai dan scroll
      if (this.highlightedId) {
        this.highlightedCompany = this.highlightedId

        this.$nextTick(() => {
          const el = this.$refs.highlightedCard
          if (el && el[0]) {
            el[0].scrollIntoView({ behavior: 'smooth', block: 'center' })
          }
        })

        // Hapus highlight setelah beberapa detik
        setTimeout(() => {
          this.highlightedCompany = null
        }, 2500)
      }
    } catch (err) {
      this.error = err.response?.data?.detail || 'Gagal mengambil data perusahaan.'
    } finally {
      this.loading = false
    }
  },
}
</script>

<style scoped>
.line-clamp-3 {
  display: -webkit-box;
  display: box;
  /* optional fallback for older non-webkit */
  -webkit-line-clamp: 3;
  line-clamp: 3;
  /* proper standard syntax, future-proof */
  -webkit-box-orient: vertical;
  box-orient: vertical;
  /* optional fallback */
  overflow: hidden;
}
</style>
