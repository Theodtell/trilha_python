users = [
    {"id": 1, "name": "Theo"},
    {"id": 2, "name": "Maria"}
]

def listar_usuarios():

    return users


def buscar_usuario(id_usuario):
    for usuario in users:
        if usuario["id"] == id_usuario:
            return usuario
    return None


def criar_usuario(nome):  #voltar e ver a possibilidade de quebrar quando a lista estiver vazia
    if not users:
        novo_id = 1
    else:
        novo_id = users[-1]["id"] + 1
        novo_usuario = {
            "id": novo_id,
            "name" : nome
        }
        users.append(novo_usuario)
        return novo_usuario



def atualizar_usuario(id_usuario, novo_nome):
    for usuario in users:
        if usuario["id"] == id_usuario:
            usuario["name"] = novo_nome

            return usuario

    return None


def remover_usuario(id_usuario):
    for usuario in users:
        if usuario["id"] == id_usuario:
            users.remove(usuario)

            return usuario

    return None

