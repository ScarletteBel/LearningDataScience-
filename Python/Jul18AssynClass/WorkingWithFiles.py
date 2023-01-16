## Scarlette Bello Barron     c0860234

#Functions with read...
f = open("practicing.txt", 'r')
print(f.name)
print(f.read())
f.close()

#different way..
print()
with open("practicing.txt", 'r') as f:
    print(f.read())

with open("practicing.txt", 'r') as f:
    f_contents = f.readlines()
    print(f_contents)

with open("practicing.txt", 'r') as f:
    f_firstContent = f.readline()
    print(f_firstContent)

with open("practicing.txt", 'r') as f:
    for line in f:
        print(line, end='')


#Functions with append...
with open("practicing.txt", 'a') as f:
    f.write("3)Introducction to AI")

#Function with write...
with open("practicing2.txt", 'w') as f:
    f.write("Second file for practicing!!!")

