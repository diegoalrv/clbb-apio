import os
from django.core.management.base import BaseCommand

def delete_model_files(model_name, app_name='backend'):
    # Rutas de archivos
    model_file_path = os.path.join(app_name, 'models', f"{model_name}.py")
    serializer_file_path = os.path.join(app_name, 'serializers', f"{model_name}.py")
    view_file_path = os.path.join(app_name, 'views', f"{model_name}.py")
    
    # Lista de rutas de archivos
    file_paths = [model_file_path, serializer_file_path, view_file_path]

    # Eliminar los archivos si existen
    for file_path in file_paths:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Archivo {file_path} eliminado.")
        else:
            print(f"El archivo {file_path} no existe.")

    # Eliminar del admin
    admin_registration = f"admin.site.register({model_name})\n"
    admin_import = f"from {app_name}.models.{model_name} import {model_name}"
    admin_file_path = os.path.join(app_name, 'admin.py')
    if os.path.exists(admin_file_path):
        with open(admin_file_path, 'r') as admin_file:
            admin_content = admin_file.readlines()
        with open(admin_file_path, 'w') as admin_file:
            for line in admin_content:
                condition = (line.strip() != admin_registration.strip()) and (line.strip() != admin_import.strip())
                if condition:
                    admin_file.write(line)
        print(f"Eliminada la inclusión del modelo {model_name} en admin.py.")
    else:
        print(f"No se encontró el archivo {admin_file_path}.")

    # Eliminar de las urls
    urls_registration = f"router.register(r'{model_name.lower()}', {model_name}ViewSet)\n"
    urls_import = f"from {app_name}.views.{model_name} import {model_name}ViewSet"
    urls_file_path = os.path.join(app_name, 'urls.py')
    if os.path.exists(urls_file_path):
        with open(urls_file_path, 'r') as urls_file:
            urls_content = urls_file.readlines()
        with open(urls_file_path, 'w') as urls_file:
            for line in urls_content:
                condition = (line.strip() != urls_registration.strip()) and (line.strip() != urls_import.strip())
                if condition:
                    urls_file.write(line)
        print(f"Eliminada la inclusión del modelo {model_name} en urls.py.")
    else:
        print(f"No se encontró el archivo {urls_file_path}.")

    print(f"Eliminación del modelo {model_name} completada.")

class Command(BaseCommand):
    help = 'Elimina archivos y referencias asociadas a un modelo Django.'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Nombre del modelo.')
        parser.add_argument('app_name', type=str, default='backend', help='Nombre de la aplicación.')

    def handle(self, *args, **kwargs):
        model_name = kwargs['model_name']
        app_name = kwargs['app_name']
        delete_model_files(model_name, app_name)
