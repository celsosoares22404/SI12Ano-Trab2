import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Cria a instância da aplicação Flask
app = Flask(__name__)

# Configuração da Base de Dados SQLite
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
RAIZ_PROJETO = os.path.dirname(BASE_DIR)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(RAIZ_PROJETO, 'database.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializa a extensão da Base de Dados
db = SQLAlchemy(app)

# IMPORTANTE: Importar os modelos e as rotas depois de criar app e db
# Isto evita importações circulares e regista as rotas no Flask
from app import models, routes
