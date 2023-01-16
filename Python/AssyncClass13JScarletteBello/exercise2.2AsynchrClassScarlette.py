#Scarlette Bello Barron 0860234
#Formatting operator
print("My name is %s and I am %d years old"%("Scar",25))
print("Hi %s. You have been assigned %i blue tests"%("Simon Donald", 13))
print()
#lists...
newList = ["July", 27, 1998, "yes", "Andres"]
subList = ["date", 14]
print(newList)
print(newList[0])
print(newList[2:4])
print(newList[2:])
print(newList*3)
print(newList + subList)
print()

#updating...
newList[4] = "happy"
print(newList)
print(len(newList))
#print(max(newList)) does not apply for this list
#print(min(newList)) does not apply for this list
print()

newList.append("Canada")
print(newList)
print(newList.count("Canada"))
newList.extend("247686")
print(newList)
print(newList.count("6"))
print(newList.index)
print(newList)
print(newList.pop(-1))
print(newList)
newList.remove(1998)
print(newList)
newList.reverse()
print(newList)
#print(newList.sort()) does not apply for this list



