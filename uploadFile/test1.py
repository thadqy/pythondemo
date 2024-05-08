from typing import Union
from fastapi import FastAPI
import uvicorn
from enum import Enum


app = FastAPI()

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resent = 'resent'
    lenet = 'lenet'


fake_items_db = [{'item_name': 'Foo'}, {'item_name': 'Bar'}, {'item_name': 'Baz'}]

@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]

@app.get('/models/{model_name}')
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep learning FTW!'}
    elif model_name.value() == 'alexnet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}
    else:
        return {'model_name': model_name, 'message': 'Have some residuals'}

@app.get('/user/{user_id}')
async def get_user_info(user_id: int):
    return {'user_id': user_id}

@app.get('/user/me')
async def get_curr_info():
    return {'user_id': 'count'}

@app.get('/')
def index():
    return {'hello':'world'}

# @app.get('/items/{item_id}')
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {'item_id': item_id, 'q': q}


@app.get('/test/{item_id}')
async def get_test1(item_id: str, q: Union[str, None] = None, short: bool = False):
    item = {'item_id': item_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


