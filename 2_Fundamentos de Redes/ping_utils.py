import subprocess


def teste_ping (host):


    subprocess.run(["ping","-n", "3", host])
