f = open("demo.txt","r")


line1 = f.readline()  # reads data line by line
line2 = f.readline()


print(line1)
print("----------------------------------------------------------")

print(line2)
print("----------------------------------------------------------")

data = f.read()
daa = f.read(7)
print(type(data))
print(data)
print("----------------------------------------------------------")
print(daa)

f.close()
