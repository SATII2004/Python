from bisect import insort_right


def mul(i,j):
    return i*j

print(mul(23,34))

def add(k,l):
    print(f"Sum = {k+l}")

add(30,10)  #function call


def avg(a,b,c):
    average=(a+b+c)/3
    return average

output = avg(10,20,30)

print(output)

#print length of a list

cities = ["delhi","gurgaon","noida","mumbai","chennai","bhopal","amritsar","pune","satara","angul"]

def print_length(list):
    print(len(list))

print_length(cities)

def print_ele(list):
    print(list)

print_ele(cities)

print("###################")

print(cities[3], end=" ")
print(cities[7],end=" ")

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(cities)



#factorial of n
print( )

def factorial(n):
    fact=1
    for i in range(n,0,-1):
        fact *= i
    return fact

print(factorial(5))

#usd to inr

def curr_converter(usd_val):
    inr = 83 * usd_val
    return inr

print(curr_converter(1))


# check even or odd

def even_odd():
    n=int(input("Enter a number: "))
    if n%2==0:
        return "Even number"
    else:
        return "Odd number"

print(even_odd())