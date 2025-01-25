# import libs
import sqlite3
import hashlib
from fastapi import *
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


# app settings
app = FastAPI()

origins = [
    "http://localhost:5173",  # React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allowed
    allow_credentials=True,  # cookie 
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # HTTP methods
    allow_headers=["X-Requested-With", "Content-Type"],  # allowed headers
)

# functions
def cntDB(): 
    con = sqlite3.connect(".db")
    con.row_factory = sqlite3.Row
    return con

def signinHashingPassword(user_name: str, user_pw: str):
    cnt = cntDB()
    cur = cnt.cursor()
    try: 
        cur.execute("SELECT id FROM users WHERE name == ?", (user_name, ))
        user_id = cur.fetchall()[0]['id']
    except: return "err404" 

    print(user_id)
    
    cnt.close()
    
    user_pw += user_id # aading salt
    print(user_pw)
    
    sha256_hash = hashlib.sha256()    
    sha256_hash.update(user_pw.encode('utf-8'))
    print(sha256_hash)
    
    return sha256_hash.hexdigest()

# models
class signin_model(BaseModel):
    name : str
    pw : str


# api 
## get
@app.get("/")
async def index(): # root
    print(signinHashingPassword("adain", "!password1234"))
    return JSONResponse({"msg" : "Hello, World!"})

## post
@app.post("/signin/")
async def signin(signin : signin_model):
    user_name = signin.name
    user_pw = signin.pw
    
    real_pw = signinHashingPassword(user_name, user_pw) # hash pw
    if real_pw == "err404" : return { "login_status" : 404 }; print("wrong name") # if name is wrong
    elif user_pw == real_pw : return { "login_status" : 200 }; print("wrong pw") # if pw is wrong
    else : return { "login_status" : 404 }