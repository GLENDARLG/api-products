# Imagen base mínima
FROM python:3.10-slim

# Directorio de trabajo
WORKDIR /app

# Copiar dependencias y el código
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Exponer el puerto de la aplicación
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]
