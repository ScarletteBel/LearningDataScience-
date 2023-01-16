#Scarlette Bello Barron     0860234
#Q4

accountNumber = input("Hi! please provide us with your account number for giving you all your payment information: ")

#minutesUsed is a variable, depending on the customer minutes used...
minutesUsed = 386.0

if minutesUsed > 350:
    chargeFirstMin = 350 * 0.28
    chargeRemMin = (minutesUsed - 350) * 0.48
    minutesCharged = chargeRemMin + chargeFirstMin
else:
    chargeFirstMin = minutesUsed * 0.28
    chargeRemMin = 0
    minutesCharged = chargeFirstMin + chargeRemMin

chargeWithTaxes = minutesCharged + (minutesCharged * 0.13)
taxes = minutesCharged * 0.13

#Credit is a variable, also deoending on each customer's account...
credit = 34.0

if credit > 0:
    totalAmount = chargeWithTaxes - credit
else:
    totalAmount = chargeWithTaxes


print("%-45s%-9s"%("Costumer account number:", accountNumber))
print("%-45s%-9.2f"%("Minutes used:", minutesUsed))
print("%-45s%-9.2f"%("Charge for the first 350 minutes **$0.28:", chargeFirstMin))
print("%-45s%-9.2f"%("Charge for the remaining minutes **$0.48:", chargeRemMin))
print("%-45s%-9.2f"%("Taxes:", taxes))
print("%-45s%-9.2f"%("Credit:", credit))
print("%-45s%-9.2f"%("Total bill:", totalAmount))
