from flask import Flask, jsonify

# Exercício 1 – ex01_json.py
@app.route("/produto")
def exercicio_1():
    data = {
        "id": 1,
        "nome": "Shampoo",
        "preco": 23.50,
        "disponivel": True
    }
    return jsonify(data)


# LISTA DE PRODUTOS PARA EX.1 E 3
data = [
    {
        "id": 1,
        "nome": "Shampoo",
        "preco": 23.50,
        "disponivel": True
    },
    {
        "id": 2,
        "nome": "Sabonete",
        "preco": 3.50,
        "disponivel": True
    },
    {
        "id": 3,
        "nome": "Desodorante",
        "preco": 12.00,
        "disponivel": True
    },
    {
        "id": 4,
        "nome": "Creme",
        "preco": 24.50,
        "disponivel": False
    }        
]

# Exercício 2 – ex02_json.py
@app.route("/produtos")
def exercicio_2():
    return jsonify(data)

# Exercício 3 – ex03_json.py
@app.route("/produtos/<int:id>")
def exercicio_3(id):

    for product in data:
        if id == product["id"]:
            return f"{product.nome}"
    
    return {"erro": "Produto nao encontrado"}, 404

# Exercício 4 – Desafio – ex04_json.py
@app.route("/produtos/disponiveis")
def exercicio_4():

    produtos_disponiveis = []
    produtos_indisponiveis = []

    for product in data:
        if product["disponivel"] == True:
            produtos_disponiveis.append(product) 
        else:
            produtos_indisponiveis.append(product)

    return jsonify(produtos_disponiveis)
