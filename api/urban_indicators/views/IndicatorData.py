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
from sqlalchemy import create_engine

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
        indicator_name = request.data.get('indicator_name')
        indicator_hash = request.data.get('indicator_hash')
        table_name = request.data.get('table_name')
        json_data = request.data.get('json_data')

        # Crear un objeto IndicatorData
        indicator_data = IndicatorData.objects.create(
            indicator_name=indicator_name,
            indicator_hash=indicator_hash,
            table_name=table_name
        )

        # Procesar y subir los datos JSON a la base de datos
        self.process_json_data(indicator_data, json_data)
        indicator_data.save()
        return Response({'message': 'Data saved successfully'})
    
    def process_json_data(self, indicator_data, json_data):
        db_url = get_db_url_from_env()
        engine = create_engine(db_url)
        json_data = json.loads(json_data)
        
        indicator_name=indicator_data.indicator_name
        indicator_hash=indicator_data.indicator_hash
        # table_name = f'{indicator_name}_{indicator_hash}'[:63]
        table_name = indicator_name[:63]

        if is_geojson(json_data):
            gdf = gpd.GeoDataFrame.from_features(json_data['features'])
            gdf['geometry'] = gdf['geometry'].apply(lambda x: GEOSGeometry(str(x)))
            gdf['hash'] = indicator_hash
            gdf.to_postgis(table_name, engine, if_exists='replace', index=False)
        else:
            df = pd.DataFrame(json_data)
            df['hash'] = indicator_hash
            df.to_sql(table_name, engine, if_exists='replace', index=False)
        pass

    @action(detail=False, methods=['get'])
    def get_table_data(self, request):
        table_name = request.query_params.get('table_name')
        indicator_hash = request.query_params.get('indicator_hash')

        table_data = self.query_table_data(table_name, indicator_hash)
        return JsonResponse(table_data, safe=False)

    def query_table_data(self, table_name, indicator_hash):
        db_url = get_db_url_from_env()
        engine = create_engine(db_url)
        sql_query = f"""SELECT * FROM "{table_name}" """
        if indicator_hash:
            sql_query+=f"""WHERE {table_name}.hash='{indicator_hash}' """
        df = pd.read_sql_query(sql_query, engine)
        print(df)
        return df.to_dict(orient='records')
