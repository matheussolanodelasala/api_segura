from fastapi import FastAPI, HTTPException, Depends
from sqlmodel import SQLModel, Session, select
from contextlib import asynccontextmanager

from database import engine
from models import User, LoginData
from security import create_secure_hash, validate

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    yield

app = FastAPI(lifespan=lifespan)

def get_db():
    with Session(engine) as session:
        yield session

@app.post("/register")
def save(data: LoginData, db: Session = Depends(get_db)):
    found = db.exec(select(User).where(User.username == data.username)).first()
    
    if found:
        raise HTTPException(status_code=400, detail="Nombre ocupado")

    new_user = User(
        username=data.username,
        hashed_password=create_secure_hash(data.password)
    )

    db.add(new_user)
    db.commit()
    return {"result": "Usuario guardado exitosamente"}

@app.post("/login")
def access(data: LoginData, db: Session = Depends(get_db)):
    user = db.exec(select(User).where(User.username == data.username)).first()

    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    if not validate(data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Acceso denegado")

    return {"result": "Bienvenido al sistema"}