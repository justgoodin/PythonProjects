import os

#cur_path = os.path.dirname(__file__)
fileLocation =os.path.realpath("00.TheBasics\\resources\\files")

with open(fileLocation+"\\"+"fruits.txt","r") as fruitfile:
    content = fruitfile.read()

with open(fileLocation+"\\"+"veg.txt","w") as vegfile:
    vegfile.write("Tomato\nCucumber\nOnion\nPotato")
    vegfile.write("\nGarlic")

    print(content)