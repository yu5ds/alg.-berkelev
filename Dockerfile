# Usar imagen base de Python
FROM python:3.10

WORKDIR /app
COPY . /app

CMD ["python", "berkeley_server.py"]
