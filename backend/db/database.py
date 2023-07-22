from supabase import Client, create_client
from dotenv import load_dotenv
import os

load_dotenv('.env')

url:str = os.getenv('SUPABASE_URL')
key:str = os.getenv('SUPABASE_KEY')

def create_supabase_client():
    supabase: Client = create_client(url,key)
    return supabase