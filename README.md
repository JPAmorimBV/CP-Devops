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

## 👤 Integrantes
- Carlos Eduardo Rodrigues Coelho Pacheco - RM 557323
- Pedro Augusto Costa ladeira - RM 558514
- João Pedro Amorim Brito Virgens - RM 559213

## 📷 Prints da aplicação
![Print 1 ](https://github.com/user-attachments/assets/43c2d59c-34ba-4017-a84c-a96693bdda36)
![Print 2](https://github.com/user-attachments/assets/11946a26-a54a-4c20-95e5-3f2af553874c)
![Print 3](https://github.com/user-attachments/assets/fd1cb038-1639-4064-b72c-7516b9dbeb51)
![Print 4](https://github.com/user-attachments/assets/777c35ca-2ae3-48b2-ba23-64e167bbc2ea)
![Print 5 ](https://github.com/user-attachments/assets/938d35f8-a1d9-4f26-a5e8-e37239fd71bf)
![Print 6](https://github.com/user-attachments/assets/c3b5dc2a-55a1-4e7a-af3f-307aa9476ecb)
![Print 7](https://github.com/user-attachments/assets/adc6e4db-0e4d-45b1-b2ff-eb120a91cf91)
![Print 8](https://github.com/user-attachments/assets/1a476da2-7714-4f97-8bb4-89ccb15c5e59)
![Print 9](https://github.com/user-attachments/assets/5f8d9859-a8ea-44be-8cb5-38a4f00a59b9)
![Print 10](https://github.com/user-attachments/assets/e1a24fb6-b278-4950-a614-6c818a046b8d)
![Print 11](https://github.com/user-attachments/assets/a6109f24-3ca7-48fe-ba4e-412434793d78)
