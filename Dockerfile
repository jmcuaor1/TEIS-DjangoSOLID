# 1. Usamos Python 3.12 porque Django 6.0.4 lo requiere
FROM python:3.12-slim

# 2. Evitamos archivos .pyc y buffer de logs
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 3. Directorio de trabajo dentro del contenedor
WORKDIR /app

# 4. Copiamos e instalamos dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiamos el código fuente
COPY . /app/

# 6. Comando para iniciar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]