f = open("demo.txt","r")

data = f.read()
daa = f.read(7)
dat = f.readline()  # reads data line by line


print(data)
print(daa)
print(dat)

print(type(data))

f.close()