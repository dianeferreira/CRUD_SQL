
from flask import Flask, request
from config.database import cursor, connecting

app = Flask(__name__)


@app.route("/cadastro", methods=['POST'])
def create():
    body = request.json
    nome = body.get('nome')
    sobrenome = body.get('sobrenome')
    sexo = body.get('sexo')
    data_nascimento = body.get('data_nascimento')
    email = body.get('email')
    senha = body.get('senha')
    sql = "INSERT INTO cadastro (nome, sobrenome, sexo, data_nascimento, email, senha) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (nome, sobrenome,  sexo,
                   data_nascimento, email, senha))
    connecting.commit()
    return {"message": "Cadastro efetuado com sucesso"}
