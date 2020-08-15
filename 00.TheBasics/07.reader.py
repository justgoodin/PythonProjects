#Import libraries
import time
import os
import pandas

#Declate the path to the CSV file
filePath = "00.TheBasics/resources/files/today.csv"

while True:
    #Check if the file exists
    if os.path.exists(filePath):
        #import data using pandas
        data = pandas.read_csv(filePath)
        print(data.mean()["st1"])
    else:
        print("File does not exist")
    time.sleep(10)
    
