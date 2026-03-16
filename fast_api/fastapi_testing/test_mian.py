from fastapi.testclient import TestClient 
from main import app, db 

client = TestClient(app) 



def test_get_items(): 
    response = client.get("/items/")
    assert response.status_code == 200 
    assert response.json() ==[]

def test_create_read_item():
    response = client.post("/items",json={
  "id": 1,
  "name": "string",
  "description": "string",
  "price": 0,
  "tax": 0
})
    assert response.status_code == 201
    # assert response.json == {"helo"}

def test_get_items_id():
    response = client.get("/items/1")
    assert response.status_code==200



