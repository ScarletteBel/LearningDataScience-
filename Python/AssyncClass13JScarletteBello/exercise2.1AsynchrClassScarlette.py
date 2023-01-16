#Scarlette Bello Barron 0860234
#Strings and slices ...
myString = "Lambton first term"
print(myString)
print(myString[0])
print(myString[-5])
print(myString[-5] == myString[4])
print(myString[-5] == myString[8])
print(myString[-5] == myString[14])
print(myString[2:11])
print(myString[0:4] + myString[8:13] + myString[14:-1])
print(myString*2)
print(myString + " 2022")
print()

#Escape characters
print("Update String:", myString[6] + "String")
print("Update String:", myString[:6] + "String")
print("Updated String\a",myString[:6]+"String")
print("Updated String\b",myString[:6]+"String")
print("Updated String\n",myString[:6]+"String")
print("Updated String\t",myString[:6]+"String")


