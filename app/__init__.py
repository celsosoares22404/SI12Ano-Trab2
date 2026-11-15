import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Usa uma base PostgreSQL alojada em produção e SQLite em desenvolvimento local.
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
RAIZ_PROJETO = os.path.dirname(BASE_DIR)
database_url = os.environ.get('DATABASE_URL')

if database_url:
    if database_url.startswith('postgres://'):
        database_url = database_url.replace('postgres://', 'postgresql+psycopg://', 1)
    elif database_url.startswith('postgresql://'):
        database_url = database_url.replace('postgresql://', 'postgresql+psycopg://', 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
elif os.environ.get('VERCEL'):
    raise RuntimeError('DATABASE_URL tem de estar definida nas variáveis de ambiente do Vercel.')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(RAIZ_PROJETO, 'database.db')}"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa a extensão da Base de Dados
db = SQLAlchemy(app)

# IMPORTANTE: Importar os modelos e as rotas depois de criar app e db
# Isto evita importações circulares e regista as rotas no Flask
from app import models, routes
