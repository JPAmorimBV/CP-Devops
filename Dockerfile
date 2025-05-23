# Usar imagem base Python Alpine para menor tamanho
FROM python:3.11-alpine

# Criar usuário não-root
ARG USERNAME=dimdim-user
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN addgroup -g $USER_GID $USERNAME \
    && adduser -u $USER_UID -G $USERNAME -D $USERNAME

# Instalar dependências do sistema para PostgreSQL
RUN apk add --no-cache postgresql-dev gcc musl-dev

# Definir diretório de trabalho
WORKDIR /app

# Configurar variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DATABASE_URL=postgresql://dimdim:senha123@dimdim-db:5432/dimdimapp \
    FLASK_ENV=production

# Copiar requirements e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código da aplicação e ajustar permissões
COPY --chown=$USERNAME:$USERNAME . .

# Definir usuário não-root
USER $USERNAME

# Expor porta
EXPOSE 5000

# Comando de execução
CMD ["python", "src/app.py"]
