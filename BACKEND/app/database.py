from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# PERUBAHAN UTAMA: Titik sebelum 'config' telah dihapus.
from config import settings

# Membuat 'engine' untuk koneksi ke database sesuai dengan URL di config
engine = create_engine(settings.DATABASE_URL)

# Membuat sebuah kelas SessionLocal yang akan menjadi sesi database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Membuat sebuah 'Base' class. Semua model tabel akan menjadi turunan dari kelas ini.
Base = declarative_base()

def get_db():
    """
    Sebuah 'dependency' untuk FastAPI.
    Fungsi ini akan membuat sesi database baru untuk setiap request yang masuk
    dan akan otomatis menutupnya setelah request selesai.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
