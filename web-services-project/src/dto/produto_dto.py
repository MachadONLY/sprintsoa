from dataclasses import dataclass
from typing import Optional
from decimal import Decimal

@dataclass
class CriarCategoriaDTO:
    nome: str
    descricao: Optional[str] = None
    
    def validar(self):
        erros = []
        
        if not self.nome or len(self.nome.strip()) == 0:
            erros.append("Nome da categoria é obrigatório")
        
        if len(self.nome) > 100:
            erros.append("Nome da categoria deve ter no máximo 100 caracteres")
            
        return erros

@dataclass
class AtualizarCategoriaDTO:
    nome: Optional[str] = None
    descricao: Optional[str] = None
    
    def validar(self):
        erros = []
        
        if self.nome is not None and len(self.nome.strip()) == 0:
            erros.append("Nome da categoria não pode ser vazio")
        
        if self.nome and len(self.nome) > 100:
            erros.append("Nome da categoria deve ter no máximo 100 caracteres")
            
        return erros

@dataclass
class CriarProdutoDTO:
    nome: str
    preco: float
    categoria_id: int
    descricao: Optional[str] = None
    estoque: Optional[int] = 0
    
    def validar(self):
        erros = []
        
        if not self.nome or len(self.nome.strip()) == 0:
            erros.append("Nome do produto é obrigatório")
        
        if len(self.nome) > 200:
            erros.append("Nome do produto deve ter no máximo 200 caracteres")
        
        if self.preco is None or self.preco < 0:
            erros.append("Preço deve ser um valor positivo")
        
        if self.categoria_id is None or self.categoria_id <= 0:
            erros.append("Categoria é obrigatória")
        
        if self.estoque is not None and self.estoque < 0:
            erros.append("Estoque não pode ser negativo")
            
        return erros

@dataclass
class AtualizarProdutoDTO:
    nome: Optional[str] = None
    descricao: Optional[str] = None
    preco: Optional[float] = None
    estoque: Optional[int] = None
    categoria_id: Optional[int] = None
    status: Optional[str] = None
    
    def validar(self):
        erros = []
        
        if self.nome is not None and len(self.nome.strip()) == 0:
            erros.append("Nome do produto não pode ser vazio")
        
        if self.nome and len(self.nome) > 200:
            erros.append("Nome do produto deve ter no máximo 200 caracteres")
        
        if self.preco is not None and self.preco < 0:
            erros.append("Preço deve ser um valor positivo")
        
        if self.categoria_id is not None and self.categoria_id <= 0:
            erros.append("ID da categoria deve ser válido")
        
        if self.estoque is not None and self.estoque < 0:
            erros.append("Estoque não pode ser negativo")
        
        if self.status and self.status not in ['ATIVO', 'INATIVO', 'DESCONTINUADO']:
            erros.append("Status deve ser ATIVO, INATIVO ou DESCONTINUADO")
            
        return erros

