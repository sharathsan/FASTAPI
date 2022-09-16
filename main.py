from turtle import title
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    published: bool = True
    rating: int = None

@app.get("/")
async def root():
    return{"message": "Awesome!!!"}

@app.get("/hosts")
def get_posts():
    return {"data":"your post has been liked"}

@app.post("/createposts")
def create_posts(new_post:Post):
    print(new_post)
    print(new_post.dict())
    return{"data":"new_post"}







