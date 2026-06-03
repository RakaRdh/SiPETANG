from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
# PERUBAHAN: Impor router riwayat
from routers import auth, users, kriteria, alternatif, perhitungan, riwayat

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API SPK Pemilihan Tempat Magang",
    description="Backend Lengkap untuk Sistem Pendukung Keputusan dengan metode ARAS.",
    version="1.0.1",
)

origins = [
    "http://localhost:5173", # Ganti dengan port Vue dev server Anda
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
def read_root():
    return {"status": "API Berjalan", "docs": "/docs"}

# Mendaftarkan semua router
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(kriteria.router)
app.include_router(alternatif.router)
app.include_router(perhitungan.router)
# PERUBAHAN: Daftarkan router riwayat
app.include_router(riwayat.router)
