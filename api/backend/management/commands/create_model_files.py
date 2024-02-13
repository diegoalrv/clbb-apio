# backend/management/commands/create_model_files.py

import os
from django.core.management.base import BaseCommand

def create_model_files(model_name, app_name):
    # Crear directorios si no existen
    model_directory = os.path.join(app_name, 'models')
    serializers_directory = os.path.join(app_name, 'serializers')
    views_directory = os.path.join(app_name, 'views')
    
    os.makedirs(model_directory, exist_ok=True)
    os.makedirs(serializers_directory, exist_ok=True)
    os.makedirs(views_directory, exist_ok=True)
    
    # Rutas de archivos
    model_file_path = os.path.join(model_directory, f"{model_name}.py")
    serializer_file_path = os.path.join(serializers_directory, f"{model_name}.py")
    view_file_path = os.path.join(views_directory, f"{model_name}.py")
    
    # Contenido predeterminado de los archivos
    model_content = f"""
from django.contrib.gis.db import models

class {model_name}(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
"""
    serializer_content = f"""
from rest_framework_gis import serializers
from {app_name}.models.{model_name} import {model_name}

class {model_name}Serializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = {model_name}
        fields = '__all__'
"""
    view_content = f"""
from rest_framework import viewsets
from {app_name}.models.{model_name} import {model_name}
from {app_name}.serializers.{model_name} import {model_name}Serializer

class {model_name}ViewSet(viewsets.ModelViewSet):
    queryset = {model_name}.objects.all()
    serializer_class = {model_name}Serializer
"""

    # Escribir en los archivos
    with open(model_file_path, 'w') as model_file:
        model_file.write(model_content.strip())
    with open(serializer_file_path, 'w') as serializer_file:
        serializer_file.write(serializer_content.strip())
    with open(view_file_path, 'w') as view_file:
        view_file.write(view_content.strip())

    # Agregar al admin y a las URL
    admin_registration = f"\nfrom {app_name}.models.{model_name} import {model_name}\n"
    admin_registration += f"admin.site.register({model_name})\n"
    url_inclusion = f"\nfrom {app_name}.views.{model_name} import {model_name}ViewSet\n"
    url_inclusion += f"router.register(r'{model_name.lower()}', {model_name}ViewSet)\n"
    with open(f'{app_name}/admin.py', 'a') as admin_file:
        admin_file.write(admin_registration)
    with open(f'{app_name}/urls.py', 'a') as urls_file:
        urls_file.write(url_inclusion)

    print(f"Archivos creados para el modelo {model_name} en la aplicación {app_name}:")
    print(f"- {model_file_path}")
    print(f"- {serializer_file_path}")
    print(f"- {view_file_path}")
    print("Agregado al admin y a las URL.")

class Command(BaseCommand):
    help = 'Crea archivos para un nuevo modelo Django.'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Nombre del modelo.')
        # parser.add_argument('app_name', type=str, help='Nombre de la aplicación.')

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name']
        # app_name = kwargs['app_name']
        app_name = 'backend'
        create_model_files(model_name, app_name)
