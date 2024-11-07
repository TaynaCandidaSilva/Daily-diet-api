from repository.database import db


class Refeicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(200))

    def to_dict(self):
        return {"id": self.id, "nome": self.nome, "descricao": self.descricao}
