from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

# Perubahan: Impor absolut dari root direktori proyek
import crud
import schemas
from database import get_db
from routers.users import get_current_active_user # Impor dari dalam package routers

router = APIRouter(
    prefix="/kriteria",
    tags=["Kriteria"],
    dependencies=[Depends(get_current_active_user)] # Melindungi semua endpoint di router ini
)

@router.get("/", response_model=List[schemas.Kriteria])
def read_all_kriteria(db: Session = Depends(get_db)):
    """
    Endpoint untuk mendapatkan daftar semua kriteria yang tersedia dalam sistem.
    Hanya user yang sudah login dan aktif yang bisa mengakses.
    """
    kriteria_list = crud.get_all_kriteria(db)
    return kriteria_list
