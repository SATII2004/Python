def show(n):
    if(n==0):       #base case
        return
    print(n)
    show(n-1)
    print("END")

print(show(5))


# factorial

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)

print(fact(6))

# sum of first n natural numbers

def calc_sum(n):
    if(n==0):
        return 0
    sum = calc_sum(n-1) + n
    return sum

print(calc_sum(3))

# printing list

l = ["scss", "ccef","fefve","dwdwrw","dwdodsjw","ddiwdjw","xxanscv","dwodwdwd"]

def print_list(list,idx=0):

    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

print(print_list(l))