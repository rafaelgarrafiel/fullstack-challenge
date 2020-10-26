# fullstack-challenge

Projeto para atendimento ao fillstack-challenge.

## Tecnologias utilizadas

### Backend
 - Flask

### Frontend
 - React

## Passo a passo para o uso

Clone o repositório:

```bash
git clone https://github.com/rafaelgarrafiel/fullstack-challenge.git
```

## Building 

Entre no diretório fullstack-challenge

```bash
cd fullstack-challenge
```

Realize suba o docker-compose

```bash
docker-compose up -d
```

Criando o banco de dados

```bash
docker exec challenge_backend flask db init
docker exec challenge_backend flask db migrate
docker exec challenge_backend flask db upgrade
docker exec challenge_backend flask populate-db
```

## Acesso

O acesso ao frontend estará disponível em [`http://localhost:3000`](http://localhost:3000).

A api do backend estará disponível em [`http://localhost:8000`](http://localhost:8000).
