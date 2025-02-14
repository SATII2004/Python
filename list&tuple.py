from zipapp import create_archive

student = ["karan",98.3,14,"daman"]

print(student[0])

student[0]="arjun"

print(student[0])


marks=[23,53.69,37,71,52 ]

print(marks[1:4])

print(marks[-4:-1])

num=[34,234,10,921,134,623]
print(num)
num.append(4)
print(num)
num.sort()
print(num)

num.sort(reverse=True)
print(num)

num.reverse()
print(num)

num.insert(2,98)
print(num)

num.remove(10)
print(num)

num.pop(3)
print(num)


                      #TUPLES
tup=(29,41,29,90,77,8,91,29,25)

print(tup[0])

tup1=(1,)
print(tup1)
print(type(tup))

print(tup.index(8))

print(tup.count(29))

cars=[]

car1 = input("Enter 1st car name : ")
car2 = input("Enter 2nd car name : ")
car3 = input("Enter 3rd car name : ")

cars.append(car1)
cars.append(car2)
cars.append(car3)

print(cars)