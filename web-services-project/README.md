# Sistema de Gerenciamento de Produtos - Web Services

# Gabriel teixeira machado rm551570
# Guilherme Brazioli rm98237
# Felipe Bressane rm97688
# Camila do Prado Padalino rm98316

## Descrição do Projeto

A aplicação consiste em um sistema de gerenciamento de produtos e categorias que expõe funcionalidades através de Web Services RESTful, seguindo as melhores práticas de desenvolvimento de software e arquitetura de sistemas.

### Objetivos do Projeto

O sistema foi desenvolvido com os seguintes objetivos principais:

- Demonstrar a implementação prática de Web Services utilizando arquitetura REST
- Aplicar conceitos de Arquitetura Orientada a Serviços (SOA)
- Implementar operações CRUD completas com validação de dados
- Criar uma interface de usuário para consumo dos serviços
- Estabelecer uma arquitetura em camadas bem estruturada
- Aplicar boas práticas de desenvolvimento, incluindo tratamento de erros e padronização de respostas

### Funcionalidades Principais

O sistema oferece as seguintes funcionalidades:

**Gerenciamento de Categorias:**
- Criação de novas categorias de produtos
- Listagem de todas as categorias cadastradas
- Consulta de categoria específica por ID
- Atualização de informações de categorias existentes
- Exclusão de categorias (com validação de integridade referencial)

**Gerenciamento de Produtos:**
- Cadastro de novos produtos com informações completas
- Listagem de produtos com filtros por categoria e status
- Consulta detalhada de produto específico
- Atualização de informações de produtos
- Controle de status (Ativo, Inativo, Descontinuado)
- Gerenciamento de estoque
- Exclusão de produtos

**Interface Web:**
- Interface gráfica intuitiva para interação com os Web Services
- Formulários para criação e edição de dados
- Visualização organizada de informações
- Ferramenta de teste manual de API
- Feedback visual das operações realizadas

## Tecnologias Utilizadas

### Backend
- **Python 3.11**: Linguagem de programação principal
- **Flask**: Framework web para criação dos Web Services
- **SQLAlchemy**: ORM (Object-Relational Mapping) para abstração do banco de dados
- **SQLite**: Sistema de gerenciamento de banco de dados
- **Flask-SQLAlchemy**: Integração entre Flask e SQLAlchemy

### Frontend
- **HTML5**: Estruturação da interface web
- **CSS3**: Estilização e design responsivo
- **JavaScript (ES6+)**: Lógica de interação e consumo de APIs
- **Fetch API**: Comunicação assíncrona com os Web Services

### Arquitetura e Padrões
- **Arquitetura REST**: Para design dos Web Services
- **Padrão MVC**: Separação de responsabilidades
- **DTO (Data Transfer Objects)**: Validação e transferência de dados
- **Service Layer**: Camada de lógica de negócio
- **Repository Pattern**: Abstração de acesso a dados

## Arquitetura do Sistema

### Estrutura de Camadas

O sistema foi desenvolvido seguindo uma arquitetura em camadas bem definida:

```
┌─────────────────────────────────────┐
│           Interface Web             │
│        (HTML/CSS/JavaScript)        │
├─────────────────────────────────────┤
│          Web Services Layer         │
│           (Flask Routes)            │
├─────────────────────────────────────┤
│         Service Layer               │
│        (Business Logic)             │
├─────────────────────────────────────┤
│          Data Access Layer          │
│         (SQLAlchemy ORM)            │
├─────────────────────────────────────┤
│          Database Layer             │
│           (SQLite)                  │
└─────────────────────────────────────┘
```

### Componentes Principais

**1. Modelos de Dados (Models)**
- `Categoria`: Representa as categorias de produtos
- `Produto`: Representa os produtos do sistema
- `StatusProduto`: Enum para controle de status dos produtos

**2. Objetos de Transferência de Dados (DTOs)**
- `CriarCategoriaDTO`: Validação para criação de categorias
- `AtualizarCategoriaDTO`: Validação para atualização de categorias
- `CriarProdutoDTO`: Validação para criação de produtos
- `AtualizarProdutoDTO`: Validação para atualização de produtos

**3. Camada de Serviços (Services)**
- `CategoriaService`: Lógica de negócio para categorias
- `ProdutoService`: Lógica de negócio para produtos

**4. Controladores (Routes)**
- `produto.py`: Endpoints REST para produtos e categorias
- `user.py`: Endpoints de exemplo para usuários

**5. Utilitários**
- `ResponseUtils`: Padronização de respostas HTTP
- `error_handlers.py`: Tratamento global de erros




## Configuração e Execução

