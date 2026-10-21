Task Manager API (Flask & SQLAlchemy)

Uma API RESTful simples e eficiente para gestão de tarefas (To-Do List), desenvolvida em Python com a utilização da framework Flask e SQLAlchemy para persistência de dados num banco SQLite.

Este projeto foi construído seguindo boas práticas de arquitetura modular, organização de código e controlo de versões com Git (utilizando o padrão de feature branches).
🚀 Funcionalidades

    Listar Tarefas (GET /tarefas): Obtém todas as tarefas registadas na base de dados.

    Criar Tarefa (POST /tarefas): Regista uma nova tarefa (campo titulo obrigatório).

    Atualizar Tarefa (PUT /tarefas/<id>): Modifica o título, a descrição ou o estado de conclusão de uma tarefa existente.

    Remover Tarefa (DELETE /tarefas/<id>): Elimina uma tarefa da base de dados através do seu ID.

 Tecnologias Utilizadas

    Python 3

    Flask: Framework web para construção da API REST.

    Flask-SQLAlchemy: ORM para abstração e gestão da base de dados.

    SQLite: Banco de dados relacional em ficheiro.

    Git & GitHub: Controlo de versões e alojamento do código.

    Postman: Ferramenta para testes de endpoints HTTP.

Estrutura do Projeto
Plaintext

projeto-api-github/
├── instance/
│   └── todo.db          # Ficheiro do banco de dados SQLite (gerado automaticamente)
├── app.py               # Rotas da aplicação e inicialização do servidor
├── database.py          # Instância centralizada do SQLAlchemy
├── models.py            # Definição do modelo de dados (Tabela Tarefa)
├── .gitignore           # Ficheiros ignorados pelo Git (ex: .venv, __pycache__)
└── README.md            # Documentação do projeto

🔧 Como Executar o Projeto
Pré-requisitos

    Python 3.x instalado.

    Git instalado.

Passo a Passo

    Clonar o repositório:
    Bash

    git clone https://github.com/O-TEU-UTILIZADOR/O-TEU-REPOSITORIO.git
    cd O-TEU-REPOSITORIO

    Criar e ativar o ambiente virtual (.venv):
    Bash

    # No Linux / macOS:
    python3 -m venv .venv
    source .venv/bin/activate

    # No Windows:
    python -m venv .venv
    .venv\Scripts\activate

    Instalar as dependências:
    Bash

    pip install flask flask-sqlalchemy

    Executar a aplicação:
    Bash

    python app.py

    A API ficará disponível em: [http://127.0.0.1:5001/](http://127.0.0.1:5001/)

Documentação dos Endpoints
1. Listar todas as tarefas

    Método: GET

    URL: /tarefas

    Resposta (200 OK):
    JSON

    [
      {
        "id": 1,
        "titulo": "Estudar Flask",
        "descricao": "Praticar rotas e SQLAlchemy",
        "concluida": false
      }
    ]

2. Criar uma nova tarefa

    Método: POST

    URL: /tarefas

    Corpo da Requisição (JSON):
    JSON

    {
      "titulo": "Comprar leite",
      "descricao": "Marca desnatada"
    }

    Resposta (201 Created):
    JSON

    {
      "id": 2,
      "titulo": "Comprar leite",
      "descricao": "Marca desnatada",
      "concluida": false
    }

3. Atualizar uma tarefa

    Método: PUT

    URL: /tarefas/<id>

    Corpo da Requisição (JSON):
    JSON

    {
      "concluida": true
    }

    Resposta (200 OK):
    JSON

    {
      "id": 2,
      "titulo": "Comprar leite",
      "descricao": "Marca desnatada",
      "concluida": true
    }

4. Remover uma tarefa

    Método: DELETE

    URL: /tarefas/<id>

    Resposta (200 OK):
    JSON

    {
      "mensagem": "Tarefa 2 deletada com sucesso!"
    }
