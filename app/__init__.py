from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# Criando a instância do Flask
app = Flask(__name__)

# Configurações do banco de dados
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'aXU3sEdU'  # Chave secreta gerada
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'example.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializando o banco de dados e as migrações
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importando e registrando blueprints
from app.routes import bp as main_bp
app.register_blueprint(main_bp)

# Criando o banco de dados, se necessário
@app.before_first_request
def create_database():
    db.create_all()

# Importando os módulos de sua aplicação
from app import routes, models
