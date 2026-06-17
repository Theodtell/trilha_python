# UDP Client-Server

Projeto desenvolvido como atividade prática para estudo de Redes de Computadores utilizando Python e sockets UDP.

## Objetivo

Implementar uma comunicação simples entre cliente e servidor utilizando o protocolo UDP.

O cliente envia uma mensagem para o servidor e o servidor responde com uma confirmação (`ACK`).

---

## Conceitos Praticados

- Modelo Cliente-Servidor
- Endereçamento IP
- Portas
- Protocolo UDP
- Sockets em Python
- Codificação e decodificação de mensagens (`encode()` e `decode()`)
- Comunicação em rede sem conexão

---

## Estrutura do Projeto

```text
5_UDP/
│
├── main.py
├── server.py
└── client.py
```

### server.py

Responsável pelas operações do servidor:

- Criar o socket UDP
- Receber mensagens
- Enviar respostas

### client.py

Responsável pelas operações do cliente:

- Criar o socket UDP
- Enviar mensagens
- Receber respostas

### main.py

Responsável por iniciar e manter o servidor em execução.

---

## Funcionamento

Fluxo da comunicação:

```text
CLIENTE
    |
    | "Olá servidor"
    v
SERVIDOR
    |
    | "ACK"
    v
CLIENTE
```

---

## Como Executar

### 1. Iniciar o servidor

Abra um terminal na pasta do projeto e execute:

```bash
python main.py
```

Saída esperada:

```text
Servidor UDP iniciado na porta 9001
```

---

### 2. Executar o cliente

Abra um segundo terminal na mesma pasta e execute:

```bash
python client.py
```

Digite uma mensagem:

```text
Digite uma mensagem: Olá servidor
```

---

## Exemplo de Execução

### Servidor

```text
Servidor UDP iniciado na porta 9001
Cliente ('127.0.0.1', 54123) enviou: Olá servidor
```

### Cliente

```text
Digite uma mensagem: Olá servidor
Servidor respondeu: ACK
```

---

## Tecnologias Utilizadas

- Python 3
- Biblioteca Socket

---

## Aprendizados

Durante o desenvolvimento deste projeto foram praticados os seguintes conceitos:

- Criação de sockets UDP
- Associação de portas utilizando `bind()`
- Envio de dados com `sendto()`
- Recebimento de dados com `recvfrom()`
- Conversão entre texto e bytes
- Comunicação entre processos através da rede

