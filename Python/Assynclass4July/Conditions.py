## Scarlette Bello Barron   c0860234

#Just a liitle of conditions...
weight = float(input("How many pounds does your suitcase weigh? "))

if weight > 50:
    print("There is a $25 charge for luggage that heavy.")
else:
    print("All good, have a nice trip")
print("Thank you for your business.")


print()
hourlyWage = int(input("Please insert your hourly wage... "))
totalHours = int(input("How many hours have ypu worked in total? "))
overtime = int(input("Indicate your overtime hours: "))

if totalHours <= 40:
    totalWages = hourlyWage*totalHours
else:
    overtime = totalHours - 40

totalWages = hourlyWage*40 + (1.5*hourlyWage)*overtime
print("The total wage is ", totalWages)

print()
salary=int(input("enter a salary: "))
yearOnJob=int(input("Enter years of experience: "))
if salary>=3000:
    if yearOnJob>=3:
        print("You qualify for a loan")
    else:
        print("You qualify for a half of a loan")
    if yearOnJob>=10:
        print("You qualify for a half of a 25%% of a loan ")
else:
    print("You do not qualify for loans")




