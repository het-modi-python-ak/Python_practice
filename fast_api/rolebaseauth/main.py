from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from pydantic import BaseModel

app = FastAPI()

# Secret Key
SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
print(oauth2_scheme)

#admin class
class Admin(BaseModel):
    username :str
    password:str
    role:str = "admin"


# In-memory users
users_db = {
    "admin": {
        "username": "admin",
        "password": pwd_context.hash("admin123"),
        "role": "admin"
    },
    "het": {
        "username": "het",
        "password": pwd_context.hash("user123"),
        "role": "user"
    }
}



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str):
    user = users_db.get(username)

    if not user:
        return None

    if not verify_password(password, user["password"]):
        return None

    return user


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        username: str = payload.get("sub")
        role: str = payload.get("role")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = users_db.get(username)

        return user

    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


def require_role(required_role: str):

    def role_checker(user: dict = Depends(get_current_user)):

        if user["role"] != required_role:
            raise HTTPException(status_code=403, detail="Access Forbidden")

        return user

    return role_checker

#register admin
@app.post("/register/admin")
def register_user(admin: Admin):
    hashed_password = pwd_context.hash(admin.password)
    users_db[admin.username] = {
        "username": admin.username,
        "password": hashed_password,
        "role":"admin"
    }
    return admin


@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):

    user = authenticate_user(form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        {"sub": user["username"], "role": user["role"]}
    )

    return {"access_token": access_token, "token_type": "bearer"}



@app.get("/profile")
def user_profile(user: dict = Depends(get_current_user)):
    return {"message": f"Hello {user['username']}", "role": user["role"]}


@app.get("/admin")
def admin_dashboard(user: dict = Depends(require_role("admin"))):
    return {"message": "Welcome Admin","access token " : oauth2_scheme}


@app.get("/user")
def user_dashboard(user: dict = Depends(require_role("user"))):
    return {"message": "Welcome User" }


