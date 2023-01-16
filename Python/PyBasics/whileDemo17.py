#write a python program to calculate the avg of 5 sales
#make sure to get the sales from user

i = 0# a counter
sum = 0
while i < 5:# a condition
    sales = float(input("Enter the monthly sales amount: "))
    if sales < 0:# an invalid sale value
        continue
    sum = sum + sales
    i = i + 1 #updating the counter
avg = sum / i
print("the average is ", avg)
