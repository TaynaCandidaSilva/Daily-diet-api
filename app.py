from flask import Flask

app = Flask(__name__)


@app.route("/refeicao", methods=["GET"])
def refeicao():
    return "refeicao"


if __name__ == "__main__":
    app.run(debug=True)
