from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import Union

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


