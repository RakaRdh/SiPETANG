from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import crud, schemas
from database import get_db
from routers.users import get_current_active_user

router = APIRouter(
    prefix="/riwayat",
    tags=["Riwayat"],
    dependencies=[Depends(get_current_active_user)]
)

@router.get("/", response_model=List[schemas.Riwayat])
def read_user_riwayat(
    db: Session = Depends(get_db),
    current_user: schemas.User = Depends(get_current_active_user)
):
    """
    Endpoint untuk mengambil riwayat perhitungan dari user yang sedang login.
    """
    return crud.get_riwayat_by_user_id(db, user_id=current_user.id_user)
