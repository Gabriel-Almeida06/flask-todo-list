# 📝 Task Manager (API Flask + Streamlit Frontend)



Uma aplicação Full Stack completa para gestão de tarefas (*To-Do List*), desenvolvida em Python. O projeto conta com uma **API RESTful** construída com **Flask** e **SQLAlchemy** (banco de dados SQLite) e uma interface web moderna e interativa criada com **Streamlit**.



---



## 🎨 Interface da Aplicação



<img width="1798" height="959" alt="Captura de tela de 2026-10-20 23-49-43" src="https://github.com/user-attachments/assets/d047609f-bbf9-4713-b94f-8136377532f2" />




---



## 🚀 Funcionalidades



- **Listar Tarefas (`GET`)**: Exibe todas as tarefas cadastradas no banco de dados SQLite com seus respectivos status (Pendente / Concluída).

- **Criar Tarefa (`POST`)**: Adiciona novas tarefas através de um formulário com campos de título (obrigatório) e descrição.

- **Atualizar Status (`PUT`)**: Alterna rapidamente o estado da tarefa entre concluída e pendente com um clique.

- **Remover Tarefa (`DELETE`)**: Exclui permanentemente tarefas do banco de dados.



---



## 🛠️ Tecnologias Utilizadas



### Backend (API RESTful)

- **Python 3**

- **Flask**: Framework para estruturação das rotas HTTP.

- **Flask-SQLAlchemy**: ORM para abstração e persistência na base de dados.

- **SQLite**: Banco de dados relacional em arquivo local (`todo.db`).



### Frontend (Interface Web)

- **Streamlit**: Framework Python para construção de interfaces web reativas sem necessidade de HTML/CSS/JS.

- **Requests**: Biblioteca para consumo e comunicação de dados HTTP entre a interface e a API Flask.



### Versionamento & Ferramentas

- **Git & GitHub**: Versionamento estruturado em *feature branches*.

- **Postman**: Validação dos endpoints HTTP.



---



## 📂 Estrutura do Projeto



```text

projeto-api-github/

├── instance/

│   └── todo.db          # Banco de dados SQLite (gerado automaticamente)

├── app.py               # Servidor Backend (API Flask)

├── frontend.py          # Interface Web (Streamlit)

├── database.py          # Instância centralizada do SQLAlchemy

├── models.py            # Modelo de dados da tabela Tarefa

├── .gitignore           # Arquivos ignorados pelo Git (.venv, __pycache__, *.db)

├── README.md            # Documentação do projeto

└── Captura de tela de 2026-10-20 23-49-43.png  # Imagem da interface

```



---



## 🔧 Como Executar o Projeto



### Pré-requisitos

- Python 3.x instalado.

- Git instalado.



### 1. Clonar o repositório e preparar o ambiente

```bash

git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git

cd SEU-REPOSITORIO



# Criar e ativar o ambiente virtual (.venv)

python3 -m venv .venv

source .venv/bin/activate  # No Windows: .venv\Scripts\activate



# Instalar dependências

pip install flask flask-sqlalchemy streamlit requests

```



### 2. Executar a Aplicação (2 Terminais)



Para rodar o sistema completo, é necessário manter a API (Backend) e a Interface (Frontend) executando simultaneamente em terminais separados:



* **Terminal 1 — Backend (API Flask):**

  ```bash

  python app.py

  ```

  *A API estará ativa em: `http://127.0.0.1:5001/`*



* **Terminal 2 — Frontend (Streamlit):**

  ```bash

  source .venv/bin/activate

  streamlit run frontend.py

  ```

  *A interface abrirá automaticamente no navegador em: `http://localhost:8501`*



---



## 📌 Documentação da API (Endpoints REST)



| Método | Endpoint | Descrição |

| :--- | :--- | :--- |

| `GET` | `/tarefas` | Retorna a lista de todas as tarefas em formato JSON. |

| `POST` | `/tarefas` | Cria uma nova tarefa. Requer JSON: `{"titulo": "..."}`. |

| `PUT` | `/tarefas/<id>` | Atualiza dados/status da tarefa pelo ID. |

| `DELETE` | `/tarefas/<id>` | Remove a tarefa do banco de dados pelo ID. |



---



## ✒️ Autor



Desenvolvido por **Gabriel** durante a construção prática de uma aplicação Full Stack em Python.
