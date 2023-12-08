# Usa una imagen base con Python y Flask
FROM python:3.8-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos necesarios
COPY . .

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto en el que la aplicación está escuchando
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["python3", "app.py"]
