## Scarlette Bello Barron   c0860234

#Here we can skip one number...
dig = 15
while dig > 0:
    dig -= 1
    if dig == 7:
        continue
    print('The current value is:', dig)
print("Thanks!")

#multiple desicion...
print()
var = 4
if var == 200:
    print("1 - Got a true expression value")
    print(var)
elif var == 150:
    print("2 - Got a true expression value")
    print(var)
elif var == 100:
    print("3 - Got a true expression value")
    print(var)
else:
    print("4 - Got a false expression value")
    print(var)
print("Good bye!")

print()
amount =0
count = int(input("enter a number less than 10 :"))
if count < 10:
    while (count <10):
        count+= 1
        print("count", count)
else:
    print("You entered an invalid value")


