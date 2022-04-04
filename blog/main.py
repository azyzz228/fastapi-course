from fastapi import FastAPI, Depends, status, Response, HTTPException
import schemas, models, database
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blogs")
def all(db: Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}", status_code=200)
def show(id: int, res: Response ,db: Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Blog {id} is not found in database")
        # res.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail": f"Blog with {id} is not available"}
    return blog

@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session=Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "deleted"


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, response: Response, request: schemas.Blog ,db: Session=Depends(get_db)):
    print(request)
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    
    if not blog.first():
        # response.status_code=status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this id does not exist")
    blog.update(request.dict())
    db.commit()
    return "updated"