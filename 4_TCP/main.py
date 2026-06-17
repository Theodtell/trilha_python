import threading
from server import create_server, wait_client, handle_client

def main():
    server = create_server()

    while True:
        conn, addr = wait_client(server)
        # em vez de tratar aqui, cria uma thread pra esse cliente
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()