from fastapi import FastAPI, Query
from pydantic import BaseModel
import uvicorn
from typing import Union, List

app = FastAPI()

@app.get("/test")
async def get_test():
    return 'this is a test demo'

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

@app.post('/items/')
async def query_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict

@app.get('/test/test1')
async def read_items(q: Union[str, None] = Query(default=None, max_length=2)):
    return q

@app.get('/test/test2')
async def test2(q: Union[List[str], None] = None):
    item = {'q': q}
    return item
   
