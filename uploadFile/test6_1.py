from pydantic import BaseModel



class User(BaseModel):
    userName: str
    age: int
    email: str | None = None

class UserInfo(User):
    password: str
