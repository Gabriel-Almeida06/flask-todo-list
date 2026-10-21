from flask import Flask, request, jsonify
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

#metodo GET
@app.route('/tarefas',methods=['GET'])
def listar_tarefas():
    tarefas = Tarefa.query.all()
    return jsonify([tarefa.to_dict() for tarefa in tarefas]), 200 


# metodo POST
@app.route('/tarefas',methods=['POST'])
def criar_tarefas():
    dados = request.get_json()
    if not dados or 'titulo' not in dados:
        return jsonify({'erro': 'o titulo é obrigatório'}), 400

    nova_tarefa = Tarefa(
        titulo=dados['titulo'],
        descricao=dados.get('descricao', '')
    )

    db.session.add(nova_tarefa)
    db.session.commit()

    return jsonify(nova_tarefa.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001)