from fastapi import FastAPI, status, Response
from data_base_config import database
app = FastAPI()


@app.get('/blog')
async def get_all_blogs():
    return {'data': "All blogs is fetched successfully"}


@app.post('/blog', status_code=status.HTTP_201_CREATED)
async def create_blog(response: Response):
    _blog = {
        'blog_id': 12,
        'title': 'It is my custom blog title',
        'description': 'Description is under construction'
    }
    print(_blog)
    created_blog = await database.get_collection('blog').insert_one(_blog)
    print(created_blog)
    print(response)
    response.status_code = status.HTTP_200_OK
    return {'data': "Your blog is created successfully"}