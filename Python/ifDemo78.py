#check if age is greater than or equal to 65 or less than 12 then client gets a discount on the transition
age = int(input("Enter the age: "))
ticket = float(input("Enter the ticket price: "))
# below is what we call as nested if structure
if age > 0 and ticket > 0: # validating the value if age
    if age >= 65 or age < 12:# an inner if
        discountAmount = ticket * 35/100
        fare = ticket - discountAmount
    else:
        fare = ticket
    print('you are charge', fare)
else:
    print ('you have enterd an invlaid value')
    print('the program exits...')