### Pré-requisitos

Para executar este projeto, você precisará ter instalado em seu sistema:

- Python 3.11 ou superior
- pip (gerenciador de pacotes Python)
- Git (para clonagem do repositório)

### Passos de Instalação

**1. Preparação do Ambiente**

Primeiro, extraia o arquivo ZIP do projeto e navegue até o diretório:

```bash
unzip web-services-project.zip
cd web-services-project
```

**2. Ativação do Ambiente Virtual**

O projeto já inclui um ambiente virtual configurado. Para ativá-lo:

No Linux/macOS:
```bash
source venv/bin/activate
```

No Windows:
```bash
venv\Scripts\activate
```

**3. Verificação das Dependências**

As dependências já estão instaladas no ambiente virtual, mas você pode verificá-las:

```bash
pip list
```

As principais dependências incluem:
- Flask
- Flask-SQLAlchemy
- SQLAlchemy

**4. Inicialização do Banco de Dados**

O banco de dados SQLite será criado automaticamente na primeira execução. O arquivo será gerado em `src/database/app.db`.

**5. Execução da Aplicação**

Para iniciar o servidor de desenvolvimento:

```bash
python src/main.py
```

A aplicação estará disponível em:
- **Interface Web**: http://localhost:5000
- **API Base URL**: http://localhost:5000/api

### Verificação da Instalação

Após iniciar a aplicação, você pode verificar se tudo está funcionando corretamente:

1. Acesse http://localhost:5000 no seu navegador
2. Você deve ver a interface do "Sistema de Gerenciamento de Produtos"
3. Teste a criação de uma categoria na aba "Categorias"
4. Teste a criação de um produto na aba "Produtos"

### Estrutura de Diretórios

```
web-services-project/
├── venv/                          # Ambiente virtual Python
├── src/                           # Código fonte da aplicação
│   ├── models/                    # Modelos de dados
│   │   ├── user.py               # Modelo de usuário (exemplo)
│   │   └── produto.py            # Modelos de produto e categoria
│   ├── routes/                    # Controladores/Endpoints
│   │   ├── user.py               # Rotas de usuário (exemplo)
│   │   └── produto.py            # Rotas de produtos e categorias
│   ├── services/                  # Camada de lógica de negócio
│   │   └── produto_service.py    # Serviços de produtos e categorias
│   ├── dto/                       # Objetos de transferência de dados
│   │   └── produto_dto.py        # DTOs para validação
│   ├── utils/                     # Utilitários
│   │   └── response_utils.py     # Padronização de respostas
│   ├── static/                    # Arquivos estáticos (frontend)
│   │   └── index.html            # Interface web principal
│   ├── database/                  # Banco de dados
│   │   └── app.db                # Arquivo SQLite (criado automaticamente)
│   ├── main.py                   # Ponto de entrada da aplicação
│   └── error_handlers.py         # Tratamento global de erros
├── requirements.txt              # Dependências do projeto
└── README.md                    # Esta documentação
```

## Exemplos de Uso

### Endpoints da API

A API REST oferece os seguintes endpoints:

#### Categorias

**Listar todas as categorias**
```http
GET /api/categorias
```

Resposta de exemplo:
```json
{
  "sucesso": true,
  "mensagem": "Encontradas 1 categorias",
  "dados": [
    {
      "id": 1,
      "nome": "Eletrônicos",
      "descricao": "Produtos eletrônicos em geral",
      "data_criacao": "2025-09-21T12:44:23.834650"
    }
  ]
}
```

**Criar nova categoria**
```http
POST /api/categorias
Content-Type: application/json

{
  "nome": "Livros",
  "descricao": "Livros e publicações diversas"
}
```

**Obter categoria específica**
```http
GET /api/categorias/1
```

**Atualizar categoria**
```http
PUT /api/categorias/1
Content-Type: application/json

{
  "nome": "Eletrônicos e Tecnologia",
  "descricao": "Produtos eletrônicos, tecnologia e gadgets"
}
```

**Excluir categoria**
```http
DELETE /api/categorias/1
```

#### Produtos

**Listar todos os produtos**
```http
GET /api/produtos
```

**Listar produtos com filtros**
```http
GET /api/produtos?categoria_id=1&status=ATIVO
```

Resposta de exemplo:
```json
{
  "sucesso": true,
  "mensagem": "Encontrados 2 produtos",
  "dados": [
    {
      "id": 1,
      "nome": "Smartphone Samsung",
      "descricao": "Smartphone Android com 128GB",
      "preco": 899.99,
      "estoque": 10,
      "status": "ATIVO",
      "categoria_id": 1,
      "categoria": "Eletrônicos",
      "data_criacao": "2025-09-21T12:44:27.806485",
      "data_atualizacao": "2025-09-21T12:44:27.806488"
    }
  ]
}
```

