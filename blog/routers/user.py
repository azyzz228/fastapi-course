
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
import schemas, database, models
from repository import user as userRepository

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post('/', response_model=schemas.showUser)
def createUser(request: schemas.User , db: Session=Depends(database.get_db)):
    return userRepository.create(request, db)

#SHOW USER
@router.get("/{id}", response_model=schemas.showUser)
def getUser(id:int, db: Session=Depends(database.get_db)):
  return userRepository.get_one(id, db)