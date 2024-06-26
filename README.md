# Formulário Web 

Este projeto é um formulário web simples desenvolvido com Flask, SQLite e SQLAlchemy. Ele permite que usuários enviem suas informações (nome, e-mail e mensagem) através de um formulário. As informações submetidas são armazenadas em um banco de dados SQLite.

## Tecnologias Utilizadas

- **Flask**: Framework web utilizado para criar a aplicação.
- **SQLite**: Banco de dados leve utilizado para armazenar os dados submetidos pelo formulário.
- **SQLAlchemy**: ORM (Object-Relational Mapping) utilizado para interagir com o banco de dados SQLite.
- **Docker**: Plataforma utilizada para containerizar a aplicação, facilitando a implantação e execução.

## Funcionalidades

- Formulário web para entrada de dados (nome, e-mail e mensagem).
- Armazenamento das informações submetidas em um banco de dados SQLite.
- Interface simples para exibição das mensagens armazenadas.

## Como Executar

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
Crie e ative o ambiente virtual:


python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`

Instale as dependências:
pip install -r requirements.txt


Configure o Docker:

Certifique-se de que o Docker está instalado e em execução na sua máquina.
Inicie os contêineres Docker:
docker-compose up 

Acesse a aplicação:
Abra seu navegador e acesse http://localhost:5000.