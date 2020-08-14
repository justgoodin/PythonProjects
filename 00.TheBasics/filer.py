import os

cur_path = os.path.dirname(__file__)
new_path = os.path.realpath("..\\PythonProjects\\resources\\fruits.txt")
myfile = open(new_path)

print(myfile.read())