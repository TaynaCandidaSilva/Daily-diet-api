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

    print(refeicao)

    db.session.add(nova_refeicao)
    db.session.commit()

    return refeicao


@app.route("/refeicao", methods=["GET"])
def refeicao():
    return refeicao


if __name__ == "__main__":
    app.run(debug=True)
