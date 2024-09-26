from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.database.config import engine
from app.database import base
from app.controllers import user_controller, address_controller
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(default_response_class=JSONResponse)

# Configurando o middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # ou ["*"] para aceitar qualquer origem
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)
# Cria as tabelas no banco de dados
base.Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(user_controller.router, prefix="/users")
app.include_router(address_controller.router)