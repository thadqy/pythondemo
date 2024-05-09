from fastapi import Cookie, FastAPI, HTTPException, Depends, Header
import uvicorn
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated, Union
from pydantic import BaseModel
from test6_1 import User, UserInfo


# async def check_token(token: Annotated[Union[str, None], Header()] = None):
#     if not token:
#         raise HTTPException(status_code=400, detail='token not is null')



# app = FastAPI(dependencies=[Depends(check_token)])

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@app.get('/test/oauth')
async def test_oauth(token: Annotated[str, Depends(oauth2_scheme)]):
    return {'toekn': token}





def fake_decode_token(token):
    return UserInfo(
        userName = token + 'fakeDecodeToken',
        age = 1,
        email = 'ss',
        password= '111'
    )

def get_curr_user(token: str = Depends(oauth2_scheme)):
    try:
        user = fake_decode_token(token)
    except Exception as e:
        e.__traceback__
    return user

@app.get('/user/me1', response_model=User)
async def get_user(current_user: User = Depends(get_curr_user)):
    return current_user

if __name__ == '__main__':
    uvicorn.run(app='test6:app', host='127.0.0.1', port=8000, reload=True)



