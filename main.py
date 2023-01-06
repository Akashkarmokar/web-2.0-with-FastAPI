from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/blog')
def index(limit:int=10,is_published:bool=True, sort:Optional[str] = None):
    if is_published:
        return { 'data': f'{limit} blog from published blog'}
    return {'data': f'{50} blog from unpublished blog'}

@app.get('/blog/unpublished')
async def unpublished():
    # fetch unpublished blog
    return {'data': 'It is unpublished blog'}


@app.get('/blog/{id}')
async def show(id:int = 0):
    # fetch blog with id
    return { 'data': id }


@app.get('/blog/{blog_id}/comments')
async def comments(blog_id):
    # fetch comments of blog with id = id
    return { 'data': {'1','2'}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool] = False

@app.post('/blog')
async def create_blog(blog: Blog):
    # Create blog

    return {'data': f'Blog is created with title as{blog.title} and description is {blog.body}'}









