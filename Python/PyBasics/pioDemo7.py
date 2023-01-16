keyw = input("Enter the keyword you are looking for: ")#prompt the usr to enter a keyword to search for
f1 = open("C:\\Users\\r2kar\\Documents\\List of Internet Autonomous Systems.txt")
count=0
for line in f1:
    lineToList = line.split() # create a list out of the file
    if keyw in lineToList:
        print (lineToList)
        count+=1
print()
print(count)

