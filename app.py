from flask import Flask, jsonify, request
from repository.database import db
from db_model.refeicao import Refeicao

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SECRET_KEY"] = "SECRET_KEY_DIETA"

db.init_app(app)


@app.route("/refeicao", methods=["POST"])
def nova_refeicao():
    refeicao = request.json
    nova_refeicao = Refeicao(**refeicao)

    db.session.add(nova_refeicao)
    db.session.commit()

    return jsonify({"message": "Refeição criada com sucesso"})


@app.route("/refeicao/<int:id>", methods=["GET"])
def refeicao_id(id):
    refeicao = Refeicao.query.filter_by(id=id).first()
    if refeicao:
        return jsonify(refeicao.to_dict()), 200
    return jsonify({"message": "Refeicao nao encontrada"}), 404


@app.route("/refeicao/<id>", methods={"PUT"})
def editar_refeicao(id):
    refeicao = Refeicao.query.filter_by(id=id).first()

    if refeicao:
        refeicao.nome = request.json.get("nome", refeicao.nome)
        refeicao.descricao = request.json.get("descricao", refeicao.descricao)
        refeicao.data_hora = request.json.get("data_hora", refeicao.data_hora)
        refeicao.dentro_dieta = request.json.get("dentro_dieta", refeicao.dentro_dieta)

        db.session.add(refeicao)
        db.session.commit()

        return jsonify({"message": f"Refeição {id} editada com sucesso"}), 200

    return jsonify({"message": "Refeição nao encontrada"}), 404


@app.route("/refeicao/<id>", methods=["DELETE"])
def deletar_refeicao(id):

    refeicao = Refeicao.query.filter_by(id=id).first()

    if refeicao:
        db.session.delete(refeicao)
        db.session.commit()

        return jsonify({"message": f"Refeicao {id} deletada com sucesso"}), 200

    return jsonify({"message": "Refeicao nao encontrada"}), 404


@app.route("/refeicao/<nome>", methods=["GET"])
def todas_refeicoes_usuario(nome):
    refeicoes = Refeicao.query.filter_by(nome=nome).all()
    lista_refeicoes = []
    for refeicao in refeicoes:
        lista_refeicoes.append(refeicao.to_dict())

        return jsonify({f"refeicoes de {nome}": lista_refeicoes}), 200

    return jsonify({"message": f"Nenhuma refeicao encontrada para {nome}"}), 404


if __name__ == "__main__":
    app.run(debug=True)
