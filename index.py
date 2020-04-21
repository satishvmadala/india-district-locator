import sys
import json
from shapely.geometry import shape, Point

def district_info(arg1, arg2):
    d_info ={}
    #Construct a Point with arg input - arg1 should be longitude. arg2 should be latittude
    point = Point(float(arg1),float(arg2))
    # load GeoJSON file containing coords
    with open('india_dist.json') as f:
        js = json.load(f)
    for feature in js['features']:
        polygon = shape(feature['geometry'])

        if polygon.contains(point):
            location_data = feature['properties']
            d_info = {"State" : location_data['ST_NM'], "District": location_data['DISTRICT']}
            return d_info


if __name__ == '__main__':
    print(district_info(sys.argv[1], sys.argv[2]))
