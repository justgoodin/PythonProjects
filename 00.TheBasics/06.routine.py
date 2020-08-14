import time
import os

filePath = "00.TheBasics/resources/files/veg.txt"
while True:
    if os.path.exists(filePath):
        with open(filePath) as file:
            print(file.read())
    else:
        print("File does not exist.")    
    time.sleep(10)