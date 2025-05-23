#!/bin/bash
echo "🚀 Iniciando DimDim App..."

# Criar rede se não existir
docker network create dimdim-network 2>/dev/null || echo "Rede já existe"

# Executar banco de dados
echo "📊 Iniciando banco de dados..."
docker run -d \
  --name dimdim-db \
  --network dimdim-network \
  -e POSTGRES_PASSWORD=senha123 \
  -e POSTGRES_DB=dimdimapp \
  -e POSTGRES_USER=dimdim \
  -v dimdim-data:/var/lib/postgresql/data \
  postgres:15 2>/dev/null || echo "Container do banco já existe"

# Aguardar banco inicializar
echo "⏳ Aguardando banco de dados..."
sleep 15

# Executar aplicação
echo "🌐 Iniciando aplicação..."
docker run -d \
  --name dimdim-application \
  --network dimdim-network \
  -p 5000:5000 \
  -e DATABASE_URL=postgresql://dimdim:senha123@dimdim-db:5432/dimdimapp \
  -e FLASK_ENV=production \
  dimdim-app 2>/dev/null || echo "Container da aplicação já existe"

echo "✅ DimDim App iniciado! Acesse: http://localhost:5000"
