from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

# Perubahan: Impor absolut dari root direktori proyek
import crud
import schemas
from database import get_db
from routers.users import get_current_active_user # Impor dari dalam package routers

router = APIRouter(
    prefix="/alternatif",
    tags=["Alternatif"],
    dependencies=[Depends(get_current_active_user)] # Melindungi semua endpoint di router ini
)

@router.get("/", response_model=List[schemas.Alternatif])
def read_all_alternatif(db: Session = Depends(get_db)):
    """
    Endpoint untuk mendapatkan daftar semua alternatif tempat magang.
    Hanya user yang sudah login dan aktif yang bisa mengakses.
    """
    alternatif_list = crud.get_all_alternatif(db)
    return alternatif_list
