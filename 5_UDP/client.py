import socket

def create_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return sock


def send_message(sock, message):
    data = message.encode()
    sock.sendto(data,("127.0.0.1", 9001)) #localhost


def receive_message(sock):
    data, addr = sock.recvfrom(4096)
    message = data.decode()

    return message


client = create_client()

message = input("Digite uma mensagem: ")

send_message(client, message)

response = receive_message(client)

print(f"Servidor respondeu {response}")
