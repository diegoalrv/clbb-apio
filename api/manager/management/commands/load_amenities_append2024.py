from django.core.management.base import BaseCommand
import geopandas as gpd
from django.contrib.gis.geos import GEOSGeometry
from backend.models.Amenity import Amenity
import json

def load_data():
    # Cargar los datos de GeoPandas
    gdf = gpd.read_parquet('/app/assets/am_faltantes_090524_export_server/futuro.parquet')
    gdf = gdf.to_crs(4326)
    # gdf.drop_duplicates(inplace=True)
    return gdf

def upload_to_database():
    gdf = load_data()

    # Amenity.objects.all().delete()

    puntos = [
        Amenity(
            name=row['name'],
            category=row['category'],
            subcategory=row['subcategory'],
            geo_field=GEOSGeometry(json.dumps(row['geometry'].__geo_interface__))
        )
        for index, row in gdf.iterrows()
    ]

    Amenity.objects.bulk_create(puntos)
    pass


class Command(BaseCommand):
    help = 'Upload amenities to database'

    def add_arguments(self, parser):
        pass
        # parser.add_argument('', type=str, nargs='?', default='', help='Empty')

    def handle(self, *args, **kwargs):
        upload_to_database()
        print('Finalizó')


