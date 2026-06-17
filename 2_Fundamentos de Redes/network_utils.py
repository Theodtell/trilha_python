import socket


def resolve_ip(host):
    return  socket.gethostbyname(host)




def test_ports(ip):


    for porta in (80, 443):


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET = IPv4 e SOCK_STREAM = TCP
        s.settimeout(2)


        try:
            s.connect((ip, porta))
            print (f"Porta {porta}: aberta")


        except OSError as erro:
            print (f"Porta {porta}: {erro}")


        finally:
            s.close()
