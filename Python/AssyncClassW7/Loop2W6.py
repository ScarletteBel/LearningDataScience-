##Scarlette Bello Barron    c0860234

# Continuing with for loops...

for i in range(10, 0, -2):
    print(i)

print()
for i in range(22, 6, -4):
    print(i)

print()
digits = "1234"
alphas = "abc"
for d in digits:
    for a in alphas:
        print(d+a)

#Something a little bit different but still for loop...
#Let's find the sum of all the numbers in a list...
print()
numbers = [2, 3, 5, 6, 78, 10]
sum = 0

for val in numbers:
    sum = sum + val
print("The sum is : ", sum)

#Iterating through a list...
print()
genre = ["salsa", "rock", "pop", "hip hop"]

for i in range(len(genre)):
    print("Music genre:", genre[i])

#Displaying student's marks...
print()
studentName = "Nancy"
marks = {"Jonas": 89, "Nancy": 88, "Luis":100}

for student in marks:
    if student == studentName:
        print(marks[student])


