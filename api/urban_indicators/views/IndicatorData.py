import pandas as pd
import geopandas as gpd
from django.contrib.gis.geos import GEOSGeometry
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from urban_indicators.models.IndicatorData import IndicatorData
from urban_indicators.serializers.IndicatorData import IndicatorDataSerializer
from django.db import connection

class IndicatorDataViewSet(viewsets.ModelViewSet):
    queryset = IndicatorData.objects.all()
    serializer_class = IndicatorDataSerializer

    @action(detail=False, methods=['post'])
    def create_from_json(self, request):
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
        process_json_data(indicator_data, json_data)

        return Response({'message': 'Data saved successfully'})

def is_geojson(json_data):
    if isinstance(json_data, dict):
        if "features" in json_data or "FeatureCollection" in json_data:
            return True
    return False

def process_json_data(indicator_data, json_data):
    if is_geojson(json_data):
        # Convertir GeoJSON a GeoDataFrame
        gdf = gpd.GeoDataFrame.from_features(json_data['features'])

        # Subir el GeoDataFrame a la base de datos como PostGIS
        gdf['geometry'] = gdf['geometry'].apply(lambda x: GEOSGeometry(str(x)))
        gdf.to_postgis(f'indicator__{indicator_data.table_name}', connection, if_exists='append', index=False)
    else:
        # Convertir JSON a DataFrame
        df = pd.DataFrame(json_data)

        # Subir el DataFrame a la base de datos
        df.to_sql(f'indicator__{indicator_data.table_name}', connection, if_exists='append', index=False)

    # Se guarda el registro del IndicatorData
    indicator_data.save()