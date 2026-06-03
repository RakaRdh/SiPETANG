import { createRouter, createWebHistory } from 'vue-router'
import LandingPageView from '../views/LandingPageView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import SPKView from '../views/SPKView.vue'
import HistoryView from '../views/HistoryView.vue'
import ProfilPerusahaanView from '@/views/ProfilPerusahaanView.vue'
import ProfilPenggunaView from '@/views/ProfilPenggunaView.vue'
import KontakKamiView from '@/views/KontakKamiView.vue'
import TentangKamiView from '@/views/TentangKamiView.vue'
import AdminDashboardView from '../views/admin/AdminDashboardView.vue'

const routes = [
  // --- Rute Publik (tidak perlu login) ---
  {
    path: '/',
    redirect: '/login',
  },
  {
    path: '/landingpage',
    name: 'landingpage',
    component: LandingPageView,
    meta: { title: 'Selamat Datang - SiPETANG' },
  },
  {
    path: '/login',
    name: 'login',
    component: LoginView,
    meta: { title: 'Login - SiPETANG' },
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView,
    meta: { title: 'Register - SiPETANG' },
  },
  {
    path: '/kontak-kami',
    name: 'kontakkami',
    component: KontakKamiView,
    meta: { title: 'Kontak Kami - SiPETANG' },
  },
  {
    path: '/tentang-kami',
    name: 'tentangkami',
    component: TentangKamiView,
    meta: { title: 'Tentang Kami - SiPETANG' },
  },

  // --- Rute Terproteksi untuk User Biasa ---
  {
    path: '/spk',
    name: 'spk',
    component: SPKView,
    meta: { title: 'SPK - SiPETANG', requiresAuth: true, role: 'user' },
  },
  {
    path: '/history',
    name: 'history',
    component: HistoryView,
    meta: { title: 'History - SiPETANG', requiresAuth: true, role: 'user' },
  },
  {
    path: '/profil-perusahaan',
    name: 'profilperusahaan',
    component: ProfilPerusahaanView,
    meta: { title: 'Profil Perusahaan - SiPETANG', requiresAuth: true, role: 'user' },
  },
  {
    path: '/profil-pengguna',
    name: 'profilpengguna',
    component: ProfilPenggunaView,
    meta: { title: 'Profil Anda - SiPETANG', requiresAuth: true, role: 'user' },
  },

  // --- Rute Terproteksi untuk Admin ---
  {
    path: '/admin/dashboard',
    name: 'admin-dashboard',
    component: AdminDashboardView,
    meta: { title: 'Admin Dashboard - SiPETANG', requiresAuth: true, role: 'admin' },
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior() {
    return { top: 0 }
  },
})

// --- PENJAGA NAVIGASI (NAVIGATION GUARD) LENGKAP ---
router.beforeEach((to, from, next) => {
  document.title = to.meta.title || 'SiPETANG'

  const token = localStorage.getItem('accessToken')
  const userType = localStorage.getItem('userType')

  // Jika rute yang dituju memerlukan autentikasi
  if (to.meta.requiresAuth) {
    if (!token) {
      // Jika tidak ada token, paksa kembali ke halaman login
      next({ name: 'login' })
    } else {
      // Jika ada token, periksa apakah peran pengguna sesuai
      if (to.meta.role && to.meta.role !== userType) {
        // Jika peran tidak sesuai, arahkan ke dasbor default masing-masing
        if (userType === 'admin') {
          next({ name: 'admin-dashboard' })
        } else {
          next({ name: 'landingpage' }) // Halaman default untuk user
        }
      } else {
        // Jika token ada dan peran sesuai, izinkan akses
        next()
      }
    }
  } else {
    // Jika rute tidak memerlukan autentikasi (publik), izinkan akses
    // Juga tangani kasus jika user yang sudah login mencoba mengakses halaman login/register
    if ((to.name === 'login' || to.name === 'register') && token) {
      if (userType === 'admin') {
        next({ name: 'admin-dashboard' })
      } else {
        next({ name: 'landingpage' })
      }
    } else {
      next()
    }
  }
})

export default router
