# backend/management/commands/load_nodes_roadnetwork.py

import os
from django.core.management.base import BaseCommand
from backend.models.RoadNetwork import Street, Node, RoadNetwork
import geopandas as gpd
import shapely

def make_network(kwargs):
    network_name = kwargs['network_name']
    mode = kwargs['mode']
    # get all streets
    all_streets = Street.objects.all()
    
    # create network object
    road_network = RoadNetwork.objects.create(
        name=network_name,
        mode=mode,
    )
    
    # set() many-to-many relationship
    road_network.streets.set(all_streets)
    
    # return network
    return road_network


class Command(BaseCommand):
    help = 'build road network'

    def add_arguments(self, parser):
        parser.add_argument('network_name', type=str, nargs='?', default='ccp', help='Network name to identify')
        parser.add_argument('mode', type=str, nargs='?', default='walk', help='Which kind of network you are setting up (walk, car, bicycle, railway)')

    def handle(self, *args, **kwargs):        
        net = make_network(kwargs)
        net.save()
        print('Finalizó')
