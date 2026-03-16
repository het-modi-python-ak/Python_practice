from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn


app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

db = []



@app.post("/items/", response_model=Item, status_code=201)
def create_item(item: Item):
    for existing_item in db:
        if existing_item.id == item.id:
            raise HTTPException(status_code=400, detail="Item ID already exists")
    db.append(item)
    return item


@app.get("/items/", response_model=list[Item])
def read_items():
    return db


@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: int):
    for item in db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_update: Item):
    for index, item in enumerate(db):
        if item.id == item_id:
            db[index] = item_update
            return item_update
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/items/{item_id}", status_code=204)
def delete_item(item_id: int):
    for index, item in enumerate(db):
        if item.id == item_id:
            del db[index]
            return # No content for 204
    raise HTTPException(status_code=404, detail="Item not found")

# Entry point to run the application using uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
