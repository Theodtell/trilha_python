import json
import os.path


def carregar_usuarios():
    if os.path.exists("users.json"):

        with open("users.json", "r", encoding="utf-8") as arquivo:

            return  json.load(arquivo)

    return []


def salvar_usuarios(users):
    with open("users.json", "w", encoding="utf-8") as arquivo:
        json.dump(
            users,
            arquivo,
            ensure_ascii=False,
            indent=4
        )


users = carregar_usuarios()


def listar_usuarios():

    return users


def buscar_usuario(id_usuario):
    for usuario in users:
        if usuario["id"] == id_usuario:
            return usuario
    return None


def criar_usuario(nome, email):  #voltar e ver a possibilidade de quebrar quando a lista estiver vazia

    if not users:
        novo_id = 1
    else:
        novo_id = users[-1]["id"] + 1

    novo_usuario = {
        "id": novo_id,
        "name" : nome,
        "email" : email
    }

    users.append(novo_usuario)
    salvar_usuarios(users)
    return novo_usuario



def atualizar_usuario(id_usuario, novo_nome, novo_email):
    for usuario in users:
        if usuario["id"] == id_usuario:
            usuario["name"] = novo_nome
            usuario["email"] = novo_email

            salvar_usuarios(users)

            return usuario

    return None


def remover_usuario(id_usuario):
    for usuario in users:
        if usuario["id"] == id_usuario:
            users.remove(usuario)

            salvar_usuarios(users)

            return usuario

    return None

