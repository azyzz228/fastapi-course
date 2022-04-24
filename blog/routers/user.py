
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
import schemas, database, models
from hashing import Hash

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post('/', response_model=schemas.showUser)
def createUser(request: schemas.User , db: Session=Depends(database.get_db)):
 
    new_user = models.User(username= request.username, email=request.email, password = Hash.bcrypt(request.password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

#SHOW USER
@router.get("/{id}", response_model=schemas.showUser)
def getUser(id:int, db: Session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this id does not exist")
    return user