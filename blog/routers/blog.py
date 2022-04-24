
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
import schemas, database, models

router = APIRouter(
    prefix='/blog',
    tags=['Blog']
)

# GET ALL BLOGS
@router.get("/", response_model=List[schemas.showBlog])
def all(db: Session=Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

# CREATE A BLOG
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session=Depends(database.get_db)):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# GET SINGLE BLOG
@router.get("/{id}", status_code=200, response_model=schemas.showBlog)
def show(id: int, db: Session=Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Blog {id} is not found in database")
        # res.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with {id} is not available"}
    return blog

# DELETE A BLOG
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session=Depends(database.get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "deleted"

#CHANGE EXISTING BLOG
@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED, tags=['Blog'])
def update(id: int, request: schemas.Blog ,db: Session=Depends(database.get_db)):
   
    blog = db.query(models.Blog).filter(models.Blog.id==id) 
    if not blog.first():
        # response.status_code=status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this id does not exist")
    
    blog.update(request.dict())
    db.commit()
    return "updated"
