<template>
  <div class="min-h-screen bg-white text-black flex font-sans">
    <!-- Sidebar -->
    <aside
      class="hidden md:flex md:flex-col md:justify-between w-64 fixed h-full bg-gradient-to-b from-blue-600 to-cyan-500 text-white p-6 shadow-lg z-50 scroll-smooth">
      <div>
        <div class="flex justify-center mb-10">
          <img src="@/assets/logo-putih.png" alt="Logo" class="h-14" />
        </div>
        <nav class="space-y-3 text-sm">
          <a href="#perusahaan" class="flex items-center gap-2 hover:bg-blue-700 rounded px-4 py-2">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M3 10h18M3 6h18M3 14h18M3 18h18" />
            </svg>
            Data Perusahaan
          </a>
          <a href="#pengguna" class="flex items-center gap-2 hover:bg-blue-700 rounded px-4 py-2">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                d="M5.121 17.804A9.002 9.002 0 0112 15a9.002 9.002 0 016.879 2.804M15 10a3 3 0 11-6 0 3 3 0 016 0z" />
            </svg>
            Data Pengguna
          </a>
        </nav>
      </div>
      <button @click="handleLogout"
        class="mt-6 bg-white text-blue-600 hover:text-white hover:bg-red-500 font-bold py-2 rounded transition duration-300">
        Logout
      </button>
    </aside>

    <!-- Navbar atas hanya untuk layar kecil -->
    <div
      class="md:hidden fixed top-0 left-0 right-0 bg-gradient-to-r from-blue-600 to-cyan-500 text-white z-50 px-4 py-3 flex justify-between items-center shadow">
      <img src="@/assets/logo-putih.png" alt="Logo" class="h-10" />
      <button @click="toggleMobileMenu" class="focus:outline-none">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16" />
        </svg>
      </button>
    </div>

    <div v-if="showMobileMenu" class="md:hidden fixed top-16 left-0 right-0 bg-white shadow z-40 text-black text-sm">
      <a href="#perusahaan" class="block px-4 py-2 border-b border-gray-200 hover:bg-gray-100">Data Perusahaan</a>
      <a href="#pengguna" class="block px-4 py-2 border-b border-gray-200 hover:bg-gray-100">Data Pengguna</a>
      <button @click="handleLogout"
        class="block w-full text-left px-4 py-2 text-red-600 hover:bg-red-100">Logout</button>
    </div>

    <!-- Main Content -->
    <main class="pt-20 md:pt-8 md:ml-64 w-full p-4 md:p-8 space-y-10 scroll-smooth">
      <!-- Error -->
      <div v-if="error" class="bg-red-100 border-l-4 border-red-500 text-red-700 p-4 rounded shadow-sm">
        <p class="font-bold">Terjadi Kesalahan</p>
        <p>{{ error }}</p>
      </div>

      <!-- Perusahaan Section -->
      <section id="perusahaan" class="p-6 bg-white rounded shadow border border-gray-200">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-lg font-bold text-blue-600">Manajemen Data Perusahaan</h2>
          <button @click="openModal('add')"
            class="bg-gradient-to-r from-blue-500 to-cyan-500 hover:from-blue-600 hover:to-cyan-600 text-white py-2 px-4 rounded shadow">
            Tambah Perusahaan
          </button>
        </div>

        <table class="w-full text-sm border-t">
          <thead class="bg-gray-50 text-gray-600 uppercase text-xs text-center">
            <tr>
              <th class="py-3 px-4 text-left">Nama</th>
              <th class="py-3 px-2">Jarak (KM)</th>
              <th class="py-3 px-2">Peluang Karir</th>
              <th class="py-3 px-2">Reputasi</th>
              <th class="py-3 px-2">Relevansi</th>
              <th class="py-3 px-2">Teknologi</th>
              <th class="py-3 px-2">Mentorship</th>
              <th class="py-3 px-2">Aksi</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="alt in alternatifs" :key="'p-' + alt.id_alternatif" class="hover:bg-gray-50 text-center">
              <td class="py-2 px-4 text-left">{{ alt.nama_perusahaan }}</td>
              <td class="py-2 px-2">{{ alt.jarak_km || 0 }}</td>
              <td class="py-2 px-2">{{ alt.peluang_karir || 0 }}</td>
              <td class="py-2 px-2">{{ alt.reputasi_perusahaan || 0 }}</td>
              <td class="py-2 px-2">{{ alt.relevansi_proyek || 0 }}</td>
              <td class="py-2 px-2">{{ alt.teknologi_baru || 0 }}</td>
              <td class="py-2 px-2">{{ alt.kualitas_mentorship || 0 }}</td>
              <td class="py-2 px-2 flex justify-center gap-2">
                <button @click="openModal('edit', alt)"
                  class="bg-yellow-400 text-white px-3 py-1 rounded hover:bg-yellow-500 text-xs">Edit</button>
                <button @click="confirmDelete(alt.id_alternatif)"
                  class="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600 text-xs">Hapus</button>
              </td>
            </tr>
          </tbody>
        </table>
      </section>

      <!-- Pengguna Section -->
      <section id="pengguna" class="p-6 bg-white rounded shadow border border-gray-200">
        <h2 class="text-lg font-bold text-blue-600 mb-4">Manajemen Pengguna</h2>
        <table class="w-full text-sm border-t">
          <thead class="bg-gray-50 text-gray-600 uppercase text-xs">
            <tr>
              <th class="py-3 px-4">Nama</th>
              <th class="py-3 px-4">Status</th>
              <th class="py-3 px-4">Tanggal</th>
              <th class="py-3 px-4 text-center">Aksi</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="usr in users" :key="usr.id_user" class="hover:bg-gray-50 text-center">
              <td class="py-3 px-4 text-left">{{ usr.nama_lengkap }}</td>
              <td class="py-3 px-4">
                <span :class="usr.is_active ? 'text-green-600' : 'text-red-600'">
                  {{ usr.is_active ? 'Aktif' : 'Nonaktif' }}
                </span>
              </td>
              <td class="py-3 px-4">{{ formatDate(usr.created_at) }}</td>
              <td class="py-3 px-4 text-center">
                <button v-if="usr.is_active" @click="toggleUserStatus(usr.id_user, false)"
                  class="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600 text-xs">Nonaktifkan</button>
                <button v-else @click="toggleUserStatus(usr.id_user, true)"
                  class="bg-green-500 text-white px-3 py-1 rounded hover:bg-green-600 text-xs">Aktifkan</button>
              </td>
            </tr>
          </tbody>
        </table>
      </section>
    </main>

    <!-- Modal -->
    <div v-if="isModalOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4"
      @click="closeModal">
      <div class="bg-white rounded-lg w-full max-w-3xl p-6" @click.stop>
        <h2 class="text-xl font-bold mb-4 text-blue-600">
          {{ modal.mode === 'add' ? 'Tambah' : 'Edit' }} Perusahaan
        </h2>
        <form @submit.prevent="handleSubmit">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <input v-model="form.alternatif.nama_perusahaan" placeholder="Nama Perusahaan" required
              class="p-2 border rounded" />
            <input v-model="form.alternatif.alamat" placeholder="Alamat" class="p-2 border rounded" />
            <input v-model="form.alternatif.kontak_email" placeholder="Email Kontak" class="p-2 border rounded" />
            <input v-model="form.alternatif.website" placeholder="Website" class="p-2 border rounded" />
            <textarea v-model="form.alternatif.deskripsi_perusahaan" class="p-2 border rounded col-span-2"
              placeholder="Deskripsi Perusahaan"></textarea>

            <input v-model.number="form.penilaian.jarak_km" type="number" placeholder="Jarak (KM)"
              class="p-2 border rounded" required />
            <input v-model.number="form.penilaian.peluang_karir" type="number" placeholder="Peluang Karir (1-10)"
              class="p-2 border rounded" />
            <input v-model.number="form.penilaian.reputasi_perusahaan" type="number" placeholder="Reputasi (1-10)"
              class="p-2 border rounded" />
            <input v-model.number="form.penilaian.relevansi_proyek" type="number" placeholder="Relevansi Proyek (1-10)"
              class="p-2 border rounded" />
            <input v-model.number="form.penilaian.teknologi_baru" type="number" placeholder="Teknologi Baru (1-10)"
              class="p-2 border rounded" />
            <input v-model.number="form.penilaian.kualitas_mentorship" type="number" placeholder="Mentorship (1-10)"
              class="p-2 border rounded" />
          </div>
          <div class="flex justify-end gap-4 mt-6">
            <button type="button" @click="closeModal"
              class="bg-gray-200 hover:bg-gray-300 text-black py-2 px-4 rounded">Batal</button>
            <button type="submit" class="bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded">Simpan</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>



