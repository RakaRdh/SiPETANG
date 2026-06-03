import os
# PERUBAHAN UTAMA: Impor BaseSettings dari paket pydantic_settings
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Memuat variabel dari file .env ke dalam environment sistem
load_dotenv()

class Settings(BaseSettings):
    """
    Kelas untuk mengelola semua konfigurasi aplikasi.
    """
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        # Menentukan nama file environment
        env_file = ".env"
        # Menentukan bahwa file .env berada di dalam folder app
        env_file_encoding = 'utf-8'

# Membuat satu instance Settings yang akan diimpor dan digunakan di seluruh proyek
settings = Settings()
