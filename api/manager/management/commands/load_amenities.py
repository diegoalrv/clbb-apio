import geopandas as gpd
import hashlib
import uuid
import shapely
from django.contrib.gis.geos import Point
from backend.models.Amenity import Amenity

# Cargar los datos de GeoPandas
gdf = gpd.read_parquet('/app/assets/amenities_actual.parquet')
gdf = gdf.to_crs(4326)

# print(gdf)

# Función para generar un hash aleatorio
def generate_random_hash():
    unique_id = str(uuid.uuid4())
    return hashlib.sha256(unique_id.encode()).hexdigest()[:8]  # Tomamos los primeros 8 caracteres del hash

# Iterar sobre cada fila y guardar en la base de datos Django
for index, row in gdf.iterrows():
    geometry = row.geometry
    geom= shapely.Point(geometry.x, geometry.y)
    # Verificar si la geometría es un punto con coordenadas (x, y)
    if isinstance(geom, shapely.Point):
        
        # Convertir la geometría a EWKT (Extended Well-Known Text)
        geometry = geom.wkt
        
        # Generar un hash aleatorio para el nombre
        name = generate_random_hash()
        # Crear instancia del modelo Amenity y guardar en la base de datos
        amenity = Amenity(
            category=row['Category'],  # Usamos 'Category' para el campo 'category'
            name=name,  # Usamos el hash aleatorio para el campo 'name'
            geo_field=geometry
        )
        amenity.save()
    else:
        pass
        # print(f"La geometría en la fila {index} no es un punto válido con coordenadas (x, y)")
