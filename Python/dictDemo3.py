#creating a new dictionary
myDict1 = {}
#adding entries to myDict1
myDict1['ibm']='12345'
myDict1['ibm-x']='23098'
myDict1['hp']='28764'
myDict1['dell']='09416'
print (myDict1)
# gettting the length of myDict1
print (len(myDict1))
print (myDict1.get('ibm','99988'))# the value provided here is the default
print ("myDict1 keys are: ",myDict1.keys())# retrieves all keys
k=myDict1.keys()
print(type(k))
k9=list(k)
print(type(k9))
print(k9[1])
print ("myDict1 values are: ",myDict1.values())# retrieves all values
print ("myDict1 entries are: ",myDict1.items())# retrieves all entries
myDict1.popitem()# removes the last entry
print (myDict1)
myDict1.pop('ibm-x')
print (myDict1)
