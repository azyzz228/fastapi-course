from sqlalchemy.orm import Session
from models import Blog
import schemas
from fastapi import status, HTTPException

def get_all(db: Session):
    blogs = db.query(Blog).all()
    return blogs



def get_one(id:int, db:Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Blog {id} is not found in database")
        # res.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with {id} is not available"}
    return blog



def create(request: schemas.Blog, db: Session):
    new_blog = Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog



def destroy(id: int, db: Session):
    db.query(Blog).filter(Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "deleted"



def update(id:int, request: schemas.Blog, db: Session):
    blog = db.query(Blog).filter(Blog.id==id) 
    if not blog.first():
        # response.status_code=status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this id does not exist")
    blog.update(request.dict())
    db.commit()
    return "updated"