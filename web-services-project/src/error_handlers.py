from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException
from src.utils.response_utils import ResponseUtils

def register_error_handlers(app: Flask):
    """Registra os manipuladores de erro globais da aplicação"""
    
    @app.errorhandler(400)
    def bad_request(error):
        """Manipula erros de requisição inválida"""
        return ResponseUtils.erro(
            mensagem="Requisição inválida",
            detalhes=[str(error.description)] if error.description else [],
            status_code=400
        )
    
    @app.errorhandler(404)
    def not_found(error):
        """Manipula erros de recurso não encontrado"""
        return ResponseUtils.erro(
            mensagem="Recurso não encontrado",
            detalhes=["A URL solicitada não foi encontrada no servidor"],
            status_code=404
        )
    
    @app.errorhandler(405)
    def method_not_allowed(error):
        """Manipula erros de método não permitido"""
        return ResponseUtils.erro(
            mensagem="Método não permitido",
            detalhes=[f"O método {error.description} não é permitido para esta URL"],
            status_code=405
        )
    
    @app.errorhandler(422)
    def unprocessable_entity(error):
        """Manipula erros de entidade não processável"""
        return ResponseUtils.erro(
            mensagem="Dados inválidos",
            detalhes=[str(error.description)] if error.description else [],
            status_code=422
        )
    
    @app.errorhandler(500)
    def internal_server_error(error):
        """Manipula erros internos do servidor"""
        return ResponseUtils.erro(
            mensagem="Erro interno do servidor",
            detalhes=["Ocorreu um erro inesperado. Tente novamente mais tarde."],
            status_code=500
        )
    
    @app.errorhandler(Exception)
    def handle_exception(error):
        """Manipula exceções não tratadas"""
        # Se for uma exceção HTTP do Werkzeug, mantém o comportamento padrão
        if isinstance(error, HTTPException):
            return error
        
        # Para outras exceções, retorna erro interno
        app.logger.error(f"Erro não tratado: {str(error)}")
        return ResponseUtils.erro(
            mensagem="Erro interno do servidor",
            detalhes=["Ocorreu um erro inesperado. Tente novamente mais tarde."],
            status_code=500
        )
    
    @app.before_request
    def log_request_info():
        """Log das informações da requisição para debug"""
        app.logger.debug(f"Requisição: {request.method} {request.url}")
        if request.method in ['POST', 'PUT', 'PATCH'] and request.get_json(silent=True):
            app.logger.debug(f"Dados: {request.get_json(silent=True)}")
    
    @app.after_request
    def after_request(response):
        """Adiciona headers CORS e log da resposta"""
        # CORS headers
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        
        # Log da resposta
        app.logger.debug(f"Resposta: {response.status_code}")
        
        return response

