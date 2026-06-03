# File: schemas.py (Final)

from pydantic import BaseModel, EmailStr
from typing import List, Optional, Any, Dict
from datetime import datetime
import models

# --- Skema untuk Token JWT ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# --- Skema untuk Pengguna (User) ---
class UserBase(BaseModel):
    email: EmailStr
    nama_lengkap: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id_user: int
    is_active: bool
    created_at: datetime
    class Config:
        # PERUBAHAN: 'orm_mode' diubah menjadi 'from_attributes'
        from_attributes = True

# --- Skema untuk Kriteria ---
class Kriteria(BaseModel):
    id_kriteria: int
    kode_kriteria: str
    nama_kriteria: str
    tipe_kriteria: models.TipeKriteriaEnum
    deskripsi_singkat: Optional[str] = None
    class Config:
        # PERUBAHAN: 'orm_mode' diubah menjadi 'from_attributes'
        from_attributes = True

# --- Skema untuk Alternatif ---
class Alternatif(BaseModel):
    id_alternatif: int
    nama_perusahaan: str
    class Config:
        # PERUBAHAN: 'orm_mode' diubah menjadi 'from_attributes'
        from_attributes = True

# --- Skema untuk Penilaian (Struktur Baru) ---
class Penilaian(BaseModel):
    id_alternatif: int
    jarak_km: float
    peluang_karir: int
    reputasi_perusahaan: int
    relevansi_proyek: int
    teknologi_baru: int
    kualitas_mentorship: int
    class Config:
        # PERUBAHAN: 'orm_mode' diubah menjadi 'from_attributes'
        from_attributes = True

# --- Skema untuk Input Perhitungan ---
class BobotKriteria(BaseModel):
    peringkat: List[str]

# --- Skema untuk Output Perhitungan ---
class HasilItem(BaseModel):
    peringkat: int
    id_alternatif: int
    nama_perusahaan: str
    skor_utilitas: float

class HasilPerhitungan(BaseModel):
    id_riwayat: int
    tanggal_perhitungan: datetime
    hasil: List[HasilItem]

# --- Skema untuk Riwayat ---
class Riwayat(BaseModel):
    id_riwayat: int
    id_user: int
    tanggal_perhitungan: datetime
    bobot_kriteria: Any
    hasil_rekomendasi: Any
    class Config:
        # PERUBAHAN: 'orm_mode' diubah menjadi 'from_attributes'
        from_attributes = True