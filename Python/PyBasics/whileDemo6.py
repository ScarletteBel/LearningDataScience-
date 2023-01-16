vowels = "aeiouAEIOU"
count = 0#counter initialization
while count < 5:# an expression
      v = input("Enter a vowel: ")
      if v in vowels:
            print ("found it")
            break
      count += 1# updating the counter
      print("That is not a vowel. Try again!")
      print()
print("Thank you!")