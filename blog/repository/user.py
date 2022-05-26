from msilib import schema
from sqlalchemy.orm import Session
from models import User
import schemas
from fastapi import status, HTTPException
from hashing import Hash

def create(request: schemas.User, db: Session):
    new_user = User(username= request.username, email=request.email, password = Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_one(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this id does not exist")
    return user