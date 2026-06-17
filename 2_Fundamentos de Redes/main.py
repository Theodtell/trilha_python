from network_utils import resolve_ip, test_ports
from ping_utils import teste_ping


def main():
    host = input("digite o domínio: ")
    ip = resolve_ip(host)
    print(ip)


    test_ports(ip)


if __name__ == "__main__":
    main()
