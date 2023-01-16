#accessing a string or slicing a string using indexes
myStr1 = "python language" # the index of p is 0 ; the index of e is length of the string - 1
print('the length of myStr1 is: ', len(myStr1)) # use len function to return the length of a string
print (myStr1 [0])# p
print (myStr1 [2]) # t
print (myStr1 [-1])# this is the same as print (myStr1 [14]), it returns e, accssing the string backward
print (myStr1 [3:11])
print (myStr1 [:8])# a range, from 0 to 8 excluding 8
print (myStr1 [:8:3])# skip indexes by 2 >> 0 2 4 6
                    #0, 3, 6
print (myStr1 [:4]) # start from the beginning to index 4
print (myStr1 [8:])# start from 8 to the end
print (myStr1[1:4] + myStr1[7:])# concatenation of two strings using +, yth + language =ythlanguage
print (myStr1[1:4]+ "???"+ myStr1[7:])

print("raed"+"karim")
print("raed","karim")
print("raed","karim",sep='')
print("raed"+"karim")
print("raed","karim",sep='|',end='***')