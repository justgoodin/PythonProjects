import json
import os

#Defile the path to the data file
filePath = os.path.dirname(__file__)+"/resources/data/data.json"
#Load the json data
data = json.load(open(filePath,"r"))

#function to match keys to values
def translate(word):
    if word.lower() in data:
        output = data[word]
    else:
        output = "The word does not exist"
    return output