## Scarlette Bello Barron   c0860234

#General while loop structure...
amount = 0
count = 12
while(amount<=10000 and count<10):
    amount+=100
    count=+1
    print(count)

#For loop example with else...
print()
letterSearched = input("Insert the letter you are looking for: ")
for letter in "English":
    if letter == letterSearched:
        print("There is letter: ", letter)
        break
else:
    print("I can not find a match letter")

#Comparing with while with else...
limit = 1000
interest = 0.1
balance = float(input("enter a balance: "))
while balance < limit:
    balance = balance + balance * interest
    print('the balance is now: ', balance)
    break
else:
    print("balance is greater than limit")

#more...
letterSearch = input("Insert the letter that you want to find :")
for letter in "German":
    if letter == letterSearch:
        print("That letter exists in the word!")
        break
else:
    print("I didn't find that letter")


