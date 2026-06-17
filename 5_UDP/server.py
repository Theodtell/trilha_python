import socket

def create_server(): #criação e conf do serv
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #cria socket UDP
    sock.bind(("0.0.0.0", 9001))
    return sock


def receive_message(sock):
    data, addr = sock.recvfrom(4096) #mensagem recebida e quem enviou
    message = data.decode() #bytes --> texto
    return message, addr

def send_message(sock,message,addr):
    data = message.encode() # texto --> bytes
    sock.sendto(data, addr) #enviar para
