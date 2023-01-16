## Scarlette Bello Barron     c0860234

#Reading my text file as a list...
with open("Practicing.txt") as file:
    practicing = file.read()
    practicing_list = practicing.split(",")
    print(practicing_list)

#Reading each line of the file...
with open("Practicing.txt") as file:
    practice1 = file.readline();
    print(practice1, end="")
    practice2 = file.readline();
    print(practice2)
print()

#more...
with open("Practicing.txt") as file:
   fileContent = file.read(10)
   print(fileContent, end='')

print()
with open("Practicing.txt") as f:
    sizeToRead = 10
    fContent = f.read(sizeToRead)
    print(f.tell())

with open("Practicing.txt") as f:
    sizeToRead = 10
    fContent = f.read(sizeToRead)

    while len(fContent) > 0:
        print(fContent, end='')
        fContent = f.read(sizeToRead)




