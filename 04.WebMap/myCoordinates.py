from geopy.geocoders import ArcGIS
import pandas
import os

gps = ArcGIS()

#file path declarations
dirname = os.path.dirname(__file__)
resources = "resources"
filename = "supermarkets.csv"

#read the file
data = pandas.read_csv(os.path.join(dirname,resources,filename))
data.set_index("ID",inplace=True)

#create a column with address & get geocodes
data["Full Address"] = data["Address"]+", "+data["City"]+", "+data["State"]+", "+data["Country"]
data["Geocode"] = data["Full Address"].apply(gps.geocode)
data["Coordinates"]  = data["Geocode"].apply(lambda x: [x.latitude,x.longitude] if x!=None else [None,None])
#print(data["Coordinates"])

def get_coordinates():
    return data["Coordinates"]