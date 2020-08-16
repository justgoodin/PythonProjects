import folium
import os
from volcanoes import get_coordinates, get_elevation


path = os.path.dirname((__file__))
coordinates = get_coordinates()
max_lat = sum([item[0] for item in coordinates])/len(coordinates)
max_lon = sum([item[1] for item in coordinates])/len(coordinates)

elevation = get_elevation()
#print(coordinates)
map = folium.Map(location=[max_lat, max_lon], zoom_start=5,tiles = "Stamen Terrain")
fg = folium.FeatureGroup(name="My Map")


for coordinate,el in zip(coordinates,elevation):
    fg.add_child(folium.Marker(location=coordinate,popup=el,icon=folium.Icon(color='red')))

map.add_child(fg)
map.save(path+"/generated_maps/volcanoes.html")