**Criar novo produto**
```http
POST /api/produtos
Content-Type: application/json

{
  "nome": "Notebook Dell",
  "descricao": "Notebook Dell Inspiron 15",
  "preco": 2499.99,
  "estoque": 5,
  "categoria_id": 1
}
```

**Obter produto específico**
```http
GET /api/produtos/1
```

**Atualizar produto**
```http
PUT /api/produtos/1
Content-Type: application/json

{
  "nome": "Smartphone Samsung Galaxy",
  "preco": 799.99,
  "estoque": 15,
  "status": "ATIVO"
}
```

**Excluir produto**
```http
DELETE /api/produtos/1
```

### Usando a Interface Web

A interface web oferece uma maneira intuitiva de interagir com os Web Services:

**Aba Categorias:**
- Formulário para criar novas categorias
- Lista de categorias existentes com opções de editar/excluir
- Visualização das respostas da API em tempo real

**Aba Produtos:**
- Formulário completo para cadastro de produtos
- Seleção de categoria através de dropdown
- Filtros por categoria e status
- Lista detalhada de produtos com todas as informações

**Aba Teste de API:**
- Ferramenta para teste manual dos endpoints
- Seleção de método HTTP (GET, POST, PUT, DELETE)
- Campo para inserção de URL personalizada
- Área para inserção de dados JSON
- Visualização da resposta completa da API

### Exemplos de Validação

O sistema implementa validações robustas em todas as operações:

**Validação de Categoria:**
- Nome é obrigatório e não pode estar vazio
- Nome deve ter no máximo 100 caracteres
- Não é permitido criar categorias com nomes duplicados

**Validação de Produto:**
- Nome é obrigatório e não pode estar vazio
- Nome deve ter no máximo 200 caracteres
- Preço deve ser um valor positivo
- Categoria deve existir no sistema
- Estoque não pode ser negativo
- Status deve ser um dos valores válidos: ATIVO, INATIVO, DESCONTINUADO

**Exemplo de Resposta de Erro de Validação:**
```json
{
  "sucesso": false,
  "mensagem": "Dados inválidos",
  "detalhes": [
    "Nome do produto é obrigatório",
    "Preço deve ser um valor positivo"
  ]
}
```


## Detalhes Técnicos da Implementação

### Padrões de Design Utilizados

O projeto implementa diversos padrões de design reconhecidos na indústria de software, garantindo código limpo, manutenível e extensível.

**Data Transfer Object (DTO) Pattern**

Os DTOs são utilizados para validação e transferência segura de dados entre as camadas da aplicação. Cada DTO implementa métodos de validação específicos que garantem a integridade dos dados antes do processamento:

```python
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
        if self.preco is None or self.preco < 0:
            erros.append("Preço deve ser um valor positivo")
        return erros
```

**Service Layer Pattern**

A camada de serviços encapsula toda a lógica de negócio da aplicação, mantendo os controladores focados apenas na manipulação de requisições HTTP. Esta separação permite maior testabilidade e reutilização de código:

```python
class ProdutoService:
    @staticmethod
    def criar_produto(dto: CriarProdutoDTO) -> Produto:
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
```

**Repository Pattern através do SQLAlchemy ORM**

O SQLAlchemy atua como uma implementação do padrão Repository, fornecendo uma interface consistente para acesso aos dados independentemente do banco de dados subjacente. Isso permite fácil migração entre diferentes SGBDs sem alterações no código de negócio.

### Tratamento de Erros e Exceções

O sistema implementa um tratamento robusto de erros em múltiplas camadas:

**Tratamento Global de Erros**

Um sistema de tratamento global de erros captura e padroniza todas as exceções não tratadas, garantindo que o cliente sempre receba uma resposta estruturada:

```python
@app.errorhandler(Exception)
def handle_exception(error):
    if isinstance(error, HTTPException):
        return error
    
    app.logger.error(f"Erro não tratado: {str(error)}")
    return ResponseUtils.erro(
        mensagem="Erro interno do servidor",
        detalhes=["Ocorreu um erro inesperado. Tente novamente mais tarde."],
        status_code=500
    )
```

**Padronização de Respostas**

Todas as respostas da API seguem um padrão consistente através da classe `ResponseUtils`, facilitando o consumo pelos clientes:

