import geopandas as gpd
from django.contrib.gis.geos import GEOSGeometry
from backend.models.GreenArea import GreenArea
from shapely.geometry import Polygon

# Cargar los datos de GeoPandas
gdf = gpd.read_parquet('/app/assets/green_areas_future_export.parquet')
gdf = gdf.to_crs(4326)
# Función para convertir Polygon Z a Polygon
def convert_polygon_z_to_polygon(geometry):
    if geometry.type == 'Polygon':
        exterior = Polygon([xy[0:2] for xy in geometry.exterior.coords])
        interiors = [Polygon([xy[0:2] for xy in interior.coords]) for interior in geometry.interiors]
        return Polygon(exterior.exterior, [interior.exterior for interior in interiors])
    else:
        return geometry  # Retorna la geometría original si no es un Polygon

# Aplicar la función a cada geometría en la columna 'geometry'
gdf['geometry'] = gdf['geometry'].apply(convert_polygon_z_to_polygon)

print(gdf.head())
# Iterar sobre cada fila y guardar en la base de datos Django
for index, row in gdf.iterrows():
    geometry = row.geometry

    # Verificar si la geometría es un polígono con coordenadas (x, y)
    if isinstance(geometry, Polygon):
        
        # print(geometry.wkt)
        # Convertir la geometría a GEOSGeometry
        geometry = GEOSGeometry(geometry.wkt)
        # print(geometry)

        # Crear instancia del modelo LandUses y guardar en la base de datos
        green_area = GreenArea(
            name=row['name'],
            category=row['category'],
            subcategory=None,
            geometry=geometry,
        )
        green_area.save()
    else:
        print(f"La geometría en la fila {index} no es un polígono válido con coordenadas (x, y)")