# Trying with some practice...

lastName = "Luisini"

grade1 = 42
grade2 = 32
grade3 = 45.2

avg = (grade1 + grade2 + grade3)/3

print(lastName)
print("your average is: ", round(avg,3))

if avg >= 50:
    newAvg = avg + (avg * 0.10)
    print("your new ang is: ", newAvg)
    print("congrats! you pass")
else:
    print("You fail, and must repeat the course :(")
print()
print("Thanks!")



