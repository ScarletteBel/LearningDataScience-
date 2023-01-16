## Scarlette Bello Barron     c0860234

##Understanding functions better
def square(value1):
    square = value1 * value1
    return square
print(square(4))

def squareSum(valuex, valuey):
    squareSum = square(valuex) + square(valuey)
    return squareSum

print(squareSum(2, 4))


#A function that calls another one...
message = "Welcome to this calculor"
def printWelcome(message):
   return(message)

def futureValue():
    print(printWelcome(message))

    monthlyInvestment = float(input("Enter monthly investment: "))
    yearlyInterest = float(input("Enter yearly interest rate in %: "))
    years = float(input("Enter number of years: "))

    interests = (yearlyInterest/100)/12
    restingInterests = interests * monthlyInvestment
    realInvest = monthlyInvestment - restingInterests

    futureValuereal = realInvest
    futureMessage = "Future value:  "
    return futureMessage + str(round(futureValuereal, 2))

print(futureValue())

def main():
    choice = input("Do you want to continue? \n (y/n): ")
    if choice.lower() == "y":
        futureValue2 = futureValue()
        return futureValue2
    else:
        return "Bye!"

print (main())

