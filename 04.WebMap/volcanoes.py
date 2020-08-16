from geopy.geocoders import ArcGIS
import pandas
import os

#file path declarations
dirname = os.path.dirname(__file__)
resources = "resources"
filename = "Volcanoes.txt"


gps = ArcGIS()
data = pandas.read_csv(os.path.join(dirname,resources,filename))

def get_coordinates():
    lat = list(data["LAT"])
    lon = list(data["LON"])
    coordinates = [(i,j) for i,j in zip(lat,lon)]

    return coordinates

def get_elevation():
    elevation = list(data["ELEV"])

    return elevation




