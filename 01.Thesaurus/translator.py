import json
import os
from difflib import get_close_matches


filePath = os.path.dirname(__file__)+"/resources/data/data.json" #Defile the path to the data file
data = json.load(open(filePath,"r")) #Load the json data

'''
#function to match keys to values
def translate(word):
    if word.lower() in data:
        output = data[word.lower()]
        similar = False
    elif word.title() in data:
        output = data[word.title()]
        similar = False
    elif word.upper() in data:
        output = data[word.upper()]
        similar = False
    elif len(get_close_matches(word.lower(),data.keys())) > 0:
        output = get_close_matches(word.lower(),data.keys())[0]
        similar = True
    else:
        output = "The word does not exist"
        similar = False

    return [similar,output]
'''