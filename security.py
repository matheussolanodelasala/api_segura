import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

SERVER_SECRET = os.getenv("PEPPER", "CLAVE_DEFAULT_CAMBIAME")

def mix(password: str):
    return (password + SERVER_SECRET).encode()

def create_secure_hash(password: str):
    return bcrypt.hashpw(
        mix(password), 
        bcrypt.gensalt(rounds=13)
    ).decode()

def validate(password: str, stored_hash: str):
    return bcrypt.checkpw(
        mix(password), 
        stored_hash.encode()
    )