from flask import Flask
from database import db
from models import Tarefa

app = Flask(__name__)

# Configurações do Banco de Dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

# Cria as tabelas 
with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return "API do Gerenciador de Tarefas rodando!"

if __name__ == '__main__':
    app.run(debug=True)