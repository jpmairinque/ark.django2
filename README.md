# Projeto ArkManutenção ⚕️🏥

![Group 33](https://user-images.githubusercontent.com/53411709/135100090-5cda033b-c89f-4f46-85b6-6a04bfe4d506.png)

##

Este projeto realiza um processo de consumo e criação de API Rest (por meio do Django Rest Framework) para organizar dados de empresas, equipamentos e chamados presentes em uma infraestrutura de software de manutenção e gestão dos mesmos.

_// This project runs a process of Rest APIs consumption and creation that organizes data from companies, equipments and order tickets in a software maintenance infrastructure._

O repositório atual é correspondente apenas ao _back-end_ do projeto. Para acessar e clonar o _front-end_ (em ReactJS), clique [aqui](https://github.com/jpmairinque/ark.reactjs).

_// The current repository relates only to the project's back-end code. Click [here](https://github.com/jpmairinque/ark.reactjs) to acces and clone the front-end code_

## Executando o _back-end // Running the back-end_ 💿🎲

- Primeiramente, instale as dependências/requisitos do projeto

```
pip install -r requirements.txt
```

- Em seguida, migre os models do projeto

```
python manage.py migrate
```

- Para concluir, execute o script de captação de dados do projeto

```
python manage.py scriptmanutencao
```

_**OBS**: para o funcionamento do projeto, é fundamental que tanto o _front_ quanto o _back-end_ estejam rodando nas seguintes portas:_

React:   
```
http://localhost:3000/
```

Django:   
```
http://localhost:8000/
```

## Executando o _front-end // Running the back-end_ 💿📱

- Primeiramente, instale as dependências do projeto 

```
npm install || yarn install
```

- Em seguida, apenas execute-o

```
npm start || yarn start
```
_**OBS**: se atente na execução do servidor backend antes do React, já que este é dependente da api do Django_

## Ferramentas utilizadas 🛠

- Django 2.2.24
- Django Rest Framework
- Python 3
- ReactJS
- Styled Components
- Fetch API




