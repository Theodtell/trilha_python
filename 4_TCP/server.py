import socket
import threading

clients = []
lock = threading.Lock()

def create_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 9000))
    s.listen()
    print("Servidor iniciando...")
    return s



def wait_client(s):
    print("Aguardando cliente...")
    conn, addr = s.accept()
    print(f"Cliente conectado: {addr}")
    return conn, addr


def broadcast(sender, data):
    with lock:
        for c in clients:
            if c is not sender:
                try:
                    c.sendall(data)
                except OSError:
                    pass


def handle_client(conn, addr):
    with lock:
        clients.append(conn)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"[{addr}] {data.decode()}")
            broadcast(conn, data)
    finally:
        with lock:
            clients.remove(conn)
        conn.close()
        print(f"Cliente {addr} desconectado")
