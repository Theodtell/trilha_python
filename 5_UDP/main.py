from server import (
    create_server,
    receive_message,
    send_message
)

def main():

    server = create_server()

    print("Servidor UDP iniciado na porta 9001")

    while True:

        message, addr = receive_message(server)

        print(f"Cliente {addr} enviou: {message}")

        send_message(
            server,
            "ACK",
            addr
        )


if __name__ == "__main__":
    main()