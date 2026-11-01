# Guia Passo a Passo: Projeto Web com Flask e Base de Dados

Este guia documenta o projeto transformado em **Flask**, com uma arquitetura modular onde o backend fica organizado numa pasta `app/` com o respetivo `__init__.py`:
- **Pasta `app/` com `__init__.py`**: Configuração central do Flask e da base de dados SQLAlchemy.
- **Ficheiro único de modelos (`app/models.py`)**: Contém as classes e tabelas da base de dados.
- **Ficheiro único de rotas (`app/routes.py`)**: Contém todas as rotas da aplicação (@app.route).
- **Sem Blueprints**: Rotas e navegação simples e diretas com `url_for('nome_funcao')`.
- **Ficheiro de arranque leve (`run.py`)**: Localizado na raiz do projeto.

---

## 1. Estrutura do Projeto

```text
projeto/
│
├── run.py                          # Ponto de entrada do servidor
├── requirements.txt                # Dependências (Flask, Flask-SQLAlchemy)
├── .gitignore                      # Ficheiros ignorados pelo Git
├── GUIA_PASSO_A_PASSO_FLASK.md     # Este guia
│
└── app/                            # Backend e ficheiros da aplicação
    ├── __init__.py                 # Inicializa a app Flask e a base de dados
    ├── models.py                   # Ficheiro ÚNICO com os modelos/tabelas da BD
    ├── routes.py                   # Ficheiro ÚNICO com as rotas (@app.route)
    │
    ├── static/                     # Folhas de estilo CSS
    │   ├── style.css
    │   ├── locais.css
    │   └── gastronomia.css
    │
    └── templates/                  # Templates HTML interpretados pelo Jinja2
        ├── index.html
        ├── locais.html
        └── gastronomia.html
```

---

## 2. Instalação e Preparação do Ambiente

No terminal (PowerShell) dentro da pasta do projeto:

1. **Criar o ambiente virtual (opcional, mas recomendado):**
   ```powershell
   python -m venv venv
   ```

2. **Ativar o ambiente virtual no Windows:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   *(Se o Windows bloquear a execução de scripts no PowerShell, corre antes: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned`)*.

3. **Instalar as dependências:**
   ```powershell
   pip install -r requirements.txt
   ```

---

## 3. Explicação dos Ficheiros

### `run.py` (Raiz)
Ponto de entrada que importa `app` e `db` do pacote `app`:
```python
from app import app, db

# Cria as tabelas na base de dados se ainda não existirem
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### `app/__init__.py`
Ficheiro que define o pacote `app`:
- Instancia o `Flask(__name__)`.
- Define a base de dados SQLite (`database.db`) na raiz do projeto.
- Inicializa a extensão `db = SQLAlchemy(app)`.
- No final, importa `from app import models, routes` para registar os modelos e as rotas sem causar conflitos ou dependências circulares.

### `app/models.py`
Ficheiro único com os modelos da base de dados:
- **`Local`**: Tabela de monumentos e pontos de interesse (nome, descrição, imagem_url, wiki_url).
- **`Prato`**: Tabela de gastronomia (nome, descrição, tipo_ambiente, preco).

### `app/routes.py`
Ficheiro único com todas as rotas da aplicação:
- `@app.route('/')` -> Renderiza `index.html`.
- `@app.route('/locais')` -> Renderiza `locais.html`.
- `@app.route('/gastronomia')` -> Renderiza `gastronomia.html`.

### `app/templates/` e `app/static/`
- O Flask reconhece automaticamente `app/templates/` para as páginas HTML e `app/static/` para os ficheiros estáticos (CSS, imagens).
- No HTML, o CSS é referenciado através de:
  ```html
  <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
  ```
- E as hiperligações de navegação usam:
  ```html
  <a href="{{ url_for('index') }}">Início</a>
  <a href="{{ url_for('locais') }}">Locais a Visitar</a>
  <a href="{{ url_for('gastronomia') }}">Gastronomia Típica</a>
  ```

---

## 4. Como Iniciar a Aplicação

Para colocar o servidor a correr:

```powershell
python run.py
```

Depois, acede no teu navegador a:
**[http://127.0.0.1:5000](http://127.0.0.1:5000)**

*(O ficheiro `database.db` será gerado automaticamente na raiz assim que o servidor arrancar).*

---

## 5. Como Inserir e Manipular Dados na Base de Dados

Para experimentar a base de dados via terminal do Python:

```powershell
python
```

Dentro da consola interativa do Python:
```python
from app import app, db
from app.models import Local

with app.app_context():
    novo_local = Local(
        nome="Torre de Belém",
        descricao="Monumento do séc. XVI na foz do Rio Tejo.",
        imagem_url="https://thumb.wikimedia.org/wikipedia/commons/thumb/f/fa/Bel%C3%A9m_Tower_in_Lisbon%2C_Portugal.jpg/330px-Bel%C3%A9m_Tower_in_Lisbon%2C_Portugal.jpg",
        wiki_url="https://pt.wikipedia.org/wiki/Torre_de_Bel%C3%A9m"
    )
    db.session.add(novo_local)
    db.session.commit()
    print("Guardado com sucesso!")

exit()
```

E para listar esses dados dinamicamente no `app/routes.py`:
```python
@app.route('/locais')
def locais():
    lista = Local.query.all()
    return render_template('locais.html', locais=lista)
```

No template HTML (`app/templates/locais.html`), podes percorrê-los com o ciclo do Jinja2:
```html
{% for local in locais %}
    <h3>{{ local.nome }}</h3>
    <p>{{ local.descricao }}</p>
{% endfor %}
```
