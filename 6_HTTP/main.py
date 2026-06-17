from fastapi import FastAPI
from users import (
listar_usuarios,
buscar_usuario,
criar_usuario,
atualizar_usuario,
remover_usuario)
from schemas import (
UserUpdate,
UserCreate
)

app = FastAPI()

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
    return criar_usuario(user.name)


@app.put("/users/{id_usuario}")
def put_user(
        id_usuario:int,
             user: UserUpdate
):
    if id_usuario is None:
        return {"erro" : "Usuário não encontrado"}

    return atualizar_usuario(id_usuario, user.name)


@app.delete("/users/{id_usuario}")
def delete_user(id_usuario:int):
    return remover_usuario(id_usuario)