from fastapi import FastAPI
from db.database import create_supabase_client
from app.models import User
import bcrypt
from fastapi.middleware.cors import CORSMiddleware

supabase = create_supabase_client()
app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def user_exists(key: str = 'email_id', value: str = None):
     user = supabase.table('Users').select('*').eq(key,value).execute()
     return len(user.data)>0


@app.get("/")
def root():
     data,count = supabase.table('Users').select('username').execute()
     print(data)
     return data

@app.post('/user')
def create_user(user: User):
     try:
          user_email = user.email_id.lower()
          hashed_password= bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
          if user_exists(value=user_email):
               return {'message': 'User already exists'}
          data,count = supabase.table('Users').insert({'username':user.username,'password':str(hashed_password),'email_id':user.email_id}).execute()
          if data:
               return {'message':'user created'}
          else:
               return {'message':'user creation failed'}
     except:
          return {'message':'error'}