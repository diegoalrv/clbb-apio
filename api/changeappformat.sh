#!/bin/bash

# Verificar que se haya proporcionado el nombre del proyecto
if [ $# -ne 1 ]; then
    echo "Uso: $0 <nombre_del_proyecto>"
    exit 1
fi

# Nombre del proyecto
APP_NAME=$1

# Crear estructura de carpetas
mkdir -p $APP_NAME/models
mkdir -p $APP_NAME/serializers
mkdir -p $APP_NAME/views

# Crear archivos __init__.py
touch $APP_NAME/models/__init__.py
touch $APP_NAME/serializers/__init__.py
touch $APP_NAME/views/__init__.py

# Crear archivo urls.py con contenido predeterminado
cat <<EOF > $APP_NAME/urls.py
# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
EOF

# Moverse al directorio del proyecto
cd $APP_NAME || exit

# Eliminar archivos innecesarios
rm models.py views.py

echo "Estructura de archivos y carpetas creada satisfactoriamente."
