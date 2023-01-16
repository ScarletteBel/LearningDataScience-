fname= "Raed"
print(fname[3])#this prints d
print(len(fname))
print (fname.upper())
print (fname.lower())
print()
name ="Raed Karim"
print(name.replace('Raed','John'))

print (fname.startswith('r'))#checks if fname starts with 'r' and returns a bool value
print (fname.endswith('R'))
print (fname.endswith('d'))
print(fname.isalpha())#true
print('1234thrthr'.isalpha())#false
print('1234jhjg'.isdigit())#true, checks if '1234' is a digit

print('python class'.title())
print(' python class '.strip())
print('python class'.find("s"))#returns the index of the first occurance of s
msg='hello;class;how;are;you;doing'
words = msg.split(';')# words is a list
print (type(words))
print (words)
print(words[0])
print(words[-1])
print(words[3])
