# Usar una imagen base de Python 3.8 slim
FROM python:3.8-slim

# Establecer variables de entorno para evitar que se escriban archivos .pyc y para asegurarse de que la salida de pip sea legible
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establecer una carpeta de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de dependencias e instalarlas primero para aprovechar la cache de Docker
COPY requirements.txt .
RUN echo "🔧 Instalando dependencias..." && \
    pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos del proyecto al contenedor
COPY . .

# Crear un usuario no root para ejecutar la aplicación
RUN useradd appuser && chown -R appuser /app
USER appuser

# Exponer el puerto que utiliza la aplicación
EXPOSE 8081

# Comando para ejecutar la aplicación
CMD ["python", "main.py"]
