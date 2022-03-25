import imp
from fastapi import FastAPI
from . import schemas, models, database

app = FastAPI()

models.Base.metadata.create_all(database.engine)


@app.post("/blog")
def create(request: schemas.Blog):
    return {"data": f"passed title {request.title} with body--{request.body}"}