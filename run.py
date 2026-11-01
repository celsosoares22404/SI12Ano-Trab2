from app import app, db

# Cria as tabelas na base de dados SQLite se ainda não existirem
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Inicia o servidor local de desenvolvimento
    app.run(debug=True, port=5000)
