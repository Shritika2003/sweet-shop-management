from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.models import Sweet
from app.deps import get_db, get_current_user

router = APIRouter(
    prefix="/api/sweets",
    tags=["Inventory"]
)

@router.post("/{sweet_id}/purchase")
def purchase_sweet(
    sweet_id: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()

    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    if sweet.quantity <= 0:
        raise HTTPException(status_code=400, detail="Out of stock")

    sweet.quantity -= 1
    db.commit()

    return {"message": "Sweet purchased successfully"}


@router.post("/{sweet_id}/restock")
def restock_sweet(
    sweet_id: int,
    quantity: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)
):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()

    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    sweet.quantity += quantity
    db.commit()

    return {"message": "Sweet restocked successfully"}
