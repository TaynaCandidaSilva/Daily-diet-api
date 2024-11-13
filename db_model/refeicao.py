from repository.database import db


class Refeicao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(200))
    data_hora = db.Column(db.String(20))
    dentro_dieta = db.Column(db.Boolean)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "descricao": self.descricao,
            "data_hora": self.data_hora,
            "dentro_dieta": self.dentro_dieta,
        }
