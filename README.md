# backend-tests

Project Details:

- Será feito varios projetos aqui, para aprofundamento do meu conhecimento em APIs, banco de dados e POO;
- Vou documentar todos os passos que julgar ser importante para compartilhar esses conhecimentos com o próximo também;
- Estarei usando o padrão MVC para a arquitetura, visto que o django também segue esse padrão, vejo como uma boa prática para organizar os projetos;
- As APIs, vou usar o fastAPI;
- O banco de dado, será o mySQL, pois já trabalho com postgres e mongoDB, logo quero aprofundar minhas skills em outras frentes, por mais que prefire o postgres é importante ter o maximo de contato com outras ferramentas;

Dependencies:

1. Conectar no ambiente virtual: backend_testing
2. Instalar as dependencias:
    a. mySQL connector
    b. fastAPI (instalar também o uvicorn para ser o servidor)
3. Confirmar as dependencias intaladas

Comandos:

Ambiente virtual:
1. python3 -m venv myproject
2. source myproject/bin/activate

observação: antes de começar a instalar as dependencias, como boa prática, faça a atualização do comando pip do python:
pip install --upgrade pip

mySQL connect:
pip install mysql-connector-python

fastAPI:
pip install fastapi

Pacote cliente escolhido é o httpx ao inves de request, pq ele trabalha assincrono:
pip install httpx

Servidor ASGI para o fastAPI:
pip install uvicorn

Confirmar as dependencias instaladas:
pip list

Depois de tudo configurado corretamente, é só rodar o servidor:
uvicorn main:app --reload
