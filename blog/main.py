from fastapi import FastAPI
import models, database
from routers import blog, user, auth

app = FastAPI()
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(auth.router)

models.Base.metadata.create_all(database.engine)

get_db = database.get_db


# def get_db():
#     db = database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# @app.post("/blog", status_code=status.HTTP_201_CREATED, tags=['Blog'])
# def create(request: schemas.Blog, db: Session=Depends(get_db)):
#     new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# GET ALL BLOGS
# @app.get("/blogs", response_model=List[schemas.showBlog], tags=['Blog'])
# def all(db: Session=Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs



# @app.get("/blog/{id}", status_code=200, response_model=schemas.showBlog, tags=['Blog'])
# def show(id: int, res: Response ,db: Session=Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Blog {id} is not found in database")
#         # res.status_code = status.HTTP_404_NOT_FOUND
#         # return {"detail": f"Blog with {id} is not available"}
#     return blog



# @app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=['Blog'])
# def destroy(id: int, db: Session=Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
#     db.commit()
#     return "deleted"


# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=['Blog'])
# def update(id: int, response: Response, request: schemas.Blog ,db: Session=Depends(get_db)):
#     print(request)
#     blog = db.query(models.Blog).filter(models.Blog.id==id)
    
#     if not blog.first():
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this id does not exist")
#     blog.update(request.dict())
#     db.commit()
#     return "updated"



# @app.post('/user', response_model=schemas.showUser, tags=['users'])
# def createUser(request: schemas.User , db: Session=Depends(get_db)):
 
#     new_user = models.User(username= request.username, email=request.email, password = Hash.bcrypt(request.password))

#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)

#     return new_user

# #SHOW USER
# @app.get("/user/{id}", response_model=schemas.showUser, tags=['users'])
# def getUser(id:int, db: Session=Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog with this id does not exist")
#     return user