from pydantic import BaseModel
from typing import List


class BlogBase(BaseModel):
    title:str
    body: str

class Blog(BlogBase):
    class Config():
        orm_mode= True

# Response model -- we can define what we can show by the response


class User(BaseModel):
    username: str
    email : str
    password : str

class showUser(BaseModel):
    username: str
    email: str
    blogs: List[Blog] = []
    class Config():
        orm_mode= True

class showBlog(BaseModel):
    title: str
    body: str
    creator: showUser
    class Config():
        orm_mode= True