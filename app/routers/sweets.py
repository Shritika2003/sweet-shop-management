from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas import SweetCreate
from app.models import Sweet
from app.deps import get_db, get_current_user

router = APIRouter(
    prefix="/api/sweets",
    tags=["Sweets"]
)

@router.post("/")
def add_sweet(
    sweet: SweetCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    new_sweet = Sweet(**sweet.dict())
    db.add(new_sweet)
    db.commit()
    db.refresh(new_sweet)
    return new_sweet


@router.get("/")
def list_sweets(db: Session = Depends(get_db)):
    return db.query(Sweet).all()