```python
class ResponseUtils:
    @staticmethod
    def sucesso(data: Any = None, mensagem: str = "Operação realizada com sucesso", status_code: int = 200):
        response = {
            "sucesso": True,
            "mensagem": mensagem,
            "dados": data
        }
        return jsonify(response), status_code
    
    @staticmethod
    def erro(mensagem: str, detalhes: Optional[List[str]] = None, status_code: int = 400):
        response = {
            "sucesso": False,
            "mensagem": mensagem,
            "detalhes": detalhes or []
        }
        return jsonify(response), status_code
```

### Segurança e Boas Práticas

**Validação de Entrada**

Todas as entradas do usuário passam por validação rigorosa antes do processamento. O sistema utiliza DTOs com métodos de validação específicos que verificam tipos de dados, comprimentos de string, valores numéricos e regras de negócio.

**Integridade Referencial**

O sistema mantém a integridade referencial através de validações na camada de serviço. Por exemplo, não é possível excluir uma categoria que possui produtos associados:

```python
def excluir_categoria(categoria_id: int) -> bool:
    categoria = Categoria.query.get(categoria_id)
    if not categoria:
        return False
    
    # Verifica se há produtos associados
    if categoria.produtos:
        raise ValueError("Não é possível excluir categoria com produtos associados")
    
    db.session.delete(categoria)
    db.session.commit()
    return True
```

**CORS (Cross-Origin Resource Sharing)**

O sistema está configurado para permitir requisições de diferentes origens, facilitando a integração com frontends hospedados em domínios diferentes:

```python
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
```

### Performance e Escalabilidade

**Otimização de Consultas**

O sistema utiliza relacionamentos do SQLAlchemy para otimizar consultas ao banco de dados, evitando o problema N+1 através de eager loading quando necessário:

```python
# Carregamento otimizado de produtos com suas categorias
produtos = Produto.query.options(joinedload(Produto.categoria_ref)).all()
```

**Paginação Preparada**

Embora não implementada nesta versão, a estrutura está preparada para implementação de paginação em consultas que retornam grandes volumes de dados.

**Caching de Respostas**

A arquitetura permite fácil implementação de cache em diferentes níveis (aplicação, banco de dados, HTTP) sem modificações significativas no código existente.

## Considerações de Arquitetura

### Princípios SOLID Aplicados

O projeto segue os princípios SOLID de design orientado a objetos:

**Single Responsibility Principle (SRP)**: Cada classe tem uma única responsabilidade bem definida. Por exemplo, `ProdutoService` é responsável apenas pela lógica de negócio de produtos.

**Open/Closed Principle (OCP)**: O sistema está aberto para extensão mas fechado para modificação. Novos tipos de validação podem ser adicionados sem alterar código existente.

**Liskov Substitution Principle (LSP)**: As implementações podem ser substituídas por suas abstrações sem quebrar a funcionalidade.

**Interface Segregation Principle (ISP)**: As interfaces são específicas e focadas, evitando dependências desnecessárias.

**Dependency Inversion Principle (DIP)**: O código depende de abstrações (interfaces) ao invés de implementações concretas.

### Testabilidade

A arquitetura em camadas facilita a criação de testes unitários e de integração:

- **Testes de Unidade**: Cada serviço pode ser testado isoladamente
- **Testes de Integração**: Os endpoints podem ser testados com bancos de dados em memória
- **Testes de Interface**: A interface web pode ser testada com ferramentas de automação

### Manutenibilidade

O código foi estruturado pensando na facilidade de manutenção:

- **Separação Clara de Responsabilidades**: Cada arquivo tem um propósito específico
- **Nomenclatura Consistente**: Variáveis, funções e classes seguem convenções claras
- **Documentação Inline**: Código documentado com docstrings e comentários explicativos
- **Estrutura Modular**: Funcionalidades organizadas em módulos independentes

### Extensibilidade

O sistema foi projetado para fácil extensão:

- **Novos Modelos**: Podem ser adicionados seguindo o mesmo padrão
- **Novos Endpoints**: Facilmente implementados através de novos Blueprints
- **Novas Validações**: DTOs permitem adição de regras sem impacto no código existente
- **Novos Formatos de Resposta**: O sistema de resposta padronizada facilita mudanças de formato

## Conclusão

Este projeto demonstra uma implementação completa e profissional de um sistema baseado em Arquitetura Orientada a Serviços e Web Services. A aplicação segue as melhores práticas da indústria de software, implementa padrões de design reconhecidos e oferece uma base sólida para futuras expansões.

A combinação de uma API REST bem estruturada com uma interface web intuitiva proporciona uma experiência completa tanto para desenvolvedores que desejam integrar com os serviços quanto para usuários finais que precisam de uma interface gráfica.


