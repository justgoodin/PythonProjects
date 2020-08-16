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

html_style = """<h4>Volcano information:</h4>
Height: %s m
"""

for coordinate,el in zip(coordinates,elevation):
    iframe = folium.IFrame(html=html_style % str(el),width=175,height=100)
    fg.add_child(folium.Marker(location=coordinate,popup=folium.Popup(iframe),icon=folium.Icon(color='red')))

map.add_child(fg)
map.save(path+"/generated_maps/volcanoes.html")