<script>
import axios from 'axios'
import Swal from 'sweetalert2'
import { format, parseISO } from 'date-fns'
import { id } from 'date-fns/locale'

const API_BASE_URL = 'http://rather-blogger.gl.at.ply.gg:28663'

const initialFormState = () => ({
  alternatif: {
    nama_perusahaan: '',
    alamat: '',
    deskripsi_perusahaan: '',
    website: '',
    kontak_email: '',
    logo_perusahaan: '',
  },
  penilaian: {
    jarak_km: null,
    peluang_karir: null,
    reputasi_perusahaan: null,
    relevansi_proyek: null,
    teknologi_baru: null,
    kualitas_mentorship: null,
  },
})

export default {
  name: 'AdminDashboardView',
  data() {
    return {
      users: [],
      alternatifs: [],
      error: '',
      loading: true,
      isModalOpen: false,
      modal: {
        mode: 'add',
        id: null,
      },
      form: initialFormState(),
    }
  },
  async created() {
    const token = localStorage.getItem('accessToken')
    if (!token || localStorage.getItem('userType') !== 'admin') {
      this.$router.push('/login')
      return
    }
    this.api = axios.create({
      baseURL: API_BASE_URL,
      headers: { Authorization: `Bearer ${token}` },
    })
    this.fetchInitialData()
  },
  methods: {
    async fetchInitialData() {
      this.loading = true
      try {
        const [usersRes, altRes] = await Promise.all([
          this.api.get('/admin/users/'),
          this.api.get('/alternatif/'),
        ])
        this.users = usersRes.data
        this.alternatifs = altRes.data
      } catch (err) {
        this.handleApiError(err, 'Gagal memuat data awal.')
      } finally {
        this.loading = false
      }
    },

    formatDate(dateString) {
      if (!dateString) return 'N/A'
      try {
        const date = parseISO(dateString)
        if (isNaN(date.getTime())) throw new Error('Invalid date')
        return format(date, 'dd MMMM yyyy', { locale: id })
      } catch (error) {
        console.error('Gagal memformat tanggal:', dateString, error)
        return 'Format Salah'
      }
    },

    openModal(mode, data = null) {
      this.modal.mode = mode
      if (mode === 'edit' && data) {
        this.modal.id = data.id_alternatif
        this.form.alternatif = {
          nama_perusahaan: data.nama_perusahaan,
          alamat: data.alamat,
          deskripsi_perusahaan: data.deskripsi_perusahaan,
          website: data.website,
          kontak_email: data.kontak_email,
          logo_perusahaan: data.logo_perusahaan || '',
        }
        this.form.penilaian = {
          jarak_km: data.jarak_km ?? 0,
          peluang_karir: data.peluang_karir ?? 0,
          reputasi_perusahaan: data.reputasi_perusahaan ?? 0,
          relevansi_proyek: data.relevansi_proyek ?? 0,
          teknologi_baru: data.teknologi_baru ?? 0,
          kualitas_mentorship: data.kualitas_mentorship ?? 0,
        }
      } else {
        this.form = initialFormState()
        this.modal.id = null
      }
      this.isModalOpen = true
    },

    closeModal() {
      this.isModalOpen = false
    },

    async handleSubmit() {
      try {
        if (this.modal.mode === 'add') {
          await this.api.post('/admin/alternatifs/', this.form)
          Swal.fire('Sukses!', 'Alternatif baru berhasil ditambahkan.', 'success')
        } else {
          await this.api.put(`/admin/alternatifs/${this.modal.id}`, this.form)
          Swal.fire('Sukses!', 'Data alternatif berhasil diperbarui.', 'success')
        }
        this.fetchInitialData()
        this.closeModal()
      } catch (err) {
        this.handleApiError(err, 'Gagal menyimpan data.')
      }
    },

    async confirmDelete(id) {
      const result = await Swal.fire({
        title: 'Anda yakin?',
        text: 'Data perusahaan dan nilai terkait akan dihapus permanen!',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#6e7881',
        confirmButtonText: 'Ya, hapus!',
        cancelButtonText: 'Batal',
      })
      if (result.isConfirmed) {
        try {
          await this.api.delete(`/admin/alternatifs/${id}`)
          Swal.fire('Terhapus!', 'Data perusahaan telah dihapus.', 'success')
          this.fetchInitialData()
        } catch (err) {
          this.handleApiError(err, 'Gagal menghapus data.')
        }
      }
    },

    async toggleUserStatus(userId, shouldBeActive) {
      const actionText = shouldBeActive ? 'mengaktifkan' : 'menonaktifkan'
      const endpoint = shouldBeActive
        ? `/admin/users/${userId}/activate`
        : `/admin/users/${userId}/deactivate`
      const confirmColor = shouldBeActive ? '#3085d6' : '#d33'

      const result = await Swal.fire({
        title: 'Anda yakin?',
        text: `Anda akan ${actionText} pengguna ini.`,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: confirmColor,
        cancelButtonColor: '#6e7881',
        confirmButtonText: `Ya, ${actionText}!`,
        cancelButtonText: 'Batal',
      })

      if (result.isConfirmed) {
        try {
          await this.api.put(endpoint)
          Swal.fire('Berhasil!', `Pengguna telah di-${actionText}.`, 'success')
          this.fetchInitialData()
        } catch (err) {
          this.handleApiError(err, `Gagal ${actionText} pengguna.`)
        }
      }
    },

    async handleLogout() {
      const confirm = await Swal.fire({
        title: 'Logout?',
        text: 'Apakah Anda yakin ingin keluar?',
        icon: 'question',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Ya, Logout',
      })
      if (confirm.isConfirmed) {
        localStorage.removeItem('accessToken')
        localStorage.removeItem('tokenType')
        localStorage.removeItem('userType')
        this.$router.push('/login')
      }
    },

    handleApiError(err, defaultMessage) {
      const status = err?.response?.status
      const msg = err?.response?.data?.detail || defaultMessage

      if (status === 401 || localStorage.getItem('userType') !== 'admin') {
        Swal.fire({
          icon: 'warning',
          title: 'Session Berakhir',
          text: 'Sesi login Anda sudah habis atau akses tidak valid. Silakan login kembali.',
          confirmButtonText: 'Login Ulang',
          confirmButtonColor: '#3085d6',
        }).then(() => {
          localStorage.removeItem('accessToken')
          localStorage.removeItem('tokenType')
          localStorage.removeItem('userType')
          this.$router.push('/login')
        })
      } else {
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: msg,
        })
        console.error(err)
      }
    },
  },
}
</script>
