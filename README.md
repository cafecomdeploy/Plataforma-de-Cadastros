# Cadastro de Usuários e Endereços

## Descrição

Este projeto é uma API simples para cadastro de usuários e seus endereços, desenvolvida com FastAPI. O objetivo é fornecer uma interface eficiente e rápida para gerenciar informações de usuários, permitindo que sejam facilmente criados, lidos, atualizados e excluídos.

## Funcionalidades

- **Cadastro de Usuários**: Adicione novos usuários com informações básicas.
- **Gerenciamento de Endereços**: Associe múltiplos endereços a um usuário.
- **API RESTful**: Utilize endpoints claros e intuitivos para interagir com os dados.
- **Documentação Automática**: Acesse a documentação interativa gerada automaticamente pelo FastAPI.

## Tecnologias Utilizadas

- **FastAPI**: Framework moderno para a construção de APIs com Python.
- **Uvicorn**: Servidor ASGI para execução da aplicação.
- **SQLAlchemy**: ORM para gerenciamento do banco de dados.
- **Pydantic**: Validação de dados e criação de modelos.

## Pré-requisitos

Certifique-se de ter o Python 3.7 ou superior instalado em sua máquina.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seuusuario/cadastro-usuarios.git](https://github.com/cafecomdeploy/Plataforma-de-Cadastros.git)

2. Instale as dependências:
  pip install -r requirements.txt

3. Execute a aplicação
  uvicorn app.main:app --reload
