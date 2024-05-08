from typing import Union
from fastapi import FastAPI


app = FastAPI()

@app.get('/')
def index():
    return "<h1>Hello World! </h1>"

@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str: None] = None):
    return {'item_id': item_id, 'q': q}

