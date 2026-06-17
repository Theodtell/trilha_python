``md
# 🚀 TheoAPI

Uma aplicação full-stack para gerenciamento de usuários, composta por um **backend em FastAPI** e um **frontend em HTML, CSS e JavaScript**, com integração de envio de e-mails utilizando a **Brevo API (SMTP)** e persistência de dados em JSON.

---

## 📌 Funcionalidades

- ✅ Criar usuários
- ✅ Listar usuários
- ✅ Buscar usuário por ID
- ✅ Atualizar nome e e-mail do usuário
- ✅ Remover usuários
- ✅ Persistir dados em arquivo JSON
- ✅ Enviar e-mail de confirmação ao cadastrar usuário
- ✅ Enviar e-mail ao remover usuário
- ✅ Validar e-mails com Pydantic
- ✅ Interface web responsiva
- ✅ Integração entre frontend e backend via API REST

---

## 🛠️ Tecnologias Utilizadas

### Backend

- Python 3
- FastAPI
- Uvicorn
- Pydantic
- Requests
- Python Dotenv
- Brevo API
- JSON

### Frontend

- HTML5
- CSS3
- JavaScript (Vanilla JS)
- Font Awesome

---

## 📂 Estrutura do Projeto

```text
8_SMTP/
│
├── main.py              # Rotas da API
├── users.py             # Lógica de negócio e persistência
├── schemas.py           # Schemas do Pydantic
├── email_service.py     # Integração com Brevo
├── users.json           # Persistência dos usuários
├── .env                 # Variáveis de ambiente
│
├── frontend/
│   ├── index.html       # Interface principal
│   ├── style.css        # Estilos da aplicação
│   └── app.js           # Integração com a API
│
├── .gitignore
└── README.md
```

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone <url-do-repositorio>
cd 8_SMTP
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual:

### Windows

```bash
.venv\Scripts\activate
```

### Linux/Mac

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install fastapi uvicorn requests python-dotenv email-validator
```

---

## 🔐 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
BREVO_API_KEY=sua_api_key
SENDER_EMAIL=seu_email
SENDER_NAME=Sistema de cadastro
```

---

## ▶️ Executando o Backend

Na raiz do projeto execute:

```bash
uvicorn main:app --reload
```

Acesse a documentação Swagger:

```text
http://127.0.0.1:8000/docs
```

---

## 🌐 Executando o Frontend

Abra o arquivo:

```text
frontend/index.html
```

Ou utilize uma extensão como **Live Server** no VS Code ou IntelliJ.

---

## 📡 Endpoints

### Listar usuários

```http
GET /users
```

### Buscar usuário por ID

```http
GET /users/{id_usuario}
```

### Criar usuário

```http
POST /users
```

Exemplo de body:

```json
{
    "name": "Theo",
    "email": "email@email.com"
}
```

### Atualizar usuário

```http
PUT /users/{id_usuario}
```

Exemplo de body:

```json
{
    "name": "Novo Nome",
    "email": "novo@email.com"
}
```

### Remover usuário

```http
DELETE /users/{id_usuario}
```

---

## ✉️ Envio de E-mails

A API envia e-mails automaticamente utilizando a **Brevo API**:

- 📧 E-mail de boas-vindas ao cadastrar um usuário
- 📧 E-mail de confirmação ao remover um usuário

---

## 💾 Persistência de Dados

Os usuários são armazenados no arquivo:

```text
users.json
```

Isso permite que os dados permaneçam salvos mesmo após reiniciar a aplicação.

---

## 🔒 Segurança

- Uso de variáveis de ambiente com `.env`
- API Key protegida
- Validação de e-mails com Pydantic
- Proteção básica contra XSS no frontend
- Configuração de CORS para comunicação frontend-backend

---

## 📚 Conceitos Aplicados

- API REST
- CRUD
- FastAPI
- SMTP
- Integração com APIs externas
- Variáveis de ambiente
- Persistência em JSON
- Modularização
- Validação de dados
- Requisições HTTP
- CORS
- Frontend integrado à API

---

## 👨‍💻 Autor

Desenvolvido por **Theo Tell** como parte dos estudos de Back-end, Redes e desenvolvimento de APIs.
````
