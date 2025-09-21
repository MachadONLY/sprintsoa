from flask import Blueprint, request
from src.services.produto_service import ProdutoService, CategoriaService
from src.dto.produto_dto import CriarProdutoDTO, AtualizarProdutoDTO, CriarCategoriaDTO, AtualizarCategoriaDTO
from src.utils.response_utils import ResponseUtils

produto_bp = Blueprint('produto', __name__)

# Rotas para Produtos
@produto_bp.route('/produtos', methods=['GET'])
def listar_produtos():
    """Lista produtos com filtros opcionais"""
    try:
        categoria_id = request.args.get('categoria_id', type=int)
        status = request.args.get('status')
        
        produtos = ProdutoService.listar_produtos(categoria_id, status)
        dados = [produto.to_dict() for produto in produtos]
        
        return ResponseUtils.sucesso(
            data=dados,
            mensagem=f"Encontrados {len(dados)} produtos"
        )
    except Exception as e:
        return ResponseUtils.erro_interno(f"Erro ao listar produtos: {str(e)}")

@produto_bp.route('/produtos/<int:produto_id>', methods=['GET'])
def obter_produto(produto_id):
    """Obtém um produto específico pelo ID"""
    try:
        produto = ProdutoService.obter_produto_por_id(produto_id)
        
        if not produto:
            return ResponseUtils.nao_encontrado("Produto")
        
        return ResponseUtils.sucesso(
            data=produto.to_dict(),
            mensagem="Produto encontrado"
        )
    except Exception as e:
        return ResponseUtils.erro_interno(f"Erro ao obter produto: {str(e)}")

@produto_bp.route('/produtos', methods=['POST'])
def criar_produto():
    """Cria um novo produto"""
    try:
        dados = request.get_json(force=True)
        
        if not dados:
            return ResponseUtils.erro("Dados não fornecidos")
        
        dto = CriarProdutoDTO(
            nome=dados.get('nome'),
            descricao=dados.get('descricao'),
            preco=dados.get('preco'),
            estoque=dados.get('estoque', 0),
            categoria_id=dados.get('categoria_id')
        )
        
        erros = dto.validar()
        if erros:
            return ResponseUtils.erro_validacao(erros)
        
        produto = ProdutoService.criar_produto(dto)
        
        return ResponseUtils.criado(
            data=produto.to_dict(),
            mensagem="Produto criado com sucesso"
        )
        
    except ValueError as e:
        return ResponseUtils.erro(str(e))
    except Exception as e:
        return ResponseUtils.erro_interno(f"Erro ao criar produto: {str(e)}")

@produto_bp.route('/produtos/<int:produto_id>', methods=['PUT'])
def atualizar_produto(produto_id):
    """Atualiza um produto existente"""
    try:
        dados = request.get_json(force=True)
        
        if not dados:
            return ResponseUtils.erro("Dados não fornecidos")
        
        dto = AtualizarProdutoDTO(
            nome=dados.get('nome'),
            descricao=dados.get('descricao'),
            preco=dados.get('preco'),
            estoque=dados.get('estoque'),
            categoria_id=dados.get('categoria_id'),
            status=dados.get('status')
        )
        
        erros = dto.validar()
        if erros:
            return ResponseUtils.erro_validacao(erros)
        
        produto = ProdutoService.atualizar_produto(produto_id, dto)
        
        if not produto:
            return ResponseUtils.nao_encontrado("Produto")
        
        return ResponseUtils.sucesso(
            data=produto.to_dict(),
            mensagem="Produto atualizado com sucesso"
        )
        
    except ValueError as e:
        return ResponseUtils.erro(str(e))
    except Exception as e:
        return ResponseUtils.erro_interno(f"Erro ao atualizar produto: {str(e)}")

