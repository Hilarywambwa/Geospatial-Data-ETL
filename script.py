import requests
import pandas as pd
import geopandas as gpd
from shapely.geometry import LineString
from sqlalchemy import create_engine

## Define overpass QL query for roads in Nairobi
overpass_url = 'https://overpass-api.de/api/interpreter'

query = """
[out:json];
area[name="Nairobi"]->.searchArea;
(
  way["highway"="primary"](area.searchArea);
  way["highway"="secondary"](area.searchArea);
  way["highway"="residential"](area.searchArea);
);
out geom;
"""
# Send query to overpass API
response = requests.get(overpass_url, data = query)

data = response.json()
data.keys()

roads = data['elements']
type(roads)

sample_road = roads[0]

final_data=[]
for road in roads:
    road_data = {'id': road['id'], 'type': road['type']}
    road_data.update(road['tags'])
    coords = [(point['lon'],point['lat']) for point in road['geometry']]
    linestring = LineString(coords)
    road_data['geometry'] = linestring.wkt
    final_data.append(road_data)

df = pd.DataFrame(final_data)

df = df.drop(columns=[
       'access', 'lit', 'sidewalk', 'name:en', 'bicycle', 'created_by',
       'layer', 'source', 'foot', 'horse', 'note', 'narrow', 'fixme', 'junction:ref', 'alt_name',
        'cutting', 'FIXME', 'parking:both',
       'sidewalk:left', 'maxheight', 'motor_vehicle', 'mapillary',
       'survey:date', 'mtb:scale', 'complete', 'node', 'service', 'motorroad', 'covered', 'barrier',
       'incline', 'sidewalk:surface', 'maxspeed:advisory', 'name:sw',
       'amenity', 'segregated', 'trail_visibility', 'name:etymology:wikidata',
       'embankment', 'cycleway:both', 'source:date', 'ski', 'snowmobile',
       'addr:city', 'addr:housenumber', 'addr:street', 'tunnel', 'sac_scale',
       'safercity', 'check_date:smoothness', 'bridge:structure',
       'maxspeed:type', 'description', 'noname', 'proposed',
       'parking:right', 'bicycle_road', 'flood_prone', 'trolley_wire',
       'check_date', 'check_date:surface', 'via', 'internet_access',
       'short_name:en', 'website'])

engine = create_engine('postgresql://avnadmin:password@wambwa-wambwahilary-dfb2.f.aivencloud.com:20075/geospatial')

df.to_sql('nairobi_roads', engine, if_exists='replace',index=False,schema='nairobi')