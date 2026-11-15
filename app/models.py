from app import db


# Modelo da tabela de Restaurantes
class Restaurante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    zona = db.Column(db.String(100), nullable=False)
    especialidade = db.Column(db.String(100), nullable=False)
    preco = db.Column(db.String(20), nullable=False)  # Barato, Médio, Caro