@produto_bp.route('/produtos/<int:produto_id>', methods=['DELETE'])
def excluir_produto(produto_id):
    """Exclui um produto"""
    try:
        sucesso = ProdutoService.excluir_produto(produto_id)
        
        if not sucesso:
            return ResponseUtils.nao_encontrado("Produto")
        
        return ResponseUtils.sem_conteudo("Produto excluído com sucesso")
        
    except Exception as e:
        return ResponseUtils.erro_interno(f"Erro ao excluir produto: {str(e)}")

# Rotas para Categorias
@produto_bp.route('/categorias', methods=['GET'])
def listar_categorias():
    """Lista todas as categorias"""
    try:
        categorias = CategoriaService.listar_categorias()
        dados = [categoria.to_dict() for categoria in categorias]
        
        return ResponseUtils.sucesso(
            data=dados,
            mensagem=f"Encontradas {len(dados)} categorias"
        )
    except Exception as e:
        return ResponseUtils.erro_interno(f"Erro ao listar categorias: {str(e)}")

@produto_bp.route('/categorias/<int:categoria_id>', methods=['GET'])
def obter_categoria(categoria_id):
    """Obtém uma categoria específica pelo ID"""
    try:
        categoria = CategoriaService.obter_categoria_por_id(categoria_id)
        
        if not categoria:
            return ResponseUtils.nao_encontrado("Categoria")
        
        return ResponseUtils.sucesso(
            data=categoria.to_dict(),
            mensagem="Categoria encontrada"
        )
    except Exception as e:
        return ResponseUtils.erro_interno(f"Erro ao obter categoria: {str(e)}")

@produto_bp.route('/categorias', methods=['POST'])
def criar_categoria():
    """Cria uma nova categoria"""
    try:
        dados = request.get_json(force=True)
        
        if not dados:
            return ResponseUtils.erro("Dados não fornecidos")
        
        dto = CriarCategoriaDTO(
            nome=dados.get('nome'),
            descricao=dados.get('descricao')
        )
        
        erros = dto.validar()
        if erros:
            return ResponseUtils.erro_validacao(erros)
        
        categoria = CategoriaService.criar_categoria(dto)
        
        return ResponseUtils.criado(
            data=categoria.to_dict(),
            mensagem="Categoria criada com sucesso"
        )
        
    except ValueError as e:
        return ResponseUtils.erro(str(e))
    except Exception as e:
        return ResponseUtils.erro_interno(f"Erro ao criar categoria: {str(e)}")

@produto_bp.route('/categorias/<int:categoria_id>', methods=['PUT'])
def atualizar_categoria(categoria_id):
    """Atualiza uma categoria existente"""
    try:
        dados = request.get_json(force=True)
        
        if not dados:
            return ResponseUtils.erro("Dados não fornecidos")
        
        dto = AtualizarCategoriaDTO(
            nome=dados.get('nome'),
            descricao=dados.get('descricao')
        )
        
        erros = dto.validar()
        if erros:
            return ResponseUtils.erro_validacao(erros)
        
        categoria = CategoriaService.atualizar_categoria(categoria_id, dto)
        
        if not categoria:
            return ResponseUtils.nao_encontrado("Categoria")
        
        return ResponseUtils.sucesso(
            data=categoria.to_dict(),
            mensagem="Categoria atualizada com sucesso"
        )
        
    except ValueError as e:
        return ResponseUtils.erro(str(e))
    except Exception as e:
        return ResponseUtils.erro_interno(f"Erro ao atualizar categoria: {str(e)}")

@produto_bp.route('/categorias/<int:categoria_id>', methods=['DELETE'])
def excluir_categoria(categoria_id):
    """Exclui uma categoria"""
    try:
        sucesso = CategoriaService.excluir_categoria(categoria_id)
        
        if not sucesso:
            return ResponseUtils.nao_encontrado("Categoria")
        
        return ResponseUtils.sem_conteudo("Categoria excluída com sucesso")
        
    except ValueError as e:
        return ResponseUtils.erro(str(e))
    except Exception as e:
        return ResponseUtils.erro_interno(f"Erro ao excluir categoria: {str(e)}")

