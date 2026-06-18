from dotenv import load_dotenv
import os
import requests

load_dotenv()

API_KEY = os.getenv("BREVO_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_NAME = os.getenv("SENDER_NAME")
URL = "https://api.brevo.com/v3/smtp/email"
HEADERS = {
    "accept": "application/json",
    "api-key": API_KEY,
    "content-type": "application/json"
}

def enviar_email_confirmacao(name, email):

    body = {
        "sender": {
            "name" : SENDER_NAME,
            "email" : SENDER_EMAIL
        },
        "to": [
            {
                "email" : email
            }
        ],
        "subject" : "cadastro realizado com sucesso!",
        "htmlContent": f"""
        <h1>Seja bem-vindo(a) {name}!</h1>

        <p>Seu cadastro foi realizado com sucesso.</p>

        <p>Você está oficialmente cadastrado(a) na TheoAPI!!</p>
        """
    }

    response = requests.post(
        URL,
        headers=HEADERS,
        json=body
    )

    resposta_email(response)


def enviar_email_remocao(name, email):
    
    body = {
        "sender": {
            "name" : SENDER_NAME,
            "email" : SENDER_EMAIL
        },
        "to": [
            {
                "email": email
            }
        ],
        "subject": "Cadastro removido",
        "htmlContent": f"""
            <h1>Cadastro removido com sucesso!</h1>

            <p>Olá {name} seu cadastro foi removido do TheoAPI</p>
            """
    }

    response = requests.post(
        URL,
        headers=HEADERS,
        json=body
    )

    resposta_email(response)


def resposta_email(response):

    if response.status_code == 201:
        print("Email enviado com sucesso!")
    else:
        print("Erro ao enviar e-mail: ")
        print(response.status_code)
        print(response.text)
