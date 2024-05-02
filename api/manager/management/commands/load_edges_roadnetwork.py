# backend/management/commands/load_nodes_roadnetwork.py

import os
from django.core.management.base import BaseCommand
from backend.models.RoadNetwork import Street, Node
import geopandas as gpd
import shapely

def load_edges_files(filename):
    print(filename)
    gdf = gpd.read_parquet(filename)
    gdf = gdf.to_crs(4326)
    print(gdf.head(3))
    # Iterar sobre cada fila y guardar en la base de datos Django
    for index, row in gdf.iterrows():
        geometry = row.geometry
        geom = shapely.LineString(geometry)
        # Verificar si la geometría es un punto con coordenadas (x, y)
        if isinstance(geom, shapely.LineString):
            
            # Convertir la geometría a EWKT (Extended Well-Known Text)
            geometry = geom.wkt
            # Buscar el nodo basado en el osm_id de origen (from)
            source_node = Node.objects.get(osm_id=row['from'])

            # Buscar el nodo basado en el osm_id de destino (to)
            destination_node = Node.objects.get(osm_id=row['to'])
            # Generar un hash aleatorio para el nombre
            # Crear instancia del modelo Street y guardar en la base de datos
            edge = Street(
                osm_id=row['osmid'],
                length=row['length'],
                source=source_node,
                destination=destination_node,
                geo_field=geometry,
            )
            edge.save()
    pass

class Command(BaseCommand):
    help = 'Load edges data to build road network'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str, nargs='?', default='/app/assets/road_actual_edges.parquet', help='Edges data filename')

    def handle(self, *args, **kwargs):
        filename = kwargs['filename']
        load_edges_files(filename)
        print('Finalizó')
