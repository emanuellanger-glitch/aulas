from flask import Flask, jsonify

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


# Exercício 1 – ex01_post.py
@app.route("/produtos", methods=["GET"])
def get_produtos():
    return jsonify(data)

@app.route("/produtos", methods=["POST"])
def post_produtos():
    new = request.get_json()
    data.append(new)
    return jsonify(new), 201


# Exercício 2 – ex02_post.py
@app.route("/produtos", methods=["POST"])
def post_produtos():
    new = request.get_json()
    if (new['preco'] == None) or (new['preco'] == 0):
        return {"erro": "O campo preco e obrigatorio"}, 400
    else:
        data.append(new)
        return jsonify(new), 201


# Exercício 3 – ex03_post.py
tarefas = []

@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    return jsonify(tarefas)

@app.route("/tarefas", methods=["POST"])
def post_produtos():
    new = request.get_json()
    if (new['titulo'] == None) or (new['titulo'] == ''):
        return {"erro": "O campo titúlo é obrigatorio"}, 400
    else:
        data.append(new)
        return jsonify(new), 201