#Scarlette Bello Barron    0860234
#Trying with more string functions...
print(len("Dogs are incredible"))
print(len("Big Data"))
print(len("Big Data") + len("Dogs are incredible"))

word1 = "World"
word2 = "Peace to the world"
print(len(word1) == len(word2))

#Inclusion
print("h" in "hello")
print("Peace" in word2)
print("Peace" in word1)

#string indexing...
x = "hello word"
print(x[2])
#taking word of previous examples...
print(word2[-4])
print(x[-5])
print(x[-5] == x[5])

#Slicing...
longMessage = "You can analyze everywhere"
print(longMessage[0:9])
print(longMessage[3:5] == x[0:4])
print(x[2:5] == (longMessage[11]+longMessage[11]+longMessage[1]))
print(longMessage[11]+longMessage[11]+longMessage[1])
print(x[2:4])

#immutability...
#greeting = "hello"
#greeting[2] = "E"
#print(greeting)  returns error

