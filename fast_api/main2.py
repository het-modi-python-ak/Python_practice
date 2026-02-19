from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
async def fun1():
    return {"helo"}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]




@app.get("/users/me")
async def read_user_me(namr : str):
    return {"user_id": "the current user" , "name" : namr}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}




@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item



class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items1/")
async def create_item(item: Item):
    return item

