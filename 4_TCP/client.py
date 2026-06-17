import socket
import threading

def receber(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                break
            print(f"\n[outro]: {data.decode()}")
        except OSError:
            break

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("127.0.0.1", 9000))
    nome = input("Digite seu nome: ")
    print("Conectado! Digite suas mensagens:")

    threading.Thread(target=receber, args=(sock,), daemon=True).start()

    while True:
        msg = input()
        if msg.lower() == "sair":
            break
        mensagem_formatada = f"{nome}: {msg}"
        sock.sendall(mensagem_formatada.encode())

    sock.close()

if __name__ == "__main__":
    main()