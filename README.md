# Cronograma Médico

Este é um projeto desenvolvido em Python, utilizando SQLAlchemy e Pydantic, com o objetivo de criar um cronograma médico para auxiliar os usuários na utilização de remédios controlados.

## Funcionalidades

- Cadastro de pacientes
- Registro de consultas médicas
- Criação de receitas médicas
- Atualização e exclusão de informações de pacientes e receitas
- Listagem de pacientes e receitas

## Tecnologias Utilizadas

- **Backend**: Python, FastAPI, SQLAlchemy, Pydantic
- **Frontend**: HTML, CSS, JavaScript
- **Banco de Dados**: SQLite (ou o banco de dados de sua escolha)
- **Outras Dependências**: SimpleDatatables

## Instalação

### Pré-requisitos

- Python 3.6 ou superior
- Virtualenv (opcional, mas recomendado)

### Passos para a instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Configure o banco de dados:
    - O banco de dados será configurado automaticamente ao iniciar o servidor pela primeira vez.

5. Inicie o servidor:
    ```bash
    flask run
    ```

6. Acesse a aplicação no navegador:
    ```
    http://127.0.0.1:8000
    ```

## Estrutura do Projeto

- `main.py`: Arquivo principal que inicia a aplicação FastAPI.
- `models.py`: Define os modelos de dados utilizando SQLAlchemy.
- `schemas.py`: Define os esquemas de dados utilizando Pydantic.
- `routes/`: Contém os arquivos de rotas/endpoints.
- `static/`: Contém os arquivos estáticos (CSS, JavaScript).
- `templates/`: Contém os arquivos HTML.

## Endpoints

- `GET /pacientes`: Lista todos os pacientes.
- `POST /paciente/create`: Cria um novo paciente.
- `PUT /paciente/update`: Atualiza as informações de um paciente existente.
- `DELETE /paciente/delete`: Deleta um paciente.

- `GET /receitas`: Lista todas as receitas.
- `POST /receita/create`: Cria uma nova receita.
- `DELETE /receita/delete`: Deleta uma receita.
