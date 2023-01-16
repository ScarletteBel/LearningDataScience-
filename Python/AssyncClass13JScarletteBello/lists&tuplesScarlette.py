#Scarlette Bello Barron 0860234
#Understanding differences between tuples and strings...

st = (1,2)
print(type(st))
#st[] = 234  Invalid becouse tuples like strings are inmutable

list = [2, 5, 5]
print(type(list))

list[0] = 40  #lists are mutable
print(list)

worldCountries = ["Mexico", "Canada", "China", "New Zeland"]
print(worldCountries)
print(worldCountries[1])
print(worldCountries[-1])
print(worldCountries[1:3])
print(worldCountries[:2])
print(worldCountries[1:])
print(worldCountries[-3:-1])
print()

#more examples...
animals = ["kangaroo", "fish", "dog", "panda", "tiger", "dolphin"]
animals[1] = "shark"
print(animals)
print()

#printing one by one and using more...
for x in animals:
    print(x)

if "kangaroo" in animals:
    print("Yes, kangaroo is in the animals list")

print(len(animals))
print()

#built-in list...
animals.append("puma")
print(animals)
animals.insert(1, "turtle")
print(animals)
animals.remove("dog")
print(animals)
animals.pop(4)
print(animals)

del animals[5]
print(animals)

animals2 = animals.copy()
print(animals == animals2)
print(animals2)
animals2.clear()
print(animals2)

listFinal = animals + worldCountries
print(listFinal)
del animals2
#print(animals2) this list does not exist, is not defined...
