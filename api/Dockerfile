# Usa una imagen oficial de Python como imagen base
FROM python:3.9

# Set environment variables for Django
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos y lo instala
COPY requirements.txt .

# Instala dependencias necesarias para geodjango
RUN apt-get update \
    && apt-get install -y binutils libproj-dev gdal-bin libgdal-dev\
    && pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . /app/

# Expone el puerto que usa Django
EXPOSE 8001

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
# CMD ["ls"]
