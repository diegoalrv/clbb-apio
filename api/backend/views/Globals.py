import zipfile
import os
import json
import tempfile
import geopandas as gpd
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.gis.geos import GEOSGeometry
from backend.forms.forms import UploadFileForm
from backend.models import Amenity, AreaOfInterest, DiscreteDistribution, GreenArea, LandUse
from django.http import HttpResponse

class UploadFileView(View):
    form_class = UploadFileForm
    template_name = 'upload.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            model_type = form.cleaned_data['model_type']
            self.handle_uploaded_file(file, model_type)
            return redirect('success')

        return render(request, self.template_name, {'form': form})

    def handle_uploaded_file(self, file, model_type):
        with tempfile.TemporaryDirectory() as tmpdirname:
            filepath = os.path.join(tmpdirname, file.name)
            with open(filepath, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            if zipfile.is_zipfile(filepath):
                with zipfile.ZipFile(filepath, 'r') as zip_ref:
                    zip_ref.extractall(tmpdirname)
                    for root, dirs, files in os.walk(tmpdirname):
                        for name in files:
                            if name.endswith('.shp'):
                                shp_path = os.path.join(root, name)
                                gdf = gpd.read_file(shp_path)
                                self.create_objects_from_gdf(gdf, model_type)
            elif filepath.endswith('.geojson'):
                gdf = gpd.read_file(filepath)
                self.create_objects_from_gdf(gdf, model_type)

    def create_objects_from_gdf(self, gdf, model_type):

        model_mapping = {
            'Amenity': Amenity.Amenity,
            'AreaOfInterest': AreaOfInterest.AreaOfInterest,
            'DiscreteDistribution': DiscreteDistribution.DiscreteDistribution,
            'GreenArea': GreenArea.GreenArea,
            'LandUse': LandUse.LandUse,
        }
        
        model_class = model_mapping.get(model_type)
        if not model_class:
            raise ValueError(f"Unsupported model type: {model_type}")
        
        objects_to_create = []

        if model_type == 'Amenity':
            objects_to_create = [
                model_class(
                    name=row['name'],
                    category=row['category'],
                    subcategory=row['subcategory'],
                    geo_field=GEOSGeometry(json.dumps(row['geometry'].__geo_interface__))
                )
                for index, row in gdf.iterrows()
            ]
        elif model_type == 'AreaOfInterest':
            objects_to_create = [
                model_class(
                    name=row.get('name', 'Unnamed'),
                    geo_field=GEOSGeometry(json.dumps(row['geometry'].__geo_interface__))
                )
                for index, row in gdf.iterrows()
            ]
        elif model_type == 'DiscreteDistribution':
            objects_to_create = [
                model_class(
                    name=row.get('name', 'Unnamed'),
                    dist_type=row.get('dist_type', ''),
                    code=row.get('code', ''),
                    level=row.get('level', 0),
                    geometry=GEOSGeometry(json.dumps(row['geometry'].__geo_interface__))
                )
                for index, row in gdf.iterrows()
            ]
        elif model_type == 'GreenArea':
            objects_to_create = [
                model_class(
                    name=row.get('name', 'Unnamed'),
                    category=row.get('category', ''),
                    subcategory=row.get('subcategory', ''),
                    tags=row.get('tags', {}),
                    geometry=GEOSGeometry(json.dumps(row['geometry'].__geo_interface__))
                )
                for index, row in gdf.iterrows()
            ]
        elif model_type == 'LandUse':
            objects_to_create = [
                model_class(
                    use=row.get('use', 'Unnamed'),
                    area=row.get('area', 0.0),
                    geometry=GEOSGeometry(json.dumps(row['geometry'].__geo_interface__))
                )
                for index, row in gdf.iterrows()
            ]

        if objects_to_create:
            model_class.objects.bulk_create(objects_to_create)
        pass

def success_view(request):
    return HttpResponse("Upload successful!")

import json
import tempfile
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.core.serializers import serialize
from forms.forms import DownloadFileForm
from models import Amenity, AreaOfInterest, DiscreteDistribution, GreenArea, LandUse

class DownloadFileView(View):
    form_class = DownloadFileForm
    template_name = 'download.html'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            model_type = form.cleaned_data['model_type']
            return self.download_file(model_type)

        return render(request, self.template_name, {'form': form})

    def download_file(self, model_type):
        model_mapping = {
            'Amenity': Amenity.Amenity,
            'AreaOfInterest': AreaOfInterest.AreaOfInterest,
            'DiscreteDistribution': DiscreteDistribution.DiscreteDistribution,
            'GreenArea': GreenArea.GreenArea,
            'LandUse': LandUse.LandUse,
        }

        model_class = model_mapping.get(model_type)
        if not model_class:
            raise ValueError(f"Unsupported model type: {model_type}")

        # Serializar los datos a GeoJSON
        data = serialize('geojson', model_class.objects.all())

        # Crear una respuesta HTTP con el archivo
        response = HttpResponse(data, content_type='application/json')
        response['Content-Disposition'] = f'attachment; filename={model_type}.geojson'
        return response
