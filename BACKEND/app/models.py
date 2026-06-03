from sqlalchemy import (Boolean, Column, Integer, String, Enum as SQLAlchemyEnum, Text,
                        ForeignKey, DateTime, JSON, Float)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from database import Base
import enum

class TipeKriteriaEnum(str, enum.Enum):
    benefit = "benefit"
    cost = "cost"

class User(Base):
    __tablename__ = "tbl_users"
    id_user = Column(Integer, primary_key=True, index=True)
    nama_lengkap = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    riwayat = relationship("Riwayat", back_populates="pemilik")

class Kriteria(Base):
    __tablename__ = "tbl_kriteria"
    id_kriteria = Column(Integer, primary_key=True, index=True)
    kode_kriteria = Column(String(10), unique=True, nullable=False)
    nama_kriteria = Column(String(255), nullable=False)
    tipe_kriteria = Column(SQLAlchemyEnum(TipeKriteriaEnum), nullable=False)
    deskripsi_singkat = Column(Text)

class Alternatif(Base):
    __tablename__ = "tbl_alternatif"
    id_alternatif = Column(Integer, primary_key=True, index=True)
    nama_perusahaan = Column(String(255), nullable=False)
    alamat = Column(Text)
    deskripsi_perusahaan = Column(Text)
    website = Column(String(255))
    kontak_email = Column(String(255))
    logo_perusahaan = Column(String(255))

class Penilaian(Base):
    __tablename__ = "tbl_penilaian"
    # --- STRUKTUR BARU UNTUK MENYIMPAN NILAI MENTAH ---
    id_penilaian = Column(Integer, primary_key=True, index=True)
    id_alternatif = Column(Integer, ForeignKey("tbl_alternatif.id_alternatif", ondelete="CASCADE"), unique=True, nullable=False)
    jarak_km = Column(Float, nullable=False) # Jarak dalam KM (cost)
    peluang_karir = Column(Integer, nullable=False) # Skala 1-10 (benefit)
    reputasi_perusahaan = Column(Integer, nullable=False) # Skala 1-10 (benefit)
    relevansi_proyek = Column(Integer, nullable=False) # Skala 1-10 (benefit)
    teknologi_baru = Column(Integer, nullable=False) # Skala 1-10 (benefit)
    kualitas_mentorship = Column(Integer, nullable=False) # Skala 1-10 (benefit)

class Riwayat(Base):
    __tablename__ = "tbl_riwayat"
    id_riwayat = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("tbl_users.id_user", ondelete="CASCADE"), nullable=False)
    tanggal_perhitungan = Column(DateTime(timezone=True), server_default=func.now())
    bobot_kriteria = Column(JSONB)
    hasil_rekomendasi = Column(JSONB)
    pemilik = relationship("User", back_populates="riwayat")
