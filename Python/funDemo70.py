def input2Nums():
    num1=int(input("enter num1: "))
    num2=int(input("enter num2: "))
    return num1,num2 #returns multiple values

def sumNums(x,y):
    sum=x+y
    return sum

def main():
    thenum1,thenum2= input2Nums()
    result= sumNums(thenum1,thenum2)
    print('the sum is: ', result)

main()