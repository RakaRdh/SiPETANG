from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt

# Perubahan: Impor absolut dari root direktori proyek
import schemas
import crud
import models
from database import get_db
from config import settings

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_active_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)) -> models.User:
    """
    Dependency untuk mendapatkan user yang sedang login dan aktif dari token JWT.
    Semua endpoint yang butuh login harus 'Depends' pada fungsi ini.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Tidak dapat memvalidasi kredensial",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = crud.get_user_by_email(db, email=email)
    if user is None:
        raise credentials_exception
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Pengguna tidak aktif")
    return user

@router.get("/me", response_model=schemas.User)
def get_own_profile(current_user: models.User = Depends(get_current_active_user)):
    """Endpoint untuk mendapatkan detail profil diri sendiri."""
    return current_user

@router.post("/deactivate", response_model=schemas.User)
def deactivate_account(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_active_user)):
    """Endpoint untuk menonaktifkan akun sendiri."""
    return crud.set_user_active_status(db, user_id=current_user.id_user, is_active=False)
