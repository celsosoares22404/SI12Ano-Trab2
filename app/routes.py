from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Restaurante


# Rota da Página Inicial
@app.route('/')
def index():
    return render_template('index.html')


# Rota de Locais a Visitar
@app.route('/locais')
def locais():
    return render_template('locais.html')


# Rota de Gastronomia Típica
@app.route('/gastronomia')
def gastronomia():
    lista_restaurantes = Restaurante.query.all()
    return render_template('gastronomia.html', restaurantes=lista_restaurantes)


# Rota para Gerir a Tabela de Restaurantes
@app.route('/restaurantes', methods=['GET', 'POST'])
def restaurantes():
    if request.method == 'POST':
        novo = Restaurante(
            nome=request.form['nome'],
            zona=request.form['zona'],
            especialidade=request.form['especialidade'],
            preco=request.form['preco']
        )
        db.session.add(novo)
        db.session.commit()
        return redirect(url_for('restaurantes'))

    lista_restaurantes = Restaurante.query.all()
    return render_template('restaurantes.html', restaurantes=lista_restaurantes)


# Rota para Apagar um Restaurante pelo ID
@app.route('/apagar_restaurante/<int:id>', methods=['POST'])
def apagar_restaurante(id):
    restaurante = Restaurante.query.get_or_404(id)
    db.session.delete(restaurante)
    db.session.commit()
    return redirect(url_for('restaurantes'))


# Rota para Editar um Restaurante pelo ID
@app.route('/editar_restaurante/<int:id>', methods=['GET', 'POST'])
def editar_restaurante(id):
    restaurante = Restaurante.query.get_or_404(id)
    if request.method == 'POST':
        restaurante.nome = request.form['nome']
        restaurante.zona = request.form['zona']
        restaurante.especialidade = request.form['especialidade']
        restaurante.preco = request.form['preco']
        db.session.commit()
        return redirect(url_for('restaurantes'))

    return render_template('editar_restaurante.html', restaurante=restaurante)
