from pydantic import BaseModel,field_validator,model_validator,conint,constr

class UserProfile(BaseModel):
    name: str
    age: int = 20
    email: str

    #field validation
 
    
    @field_validator('age')
    def check_age(cls, value):
        if value < 18:
            raise ValueError('Age must be at least 18')
        return value


user = UserProfile(name="raju", age=40, email="abc@example.com")
print(user)

# with defaul value
user1 = UserProfile(name="raju", email="abc@example.com")
print(user1)


class User(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def passwords_match(cls, model):
        if model.password != model.confirm_password:
            raise ValueError("Passwords do not match")
        return model

User(password="a", confirm_password="a")


#nested model

from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str

class UserProfile(BaseModel):
    name: str
    age: int
    email: str
    address: Address

address = Address(street="10 surat", city="surat")
user = UserProfile(name="Ema", age=34, email="emma.@example.fr", address=address)
print(user)


#converting from json to python

from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: int
    email: str

data = '{"name": "mahes", "age": 28, "email": "mahesh@example.kr"}'
user = UserProfile.model_validate_json(data)
print(user)


#hndling null

from typing import Optional
from pydantic import BaseModel

class UserProfile(BaseModel):
    name: str
    age: Optional[int] = None
    email: str

user = UserProfile(name="jay", email="jay@example.se")
print(user)

#custom validation

from pydantic import BaseModel, conint, constr
from typing import List

PositiveInt = conint(gt=15)  

class Product(BaseModel):
    name: constr(min_length=1)  
    price: PositiveInt
    tags: List[str] = []

p = Product(name="Pen", price=10, tags=["stationery"])
print(p)