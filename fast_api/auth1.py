from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/")
def hello():   #no verification 
    return {"this is not verified "}

@app.get("/use")
async def hi(token:Annotated[str,Depends(oauth2_scheme)]):
    return {"messgae" : "hello "}  

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}



@app.post("/token")
async def login(form_data:OAuth2PasswordRequestForm=Depends()):
    username = form_data.username
    password = form_data.password


    if username=="het" and password =="12345":
        return{ "token_type":"bearer"}
    return{"error":"invalid credential"}


