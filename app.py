from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    msg = os.getenv(
        "WELCOME_MSG",
        "Benvenuto nel portale SaaS"
    )

    client = os.getenv(
        "CLIENT_NAME",
        "cliente"
    )

    return f"""
    <html>
    <head>
    <title>{client}</title>
    <style>
    body {{
        font-family: Arial;
        text-align:center;
        margin-top:100px;
    }}
    </style>
    </head>

    <body>
    <h1>{msg}</h1>
    <p>Portale digitale {client} - GitHub-Prova finale!!!!</p>
    </body>

    </html>
    """

app.run(host="0.0.0.0", port=5000)
