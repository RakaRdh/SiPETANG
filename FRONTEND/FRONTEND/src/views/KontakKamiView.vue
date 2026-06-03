<template>
  <div>
    <NavigationBar />

    <div class="max-w-3xl mx-auto my-12 px-4 sm:px-6 lg:px-8">
      <h1 class="text-xl font-semibold mb-4 text-center sm:text-left text-blue-600">Kontak</h1>
      <p class="mb-6 text-gray-700 text-sm sm:text-base text-justify">
        Terima kasih telah mengunjungi website kami. Ingin tanya-tanya tentang layanan kami? Silakan tuliskan pesan Anda pada kolom di bawah ini. Tim kami akan menghubungi Anda secepatnya.
      </p>
      <form @submit.prevent="submitForm" class="space-y-5">
        <div>
          <label class="block font-medium text-sm sm:text-base mb-1">Nama</label>
          <input v-model="form.nama" type="text" class="w-full border border-gray-400 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-sky-400" placeholder="Nama Anda" />
        </div>
        <div>
          <label class="block font-medium text-sm sm:text-base mb-1">Email</label>
          <input v-model="form.email" type="email" class="w-full border border-gray-400 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-sky-400" placeholder="email@domain.com" />
        </div>
        <div>
          <label class="block font-medium text-sm sm:text-base mb-1">Nomor HP</label>
          <input v-model="form.nomorhp" type="text" class="w-full border border-gray-400 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-sky-400" placeholder="08xxxxxxxxxx" />
        </div>
        <div>
          <label class="block font-medium text-sm sm:text-base mb-1">Domisili</label>
          <input v-model="form.domisili" type="text" class="w-full border border-gray-400 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-sky-400" placeholder="Kota Anda" />
        </div>
        <div>
          <label class="block font-medium text-sm sm:text-base mb-1">Pertanyaan</label>
          <textarea v-model="form.pertanyaan" rows="5" class="w-full border border-gray-400 rounded-md px-4 py-2 focus:outline-none focus:ring-2 focus:ring-sky-400" placeholder="Tulis pertanyaan Anda di sini..."></textarea>
        </div>
        <div class="text-center sm:text-left">
          <button type="submit" class="bg-gradient-to-r from-cyan-500 to-blue-500 hover:from-cyan-600 hover:to-blue-600 text-white px-6 py-2 rounded-md transition duration-300">
            Kirim Pesan
          </button>
        </div>
      </form>
    </div>

    <FooterBar />
  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import FooterBar from '@/components/FooterBar.vue'
import Swal from 'sweetalert2'

export default {
  name: 'KontakKamiView',
  components: {
    NavigationBar,
    FooterBar
  },
  data() {
    return {
      form: {
        nama: '',
        email: '',
        nomorhp: '',
        domisili: '',
        pertanyaan: ''
      }
    }
  },
  methods: {
    async submitForm() {
      const { nama, email, nomorhp, domisili, pertanyaan } = this.form

      const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/
      if (!nama || !email || !nomorhp || !domisili || !pertanyaan) {
        return Swal.fire('Gagal', 'Semua kolom wajib diisi!', 'warning')
      }
      if (!email.match(emailPattern)) {
        return Swal.fire('Format Email Salah', 'Email tidak valid.', 'error')
      }

      // Simulasi pengiriman form sukses
      await Swal.fire('Berhasil', 'Formulir Anda telah dikirim.', 'success')
      this.form = {
        nama: '',
        email: '',
        nomorhp: '',
        domisili: '',
        pertanyaan: ''
      }
    }
  }
}
</script>
