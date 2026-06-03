from sqlalchemy.orm import Session
# PERUBAHAN: Semua impor sekarang absolut (tanpa titik).
import models
import schemas
import security

# === CRUD untuk User ===
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(
        email=user.email,
        nama_lengkap=user.nama_lengkap,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def set_user_active_status(db: Session, user_id: int, is_active: bool):
    db_user = db.query(models.User).filter(models.User.id_user == user_id).first()
    if db_user:
        db_user.is_active = is_active
        db.commit()
        db.refresh(db_user)
    return db_user

# === CRUD untuk Kriteria ===
def get_all_kriteria(db: Session):
    return db.query(models.Kriteria).all()

# === CRUD untuk Alternatif ===
def get_all_alternatif(db: Session):
    return db.query(models.Alternatif).all()

# === CRUD untuk Penilaian ===
def get_all_penilaian(db: Session):
    return db.query(models.Penilaian).all()

# === CRUD untuk Riwayat ===
def create_riwayat(db: Session, user_id: int, bobot: dict, hasil: list):
    db_riwayat = models.Riwayat(
        id_user=user_id,
        bobot_kriteria=bobot,
        hasil_rekomendasi=hasil
    )
    db.add(db_riwayat)
    db.commit()
    db.refresh(db_riwayat)
    return db_riwayat

def get_riwayat_by_user_id(db: Session, user_id: int):
    """Mendapatkan semua riwayat perhitungan untuk user tertentu, diurutkan dari yang terbaru."""
    return db.query(models.Riwayat).filter(models.Riwayat.id_user == user_id).order_by(models.Riwayat.tanggal_perhitungan.desc()).all()