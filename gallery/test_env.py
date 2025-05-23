# test_env.py
import os
from dotenv import load_dotenv

load_dotenv()
print("SECRET_KEY:", os.getenv('SECRET_KEY'))
print("DEBUG:", os.getenv('DEBUG'))