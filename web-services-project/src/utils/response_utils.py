from flask import jsonify
from typing import Any, Dict, List, Optional

class ResponseUtils:
    
    @staticmethod
    def sucesso(data: Any = None, mensagem: str = "Operação realizada com sucesso", status_code: int = 200):
        """Retorna uma resposta de sucesso padronizada"""
        response = {
            "sucesso": True,
            "mensagem": mensagem,
            "dados": data
        }
        return jsonify(response), status_code
    
    @staticmethod
    def erro(mensagem: str, detalhes: Optional[List[str]] = None, status_code: int = 400):
        """Retorna uma resposta de erro padronizada"""
        response = {
            "sucesso": False,
            "mensagem": mensagem,
            "detalhes": detalhes or []
        }
        return jsonify(response), status_code
    
    @staticmethod
    def erro_validacao(erros: List[str]):
        """Retorna uma resposta de erro de validação"""
        return ResponseUtils.erro(
            mensagem="Dados inválidos",
            detalhes=erros,
            status_code=422
        )
    
    @staticmethod
    def nao_encontrado(recurso: str = "Recurso"):
        """Retorna uma resposta de recurso não encontrado"""
        return ResponseUtils.erro(
            mensagem=f"{recurso} não encontrado",
            status_code=404
        )
    
    @staticmethod
    def erro_interno(mensagem: str = "Erro interno do servidor"):
        """Retorna uma resposta de erro interno"""
        return ResponseUtils.erro(
            mensagem=mensagem,
            status_code=500
        )
    
    @staticmethod
    def criado(data: Any, mensagem: str = "Recurso criado com sucesso"):
        """Retorna uma resposta de recurso criado"""
        return ResponseUtils.sucesso(
            data=data,
            mensagem=mensagem,
            status_code=201
        )
    
    @staticmethod
    def sem_conteudo(mensagem: str = "Operação realizada com sucesso"):
        """Retorna uma resposta sem conteúdo"""
        response = {
            "sucesso": True,
            "mensagem": mensagem
        }
        return jsonify(response), 204

