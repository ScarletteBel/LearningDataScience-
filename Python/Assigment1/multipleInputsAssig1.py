# Entering multiple inputs in one statement and a little more ...

a, b, c = input("Please enter three numbers: ").split()
a, b, c = (float(a), float(b), float(c))

sum = a + b + c

print(a)
print(b)
print(c)

import math

print("testing modf: ",math.modf(a))
print("the largest number is: ", max(2,45,67))
print("the smallest number is: ", min(2,45,67))

#Checking the mof...
theModf = math.modf(a)
print(theModf)
print("the whole part is: ", theModf[1])
print("the fraction part is: ", theModf[0])

