from src.models.produto import Produto, Categoria, StatusProduto, db
from src.dto.produto_dto import CriarProdutoDTO, AtualizarProdutoDTO, CriarCategoriaDTO, AtualizarCategoriaDTO
from typing import List, Optional

class ProdutoService:
    
    @staticmethod
    def listar_produtos(categoria_id: Optional[int] = None, status: Optional[str] = None) -> List[Produto]:
        """Lista produtos com filtros opcionais"""
        query = Produto.query
        
        if categoria_id:
            query = query.filter(Produto.categoria_id == categoria_id)
        
        if status:
            try:
                status_enum = StatusProduto(status)
                query = query.filter(Produto.status == status_enum)
            except ValueError:
                pass  # Status inválido, ignora o filtro
        
        return query.all()
    
    @staticmethod
    def obter_produto_por_id(produto_id: int) -> Optional[Produto]:
        """Obtém um produto pelo ID"""
        return Produto.query.get(produto_id)
    
    @staticmethod
    def criar_produto(dto: CriarProdutoDTO) -> Produto:
        """Cria um novo produto"""
        # Verifica se a categoria existe
        categoria = Categoria.query.get(dto.categoria_id)
        if not categoria:
            raise ValueError("Categoria não encontrada")
        
        produto = Produto(
            nome=dto.nome,
            descricao=dto.descricao,
            preco=dto.preco,
            estoque=dto.estoque or 0,
            categoria_id=dto.categoria_id,
            status=StatusProduto.ATIVO
        )
        
        db.session.add(produto)
        db.session.commit()
        return produto
    
    @staticmethod
    def atualizar_produto(produto_id: int, dto: AtualizarProdutoDTO) -> Optional[Produto]:
        """Atualiza um produto existente"""
        produto = Produto.query.get(produto_id)
        if not produto:
            return None
        
        if dto.nome is not None:
            produto.nome = dto.nome
        
        if dto.descricao is not None:
            produto.descricao = dto.descricao
        
        if dto.preco is not None:
            produto.preco = dto.preco
        
        if dto.estoque is not None:
            produto.estoque = dto.estoque
        
        if dto.categoria_id is not None:
            categoria = Categoria.query.get(dto.categoria_id)
            if not categoria:
                raise ValueError("Categoria não encontrada")
            produto.categoria_id = dto.categoria_id
        
        if dto.status is not None:
            try:
                produto.status = StatusProduto(dto.status)
            except ValueError:
                raise ValueError("Status inválido")
        
        db.session.commit()
        return produto
    
    @staticmethod
    def excluir_produto(produto_id: int) -> bool:
        """Exclui um produto"""
        produto = Produto.query.get(produto_id)
        if not produto:
            return False
        
        db.session.delete(produto)
        db.session.commit()
        return True

class CategoriaService:
    
    @staticmethod
    def listar_categorias() -> List[Categoria]:
        """Lista todas as categorias"""
        return Categoria.query.all()
    
    @staticmethod
    def obter_categoria_por_id(categoria_id: int) -> Optional[Categoria]:
        """Obtém uma categoria pelo ID"""
        return Categoria.query.get(categoria_id)
    
    @staticmethod
    def criar_categoria(dto: CriarCategoriaDTO) -> Categoria:
        """Cria uma nova categoria"""
        # Verifica se já existe uma categoria com o mesmo nome
        categoria_existente = Categoria.query.filter_by(nome=dto.nome).first()
        if categoria_existente:
            raise ValueError("Já existe uma categoria com este nome")
        
        categoria = Categoria(
            nome=dto.nome,
            descricao=dto.descricao
        )
        
        db.session.add(categoria)
        db.session.commit()
        return categoria
    
    @staticmethod
    def atualizar_categoria(categoria_id: int, dto: AtualizarCategoriaDTO) -> Optional[Categoria]:
        """Atualiza uma categoria existente"""
        categoria = Categoria.query.get(categoria_id)
        if not categoria:
            return None
        
        if dto.nome is not None:
            # Verifica se já existe outra categoria com o mesmo nome
            categoria_existente = Categoria.query.filter(
                Categoria.nome == dto.nome,
                Categoria.id != categoria_id
            ).first()
            if categoria_existente:
                raise ValueError("Já existe uma categoria com este nome")
            
            categoria.nome = dto.nome
        
        if dto.descricao is not None:
            categoria.descricao = dto.descricao
        
        db.session.commit()
        return categoria
    
    @staticmethod
    def excluir_categoria(categoria_id: int) -> bool:
        """Exclui uma categoria se não tiver produtos associados"""
        categoria = Categoria.query.get(categoria_id)
        if not categoria:
            return False
        
        # Verifica se há produtos associados
        if categoria.produtos:
            raise ValueError("Não é possível excluir categoria com produtos associados")
        
        db.session.delete(categoria)
        db.session.commit()
        return True

