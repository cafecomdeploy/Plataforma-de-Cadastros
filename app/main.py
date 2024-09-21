from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.database.config import engine
from app.database import base
from app.controllers import user_controller, address_controller

app = FastAPI(default_response_class=JSONResponse)

# Cria as tabelas no banco de dados
base.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(user_controller.router, prefix="/users")
app.include_router(address_controller.router)