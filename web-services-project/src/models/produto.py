from src.models.user import db
from datetime import datetime
from enum import Enum

class StatusProduto(Enum):
    ATIVO = "ATIVO"
    INATIVO = "INATIVO"
    DESCONTINUADO = "DESCONTINUADO"

class Categoria(db.Model):
    __tablename__ = 'categorias'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False, unique=True)
    descricao = db.Column(db.Text)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relacionamento com produtos
    produtos = db.relationship('Produto', backref='categoria_ref', lazy=True)
    
    def __repr__(self):
        return f'<Categoria {self.nome}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'data_criacao': self.data_criacao.isoformat() if self.data_criacao else None
        }

class Produto(db.Model):
    __tablename__ = 'produtos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.Text)
    preco = db.Column(db.Numeric(10, 2), nullable=False)
    estoque = db.Column(db.Integer, default=0)
    status = db.Column(db.Enum(StatusProduto), default=StatusProduto.ATIVO)
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)
    data_atualizacao = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<Produto {self.nome}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': float(self.preco) if self.preco else None,
            'estoque': self.estoque,
            'status': self.status.value if self.status else None,
            'categoria_id': self.categoria_id,
            'categoria': self.categoria_ref.nome if self.categoria_ref else None,
            'data_criacao': self.data_criacao.isoformat() if self.data_criacao else None,
            'data_atualizacao': self.data_atualizacao.isoformat() if self.data_atualizacao else None
        }

