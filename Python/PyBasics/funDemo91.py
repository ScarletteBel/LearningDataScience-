def calc_gross(theHours, thePay_rate):
    gross_pay = theHours * thePay_rate
    print("The gross pay: ", gross_pay)
    calc_net(gross_pay)
    #the_net_pay = calc_net(gross_pay)
    #return the_net_pay

def calc_net(theGross):
    tax_rate = 0.13
    tax_amount = tax_rate * theGross
    print ("The tax amount: ", tax_amount)
    net_pay = theGross - tax_amount
    print("The net pay of the employee: ", net_pay)
    #return net_pay

def get_inputs():
    hours = float(input("Enter hours: "))
    pay_rate = float(input("Enter pay rate: "))
    return hours,pay_rate

def main():
    # using the returned hours and pay_rate
    hrs, p_rate = get_inputs()
    calc_gross(hrs, p_rate)
    #print("The net pay of the employee: ", calc_gross(hrs, p_rate))


main()