from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "<h1>Hello World</h1>"}

@app.get("/nm")
async def root():
    
    return {"message": "sum is 100"}






@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}




# path match

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/users")
async def read_users2():
    return ["Bean", "Elfo"]


#path with enum

from enum import Enum



class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"





@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}