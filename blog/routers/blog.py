
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
import schemas, database, models
from repository import blog

from fastapi.security import OAuth2PasswordBearer
from . import oauth2

router = APIRouter(
    prefix='/blog',
    tags=['Blog']
)

# GET ALL BLOGS
@router.get("/", response_model=List[schemas.showBlog])
def all(db: Session=Depends(database.get_db), get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

# CREATE A BLOG
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session=Depends(database.get_db)):
    return blog.create(request=request, db=db)

# GET SINGLE BLOG
@router.get("/{id}", status_code=200, response_model=schemas.showBlog)
def show(id: int, db: Session=Depends(database.get_db)):
    return blog.get_one(id, db)

# DELETE A BLOG
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session=Depends(database.get_db)):
    return blog.destroy(id, db)

#CHANGE EXISTING BLOG
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, tags=['Blog'])
def update(id: int, request: schemas.Blog ,db: Session=Depends(database.get_db)):
    return blog.update(id, request, db)
