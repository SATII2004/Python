
#printing even numbers

for i in range(2,100,2):
    print(i)


num=(29,41,29,90,77,8,91,29,25)

for i in num:
    if i==77:
        print("Number found")
    else:
        print("Number not found")


# pass statement

for k in range(6):
    pass
print("Some useful work")



# factorial of first n numbers
n=5
fact= 1
for z in range(n,0,-1):
    fact *= z

print(fact)
