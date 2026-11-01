from flask import render_template
from app import app, db


# Rota da Página Inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota de Locais a Visitar
@app.route('/locais')
def locais():
    # Exemplo com dados da BD:
    # lista_locais = Local.query.all()
    # return render_template('locais.html', locais=lista_locais)
    return render_template('locais.html')

# Rota de Gastronomia Típica
@app.route('/gastronomia')
def gastronomia():
    # Exemplo com dados da BD:
    # lista_pratos = Prato.query.all()
    # return render_template('gastronomia.html', pratos=lista_pratos)
    return render_template('gastronomia.html')
