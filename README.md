# Projeto ArkManutenção

Este projeto realiza um processo de consumo e criação de API Rest (por meio do Django Rest Framework) para organizar dados de empresas, equipamentos e chamados presentes em uma infraestrutura de software de manutenção e gestão dos mesmos.

O repositório atual é correspondente apenas ao _back-end_ do projeto. Para acessar e clonar o _front-end_ (em ReactJS), clique aqui

## Rodando o _back-end_

- Primeiramente, instale as dependências/requisitos do projeto

`pip install -r requirements.txt`

- Em seguida, migre os models do projeto

`python manage.py migrate`

- Para concluir, execute o script de captação de dados do projeto

`python manage.py scriptmanutencao`

_**OBS**: para o funcionamento do projeto, é fundamental que tanto o _front_ quanto o _back-end_ estejam rodando nas seguintes portas:_

React:   `http://localhost:3000/`

Django:   `http://localhost:8000/`

## Rodando o _front-end_


