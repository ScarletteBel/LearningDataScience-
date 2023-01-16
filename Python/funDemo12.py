#calculating the mpg
def calc_miles_gallon(themiles, thegallons):
    #mpg = 10 # this is a local var
    thempg = round ((themiles / thegallons), 2)
    #print (theMPG)
    return thempg #returns the result to the caller
def main():

    miles = float(input(" Enter miles: "))
    gallons = float(input(" Enter gallons: "))
    mpg = calc_miles_gallon(miles, gallons) # this is the caller
    #calc_miles_gallon(miles, gallons)
    print (mpg) # this is a local var
main() # the entry point for the interpreter