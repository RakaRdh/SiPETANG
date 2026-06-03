# 🖥️ Sistem Pendukung Keputusan (SPK) Pemilihan Tempat Magang - Metode ARAS

Aplikasi Sistem Pendukung Keputusan (SPK) berbasis web untuk membantu mahasiswa dalam menentukan tempat magang terbaik dengan menggunakan metode **ARAS (Additive Ratio Assessment)**.

---

## 🛠️ Tech Stack

Aplikasi ini dibagi menjadi dua bagian utama: **Backend** (API) dan **Frontend** (Antarmuka Pengguna).

### Backend
* **Framework**: FastAPI (Python)
* **ORM**: SQLAlchemy
* **Database**: PostgreSQL (menggunakan `psycopg2-binary`) / SQLite
* **Authentication**: JWT (JSON Web Tokens) dengan `python-jose` & `passlib`
* **Server**: Uvicorn

### Frontend
* **Framework**: Vue 3 (Vite)
* **State Management**: Pinia
* **Router**: Vue Router
* **Styling**: TailwindCSS & Vanilla CSS
* **HTTP Client**: Axios
* **Library Lain**: Swiper (carousel), SweetAlert2 (notifikasi)

---

## 📂 Project Structure

```text
SPK/
├── BACKEND/
│   └── app/
│       ├── routers/           # Endpoint API (auth, kriteria, alternatif, perhitungan, dll)
│       ├── app.py             # File utama FastAPI
│       ├── config.py          # Konfigurasi app & environment
│       ├── database.py        # Setup & engine database
│       ├── models.py          # Model skema database (SQLAlchemy)
│       ├── schemas.py         # Skema validasi Pydantic
│       ├── security.py        # Pengolahan password hashing & JWT
│       └── requirements.txt   # Dependensi Python
│
├── FRONTEND/
│   └── FRONTEND/
│       ├── src/
│       │   ├── assets/        # Asset gambar, CSS global, logo
│       │   ├── components/    # Komponen Vue yang reusable
│       │   ├── router/        # Konfigurasi Vue Router
│       │   ├── stores/        # Pinia state stores (auth, data, dll)
│       │   └── views/         # Halaman utama aplikasi (Admin Dashboard, SPK, Login, dll)
│       ├── package.json       # Dependensi npm & skrip
│       └── vite.config.js     # Konfigurasi bundler Vite
│
├── .gitignore                 # Konfigurasi Git ignore
└── README.md                  # Dokumentasi proyek
```

---

## 🚀 Instalasi & Cara Menjalankan

### 1. Prasyarat (Prerequisites)
Pastikan Anda sudah menginstal:
* [Python 3.10+](https://www.python.org/downloads/)
* [Node.js 18+](https://nodejs.org/)

---

### 2. Setup Backend (FastAPI)

1. Masuk ke direktori backend:
   ```bash
   cd BACKEND/app
   ```

2. Buat virtual environment (opsional namun disarankan):
   ```bash
   python -m venv .venv
   ```
   Aktifkan virtual environment:
   * **Windows (PowerShell):** `.venv\Scripts\Activate.ps1`
   * **Linux/macOS:** `source .venv/bin/activate`

3. Instal semua dependensi:
   ```bash
   pip install -r requirements.txt
   ```

4. Buat file `.env` di dalam folder `BACKEND/app/` dan sesuaikan konfigurasinya:
   ```env
   DATABASE_URL=postgresql://username:password@localhost:5432/spk_aras
   SECRET_KEY=ganti_dengan_secret_key_anda_yang_sangat_rahasia
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```
   *(Catatan: Anda juga bisa menggunakan SQLite untuk development dengan format `sqlite:///./spk.db`)*

5. Jalankan server FastAPI:
   ```bash
   uvicorn app:app --reload
   ```
   API akan berjalan di `http://localhost:8000`. Dokumentasi interaktif Swagger UI dapat diakses di `http://localhost:8000/docs`.

---

### 3. Setup Frontend (Vue 3 + Vite)

1. Masuk ke direktori frontend:
   ```bash
   cd FRONTEND/FRONTEND
   ```

2. Instal dependensi Node:
   ```bash
   npm install
   ```

3. Jalankan server development:
   ```bash
   npm run dev
   ```
   Aplikasi frontend Vue akan berjalan di `http://localhost:5173`.

---

## 📝 Fitur Utama
1. **Autentikasi Pengguna**: Login & Registrasi (Multi-role: Admin & Mahasiswa/User).
2. **Kelola Kriteria**: Admin dapat mengelola kriteria penilaian magang beserta bobotnya.
3. **Kelola Alternatif**: Admin/User dapat memasukkan daftar tempat magang sebagai alternatif.
4. **Perhitungan Metode ARAS**: Sistem otomatis melakukan proses normalisasi matriks, perkalian bobot, pencarian nilai optimal ($S_i$), dan perangkingan ($K_i$) alternatif.
5. **Riwayat Perhitungan**: Menyimpan riwayat hasil keputusan untuk referensi di masa mendatang.
