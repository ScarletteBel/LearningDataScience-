#Let´s calculate gross and net payment...

name, hours, payRate, taxes = input("Please enter your name, labor hours, pay rate and applied taxes: ").split()

hours, payRate, taxes = float(hours), float(payRate), float(taxes)

grossPay = payRate * hours
taxesPercent = taxes/100
netPay = grossPay - (grossPay*taxesPercent)

message = "Hi {}! your gross payment is {} and your net payment is {}".format(name, grossPay, netPay)

print(message)
