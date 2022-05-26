from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import schemas, database, models
from hashing import Hash
from token_generator import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(tags=["Authentication"])

@router.post("/login")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=404, detail="User with this username is not found")
    
    # if user.password != Hash.bcrypt(request.password):
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=404, detail="Wrong password")

    access_token = create_access_token(
        data={"sub": user.username}
    )
    
    return {"access_token": access_token, "token_type": "bearer"}