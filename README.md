# DimDim App - API REST Flask

Aplicação bancária DimDim desenvolvida com Flask e PostgreSQL, containerizada com Docker.

## 🏗️ Arquitetura

- **Backend**: Python Flask
- **Banco de Dados**: PostgreSQL 15
- **Containerização**: Docker
- **Rede**: Docker Bridge personalizada

## 🚀 Como Executar

### Pré-requisitos
- Docker instalado
- Portas 5000 livres

### Execução Rápida

Clonar repositório
git clone https://github.com/JPAmorimBV/CP-Devops
cd dimdim-app

Build da aplicação
./scripts/build.sh

Executar aplicação
./scripts/run.sh
### Execução Manual
Criar rede
docker network create dimdim-network

Executar banco
docker run -d --name dimdim-db --network dimdim-network
-e POSTGRES_PASSWORD=senha123 -e POSTGRES_DB=dimdimapp -e POSTGRES_USER=dimdim
-v dimdim-data:/var/lib/postgresql/data postgres:15

Build da aplicação
docker build -t dimdim-app .

Executar aplicação
docker run -d --name dimdim-application --network dimdim-network
-p 5000:5000
-e DATABASE_URL=postgresql://dimdim:senha123@dimdim-db:5432/dimdimapp
dimdim-app

## 📋 API Endpoints

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | `/` | Página inicial |
| GET | `/api/clientes` | Listar todos os clientes |
| GET | `/api/clientes/{id}` | Buscar cliente por ID |
| POST | `/api/clientes` | Criar novo cliente |
| PUT | `/api/clientes/{id}` | Atualizar cliente |
| DELETE | `/api/clientes/{id}` | Deletar cliente |

## 🧪 Testando a API

### Criar Cliente

curl -X POST http://localhost:5000/api/clientes
-H "Content-Type: application/json"
-d '{"nome": "João Silva", "email": "joao@email.com", "cpf": "123.456.789-00"}'

### Listar Clientes

curl http://localhost:5000/api/clientes
[200~
## 🔧 Verificações Docker

Verificar estrutura da aplicação
docker container exec dimdim-application pwd
docker container exec dimdim-application ls -la
docker container exec dimdim-application whoami
Verificar banco de dados
docker container exec dimdim-db pwd
docker container exec dimdim-db whoami

## ✅ Validações Implementadas

- [x] Dois containers em rede personalizada
- [x] Volume para persistência do banco
- [x] Dockerfile personalizado com usuário não-root
- [x] Variáveis de ambiente configuradas
- [x] CRUD completo funcionando
- [x] Persistência de dados testada
