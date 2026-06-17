# API REST de Usuários

Projeto desenvolvido para praticar conceitos de HTTP, APIs REST, FastAPI e manipulação de dados em memória.

## Funcionalidades

A API permite:

- Listar todos os usuários
- Buscar um usuário por ID
- Criar novos usuários
- Atualizar usuários existentes
- Remover usuários

---

# Estrutura do Projeto

```
6_HTTP/
│
├── main.py
├── users.py
├── schemas.py
```

### main.py

Responsável por:

- Criar a aplicação FastAPI
- Definir as rotas da API
- Receber requisições HTTP
- Retornar respostas para o cliente

### users.py

Responsável por:

- Armazenar os usuários
- Implementar as regras de negócio
- Manipular os dados da aplicação

### schemas.py

Responsável por:

- Definir os modelos de dados da API
- Validar os dados recebidos nas requisições
- Especificar a estrutura esperada dos JSONs
- Garantir que os tipos dos dados estejam corretos

---

# Como Executar

## 1. Instalar dependências

```bash
pip install fastapi uvicorn
```

## 2. Iniciar o servidor

```bash
uvicorn main:app --reload
```

### Explicação

```text
main -> arquivo main.py
app  -> objeto FastAPI criado no arquivo
--reload -> reinicia automaticamente ao salvar alterações
```

Após iniciar o servidor, será exibida uma mensagem semelhante a:

```text
Uvicorn running on http://127.0.0.1:8000
```

---

# Documentação Automática

Acesse:

```text
http://127.0.0.1:8000/docs
```

O FastAPI gera automaticamente uma interface Swagger para testar todas as rotas da API.

---

# Rotas Disponíveis

## GET /

Verifica se a API está funcionando.

### Resposta

```json
{
  "message": "API Funcionando!"
}
```

---

## GET /users

Retorna todos os usuários cadastrados.

### Exemplo de resposta

```json
[
  {
    "id": 1,
    "name": "Theo"
  },
  {
    "id": 2,
    "name": "Maria"
  }
]
```

---

## GET /users/{id_usuario}

Busca um usuário específico pelo ID.

### Exemplo

```http
GET /users/1
```

### Resposta

```json
{
  "id": 1,
  "name": "Theo"
}
```

---

## POST /users

Cria um novo usuário.

### Body

```json
{
  "name": "João"
}
```

### Resposta

```json
{
  "id": 3,
  "name": "João"
}
```

---

## PUT /users/{id_usuario}

Atualiza o nome de um usuário.

### Exemplo

```http
PUT /users/1
```

### Body

```json
{
  "name": "Theo Silva"
}
```

### Resposta

```json
{
  "id": 1,
  "name": "Theo Silva"
}
```

---

## DELETE /users/{id_usuario}

Remove um usuário da lista.

### Exemplo

```http
DELETE /users/1
```

### Resposta

```json
{
  "id": 1,
  "name": "Theo"
}
```

---

# Conceitos Praticados

- HTTP
- API REST
- FastAPI
- JSON
- CRUD
- Rotas
- Path Parameters
- Pydantic
- Validação de dados
- Listas
- Dicionários
- Funções
- Modularização
