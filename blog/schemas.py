
from click import password_option
from pydantic import BaseModel



class Blog(BaseModel):
    title:str
    body: str

# Response model -- we can define what we can show by the response
class showBlog(BaseModel):
    title: str
    body: str
    class Config():
        orm_mode= True

class User(BaseModel):
    username: str
    email : str
    password : str

class showUser(BaseModel):
    username: str
    email: str
    class Config():
        orm_mode= True

