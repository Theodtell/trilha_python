from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from starlette.websockets import WebSocket

from backend.services.user_service import (
listar_usuarios,
buscar_usuario,
criar_usuario,
atualizar_usuario,
remover_usuario
)
from backend.models.schemas import (
UserUpdate,
UserCreate
)
from backend.services.email_service import (
enviar_email_confirmacao,
enviar_email_remocao
)

app = FastAPI()


# Permite que o frontend acesse a API localmente
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API Funcionando!"}


@app.get("/users")
def get_users():
    return listar_usuarios()


@app.get("/users/{id_usuario}")
def get_user(id_usuario: int):

    usuario = buscar_usuario(id_usuario)

    if usuario is None:
        return {"erro" : "Usuário não encontrado"}

    return usuario


@app.post("/users")
def post_user(user : UserCreate):
    novo_usuario = criar_usuario(
        user.name,
        user.email
    )
    enviar_email_confirmacao(
        user.name,
        user.email
    )
    return novo_usuario


@app.put("/users/{id_usuario}")
def put_user(
        id_usuario:int,
             user: UserUpdate
):
    if id_usuario is None:
        return {"erro" : "Usuário não encontrado"}

    return atualizar_usuario(
        id_usuario,
        user.name,
        user.email
    )


@app.delete("/users/{id_usuario}")
def delete_user(id_usuario: int):

    usuario = remover_usuario(id_usuario)

    print(usuario)

    if usuario is not None:

        print("Enviando email de remoção...")

        enviar_email_remocao(
            usuario["name"],
            usuario["email"]
        )

    return usuario


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    while True:

        mensagem = await websocket.receive_text()

        print(f"Recebido: {mensagem}")

        await websocket.send_text(
            f"Servidor recebeu: {mensagem}"
        )