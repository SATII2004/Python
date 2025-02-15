dic = {
     321:"Satish",
     124:"neha",
     902:"mohut",
     438:"pintu"
 }

print(dic[321])

print(dic)

print(dic.keys())
print(dic.values())


for key in dic.keys():
    print(f"The value od corrsponding to key {key} is {dic[key]}")


print(dic.items())

ep={
    122:45,
    123:98,
    982:77,
    439:12
}

ep2={213:24,652:76}

ep.update(ep2)

print(ep)

# ep.clear()

ep.pop(123)

print(ep)