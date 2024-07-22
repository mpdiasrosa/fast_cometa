from http import HTTPStatus
from fastapi import FastAPI
from fast_zero.schemas import Message, UserSchema, UserPublic


from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}

@app.post('/user/', response_model=UserPublic)
def create_user(user: UserSchema):
    return user