# Use uma imagem base oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Instale dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copie o conteúdo do projeto para o diretório de trabalho
COPY . .

# Defina variáveis de ambiente
ENV DJANGO_ENV=production

# Execute as migrações do Django e colete arquivos estáticos
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Exponha a porta que a aplicação usará
EXPOSE 8000

# Defina o comando para rodar o servidor Gunicorn
CMD ["gunicorn", "gerenciador.wsgi:application", "--bind", "0.0.0.0:8000"]
