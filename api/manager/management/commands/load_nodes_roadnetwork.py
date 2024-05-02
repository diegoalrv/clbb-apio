# backend/management/commands/load_nodes_roadnetwork.py

import os
from django.core.management.base import BaseCommand
from backend.models.RoadNetwork import Node
import geopandas as gpd
import shapely

def load_node_files(filename):
    print(filename)
    gdf = gpd.read_parquet(filename)
    gdf = gdf.to_crs(4326)
    print(gdf.head(3))
    # Iterar sobre cada fila y guardar en la base de datos Django
    for index, row in gdf.iterrows():
        geometry = row.geometry
        geom= shapely.Point(geometry.x, geometry.y)
        # Verificar si la geometría es un punto con coordenadas (x, y)
        if isinstance(geom, shapely.Point):
            
            # Convertir la geometría a EWKT (Extended Well-Known Text)
            geometry = geom.wkt
            
            # Generar un hash aleatorio para el nombre
            # Crear instancia del modelo node y guardar en la base de datos
            node = Node(
                osm_id=row['osm_id'],  # Usamos 'Category' para el campo 'category'
                geo_field=geometry
            )
            node.save()
    pass

class Command(BaseCommand):
    help = 'Load nodes data to build road network'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, nargs='?', default='/app/assets/road_actual_nodes.parquet', help='Nodes data filename')

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        load_node_files(filename)
        print('Finalizó')
