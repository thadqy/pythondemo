from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI()

items = {'foo': 'The Foo Wrestlers'}

@app.get('/items/{item_id}')
async def get_item(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=404, detail='item_is is not found')
    return {'item': items['foo']}