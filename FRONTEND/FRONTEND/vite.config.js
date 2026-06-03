import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue(), vueDevTools()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  server: {
    // Membuat server dapat diakses melalui IP
    host: true,

    // --- PERUBAHAN DI SINI ---
    // Menambahkan alamat playit.gg Anda ke daftar host yang diizinkan
    // Ini adalah langkah keamanan yang diperlukan oleh Vite.
    allowedHosts: ['includes-china.gl.at.ply.gg'],
  },
})
