## Scarlette Bello Barron     c0860234

def printingWelcome():
    return("Welcome to the real life")

print(printingWelcome())


message = "Welcome to this calculor"
def printWelcome(message):
   return(message)

print(printWelcome(message))


miles = 500
gallons = 14
def calculatingMilesGallon(drivenMiles, gallons):
    mpg = drivenMiles / gallons
    mpg = round(mpg,1)
    return mpg

print(calculatingMilesGallon(34,12))


def calcTax(amount, taxRate):
    tax = amount * taxRate
    return(tax)

print(calcTax(345,0.16))

def main():
    tax = calcTax(56, 0.16)
    message = "Tax: " + str(tax)
    return(message)

print(main())


globalTax = 0.20
def calcTax(amount, taxRate):
    totalAmount = amount * globalTax
    return(totalAmount)

print(calcTax(345, 0.6))








