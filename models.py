from database import db

class Tarefa(db.Model):
    __tablename__ = 'tarefas'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    concluida = db.Column(db.Boolean, default=False)

    def to_dict(self):
        """Método auxiliar para converter o objeto em dicionário (fácil conversão para JSON)."""
        return {
            'id': self.id,
            'titulo': self.titulo,
            'descricao': self.descricao,
            'concluida': self.concluida
        }