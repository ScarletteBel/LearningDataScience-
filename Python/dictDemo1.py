myDict1 = {} # creating an empty dict
#adding pairs of key and values
myDict1 ['ibm'] = '12345'
myDict1 ['ibm-x'] = '1245-x'
myDict1 ['hp'] = '45678'
myDict1 ['asus'] = '56901'
print(len(myDict1))
print()
#retrieving the value of a key
print (myDict1['hp'])
#retrieving the value of a key using get
print (myDict1.get('ibm'))
del (myDict1['hp'])
print (myDict1.get('hp'))
#print (myDict1['hp'])
#print (myDict1['hp'])
print (myDict1)
myDict1.clear()# removing all pairs but myDict1 still exists
print (myDict1)