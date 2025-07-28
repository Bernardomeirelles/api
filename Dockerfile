# Usa Python 3.11 oficial
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos do projeto
COPY . .

# Instala dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expõe a porta padrão do Streamlit
EXPOSE 8501

# Comando para rodar seu app
CMD ["streamlit", "run", "deskfy_app4.py", "--server.port=8501", "--server.enableCORS=false"]
