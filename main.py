from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class SingleBlog(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None



@app.get('/')
def index():
    return {'data': {'name': 'John'}}


@app.get('/blog')
def blogs():
    return {
        'data': [
            'blog_one',
            'blog_two'
        ]
    }


@app.get('/blog/{blog_id}')
def blog_by_blog_id(blog_id: int):
    return blog_id


@app.get('/query-param')
def query_param(limit:int = 0, published:bool = True, sort: str | None = None):
    print(limit, published, sort)
    return {'data': 'Ok'}


@app.post('/blog')
def create_single_blog(req_body: SingleBlog):
    return req_body

