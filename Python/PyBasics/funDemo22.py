def sayHB(fName,lName):
    print("happt birthday to", fName,lName)

def main(): # calling sayHB from the main method
    fName1,lName1= input ("enter your name: ").split()
    fName2,lName2 = input ("enter your friend's name: ").split()
    print ("your name is :", fName1,lName1)
    print("your name is :", fName1, lName1)
    sayHB(fName1,lName1)
    sayHB(fName2, lName2)

main() # calling the main method to execute the program