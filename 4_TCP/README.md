# 💬 Chat TCP — Atividade Prática de Redes

Atividade prática desenvolvida durante a trilha de estudos de redes.
Implementação de um chat em tempo real utilizando o protocolo TCP, com suporte a múltiplos clientes simultâneos.

---

## 📋 Requisitos da Atividade

- [x] Servidor TCP
- [x] Múltiplos clientes
- [x] Broadcast de mensagens

---

## 🗂️ Estrutura do Projeto

```
4_TCP/
├── main.py      # Inicializa o servidor e gerencia as conexões
├── server.py    # Lógica do servidor (broadcast, handle de clientes)
└── client.py    # Cliente do chat
```

---

## ▶️ Como Rodar

### Pré-requisitos
- Python 3.x instalado

### Passo a passo

Abra **3 terminais** e navegue até a pasta do projeto em cada um:

```bash
cd "C:local do arquivo"
```

**Terminal 1 — Inicia o servidor:**
```bash
python main.py
```

**Terminal 2 e 3 — Inicia os clientes:**
```bash
python client.py
```

Ao conectar, cada cliente digita seu nome. As mensagens enviadas por um cliente aparecem para todos os outros conectados.  
Digite `sair` para encerrar a conexão.

---

## 🧠 Explicação do Código

### `main.py`
Responsável por iniciar o servidor e aguardar conexões em loop. A cada novo cliente conectado, cria uma **thread dedicada** para tratá-lo, permitindo que múltiplos clientes sejam atendidos simultaneamente.

```python
while True:
    conn, addr = wait_client(server)
    threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
```

### `server.py`
Contém a lógica principal do servidor:

- **`clients`** — lista com todas as conexões ativas
- **`lock`** — controla o acesso simultâneo à lista de clientes, evitando conflitos entre threads
- **`broadcast`** — envia a mensagem recebida para todos os clientes, exceto o remetente
- **`handle_client`** — loop de cada cliente: recebe mensagens e chama o broadcast

```python
def broadcast(sender, data):
    with lock:
        for c in clients:
            if c is not sender:
                c.sendall(data)
```

### `client.py`
O cliente utiliza **duas threads** para funcionar corretamente:

- **Thread de recebimento** — fica em loop aguardando mensagens do servidor
- **Thread principal** — lê o teclado e envia mensagens

Isso é necessário pois `recv()` é uma operação bloqueante — sem threads, o cliente travaria esperando mensagens e não conseguiria enviar nada ao mesmo tempo.

---

## 📚 O Que Aprendi

- **Protocolo TCP** — comunicação orientada à conexão, confiável e ordenada
- **Sockets em Python** — como criar, conectar, enviar e receber dados via `socket`
- **Operações bloqueantes** — entendi por que `recv()` trava o programa e como contornar isso
- **Threads** — como executar múltiplas tarefas em paralelo com `threading.Thread`
- **Lock** — como proteger recursos compartilhados (a lista de clientes) do acesso simultâneo entre threads
- **Broadcast** — padrão de distribuição de mensagens para múltiplos destinatários
- **Arquitetura cliente-servidor** — separação de responsabilidades entre quem serve e quem consome

---
