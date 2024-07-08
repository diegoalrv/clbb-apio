import pandas as pd
import geopandas as gpd
from django.contrib.gis.geos import GEOSGeometry
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from urban_indicators.models.IndicatorData import IndicatorData
from urban_indicators.serializers.IndicatorData import IndicatorDataSerializer
import json
from shapely import wkt
from shapely.geometry import Point
from sqlalchemy import create_engine
from django.db.utils import ProgrammingError

from django.db import connection
from rest_framework.decorators import action

def is_geojson(json_data):
    if isinstance(json_data, dict):
        if "features" in json_data or "FeatureCollection" in json_data:
            return True
    return False

def get_db_url_from_env():
    import os
    DB_CONTAINER_NAME = os.getenv('DB_CONTAINER_NAME', None)
    POSTGRES_USER = os.getenv('POSTGRES_USER', None)
    POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', None)
    POSTGRES_DB = os.getenv('POSTGRES_DB', None)
    DATABASE_URL = os.getenv('DATABASE_URL', None)
    return f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{DB_CONTAINER_NAME}:5432/{POSTGRES_DB}'

class IndicatorDataViewSet(viewsets.ModelViewSet):
    queryset = IndicatorData.objects.all()
    serializer_class = IndicatorDataSerializer

    @action(detail=False, methods=['post'])
    def upload_to_table(self, request):
        self.post_data_to_table(request)
        return Response({'message': 'Data saved successfully'})
    
    def post_data_to_table(self, request):
        indicator_name = request.data.get('indicator_name')
        indicator_hash = request.data.get('indicator_hash')
        self.is_geo = request.data.get('is_geo')
        print(self.is_geo)
        params = request.data.get('params')
        json_data = request.data.get('json_data')

        # Crear un objeto IndicatorData
        indicator_data = IndicatorData.objects.create(
            indicator_name=indicator_name,
            indicator_hash=indicator_hash,
            params=params,
            is_geo=self.is_geo,
        )
        # Procesar y subir los datos (Geo)JSON a la base de datos
        self.process_json_data(indicator_data, json_data)
        indicator_data.save()
        pass
    
    def process_json_data(self, indicator_data, json_data):
        db_url = get_db_url_from_env()
        engine = create_engine(db_url)
        json_data = json.loads(json_data)
        
        indicator_name=indicator_data.indicator_name
        indicator_hash=indicator_data.indicator_hash

        if self.is_geo:
            gdf = gpd.GeoDataFrame.from_features(json_data['features'])
            gdf['hash'] = indicator_hash
            gdf = gdf.set_crs(4326)
            gdf.to_postgis(indicator_name, engine, if_exists='append', index=False)
        else:
            df = pd.DataFrame(json_data)
            df['hash'] = indicator_hash
            df.to_sql(indicator_name, engine, if_exists='append', index=False)
        pass

    @action(detail=False, methods=['get'])
    def get_table_data(self, request):
        
        self.indicator_name = request.query_params.get('indicator_name')
        self.indicator_hash = request.query_params.get('indicator_hash')

        self.create_engine_db()
        self.get_is_geojson()
        self.create_query()
        self.query_table_data()
        
        return JsonResponse(self.table_data, safe=False)
    
    def get_is_geojson(self):
        # Obtener el campo específico de los elementos que cumplen con las condiciones
        queryset = IndicatorData.objects.filter(
            indicator_name=self.indicator_name,
            indicator_hash=self.indicator_hash
        ).values_list('is_geo', flat=True)

        # Convertir el queryset a una lista de valores
        field_values = list(queryset)
        print(field_values)
        self.is_geo = field_values[0]
        pass

    def create_engine_db(self):
        db_url = get_db_url_from_env()
        self.engine = create_engine(db_url)
        pass

    def create_query(self):
        self.sql_query = f"""SELECT * FROM "{self.indicator_name}" """
        if self.indicator_hash:
            self.sql_query+=f"""WHERE {self.indicator_name}.hash='{self.indicator_hash}' """
        pass

    def query_table_data(self):
        self.table_data = None
        if self.is_geo:
            gdf = gpd.read_postgis(self.sql_query, self.engine, geom_col='geometry')
            self.table_data = json.loads(gdf.to_json())
        else:
            df = pd.read_sql_query(self.sql_query, self.engine)
            self.table_data = df.to_dict(orient='records')

    @action(detail=False, methods=['post'])
    def update_indicator(self, request):
        indicator_name = request.data.get('indicator_name')
        indicator_hash = request.data.get('indicator_hash')

        self.delete_indicator(indicator_name, indicator_hash)
        self.post_data_to_table(request)

        return Response({'message': 'Indicator updated successfully'})
    
    def delete_indicator(self, indicator_name, indicator_hash):
        # Eliminar la entrada en IndicatorData
        indicator_data = IndicatorData.objects.filter(
            indicator_name=indicator_name,
            indicator_hash=indicator_hash
        ).first()
        if indicator_data:
            indicator_data.delete()

        # Comprobar si la tabla existe antes de intentar eliminar registros
        with connection.cursor() as cursor:
            cursor.execute("SELECT to_regclass(%s)", [indicator_name])
            if cursor.fetchone()[0]:
                # Si la tabla existe, ejecutar DELETE
                try:
                    cursor.execute(f"DELETE FROM \"{indicator_name}\" WHERE hash = %s", [indicator_hash])
                except ProgrammingError as e:
                    print(f"Error deleting data: {e}")
            else:
                print(f"Table {indicator_name} does not exist.")
