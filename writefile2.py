f = open("demo.txt","r+") # r+ mode if we want to add at start

f.write("ndgrnifbrbrbt")

f.close()


import os

os.remove("sample.txt")
