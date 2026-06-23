from flask import Flask
from datetime import date

app = Flask(__name__)

# EXERCICIO 1 - ex01_api.py
@app.route("/1")
def exercicio_1():
    return "<p>Meu nome completo: Emanuel Garcia Langer</p>"

# EXERCICIO 2 - ex02_api.py
@app.route("/")
def inicio():
    return "Bem-vindo"

@app.route("/curso")
def curso():
    return "Desenvolvimento de Sistema"

@app.route("/escola")
def escola():
    return "CEEP - Centro Educacional Estadual Pedro Boareto Neto"

# EXERCICIO 3 - ex03_api.py
@app.route("/saudacao")
def saudacao():
    return "Saudação passageiro. Seja bem-vindo!"

@app.route("/data")
def saudacao():
    return f"Data atual: {date.today()}"
