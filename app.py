
from flask import Flask, request
from config.database import cursor, connecting

app = Flask(__name__)


@app.route("/", methods=['GET'])
def read_all():
    sql = "SELECT * FROM cadastro;"
    cursor.execute(sql)
    cadastro = cursor.fetchall()
    return cadastro


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


@app.route("/delete/<id>", methods=['DELETE'])
def delete(id):
    sql = "DELETE FROM cadastro WHERE id = %s"
    cursor.execute(sql, (id))
    connecting.commit()
    return {"mesage": "Usuário deletado com sucesso"}


@app.route("/update/<id>", methods=["PUT"])
def update(id):
    body = request.json
    email = body.get("email")
    senha = body.get("senha")
    sql = "UPDATE cadastro SET email = %s, senha = %s WHERE id = %s"
    try:
        cursor.execute(sql, (email, senha, id))
        connecting.commit()
        return {"message": "Dados atualizados com sucesso"}

    except:
        return {"message": "Falha ao atualizar os dados"}
