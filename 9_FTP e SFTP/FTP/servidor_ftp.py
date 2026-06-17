from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import os

#garantia de que a pasta de arquivos existe
if not os.path.exists("arquivos_ftp"):
    os.makedirs("arquivos_ftp")

#1. autorizador - define usuários e as parmissões

autorizador = DummyAuthorizer()
autorizador.add_user(
    "theo",
    "senha123",
    "arquivos_ftp",
    perm="elradfmwMT"        # permissões (leitura, escrita, delete, etc.). e = CWD, l = LIST, r = RETR, a = enviar arquivos em modo append, d = deletar, f = renomear, m = MKD, w = STOR, M/T = permissões avançadas
)


#2. Handler - define o comportamento do FTP

handler = FTPHandler
handler.authorizer = autorizador

#3. Servidor - define onde ele vai escutar

servidor = FTPServer(("127.0.0.1", 21),handler)

print("Server FTP rodando em 127.0.0.1:21")
print("Usuário: theo | Senha: senha123")

servidor.serve_forever()
