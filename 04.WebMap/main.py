import folium
import os
from volcanoes import get_coordinates, get_elevation
from colorer import colour


path = os.path.dirname((__file__))
coordinates = get_coordinates()
max_lat = sum([item[0] for item in coordinates])/len(coordinates)
max_lon = sum([item[1] for item in coordinates])/len(coordinates)

elevation = get_elevation()
mean = sum(elevation)/len(elevation)  # To be used to compute color

# print(coordinates)
map = folium.Map(location=[max_lat, max_lon],
                 zoom_start=5, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")  # Feature Group for volcanoes

# To format popups
html_style = """<h4>Volcano information:</h4>
Height: %s m
"""

# Add children to volcanoe feature group
for coordinate, el in zip(coordinates, elevation):
    iframe = folium.IFrame(html=html_style % str(el), width=175, height=100)
    fgv.add_child(folium.CircleMarker(location=coordinate, radius=6, popup=folium.Popup(
        iframe), fill_color=colour(el, mean), color='grey', fill_opacity=0.9))

# Add childre to the population feature group
fgp = folium.FeatureGroup(name="Population")  # Feature Group for volcanoes
fgp.add_child(folium.GeoJson(data=(open(os.path.dirname(__file__)+"/resources/world.json", "r", encoding="utf-8-sig").read()),
                             style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
                                                       else 'orange' if 10000000 <= x['properties']['POP2005'] <= 25000000 else 'red'}
                             ))

map.add_child(fgv)
map.add_child(fgp)
# This needs to come after all layers are created
map.add_child(folium.LayerControl())
map.save(path+"/generated_maps/volcanoes.html")
