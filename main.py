from datetime import datetime
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


#to provide parameters as in /blog?limit=X we simply pass param name as parameter to the function
# we can also define data type and default values inside. by default, it will think that those parameters are required and won't run the program withot them
#we can also set something to be completely optional
@app.get("/")
def index(limit=10, published: bool = True, sort: Optional[str]=None):
    if published:
        return {"data":f"{limit} published blogs from the list, sort={sort}"}
    else:
        return {"data":f"{limit} blogs from the list"}


### should come first before path with parameter, because it goes line by line
@app.get("/blog/unpublished")
def unpublished():
    return {"data": "All unpublished blogs"}


@app.get("/blog/{id}")
def about(id: int):
    return {"data": id}


@app.get("/blog/{id}/comments")
def comments(id):
    return {"data": {id: ["comment 1", "comment 2"]}}



class Blog(BaseModel):
    title: str
    description: str
    published: Optional[bool] = False
    #created_at: datetime
    


@app.post("/blog")
def create_blog(blog: Blog):
    return {"data":f"blog created with title as {blog.title}"}