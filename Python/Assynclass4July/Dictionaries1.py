## Scarlette Bello Barron   c0860234

#Starting with dictionaries...
#Built-in Functions and methods...

dict1 = {'Name':'Simon','Title':'Director','yOFeMJNF':14}

print(len(dict1))
print(str(dict1))
print(type(dict1))
print(dict1.copy())
print(dict1.get('Name'))
print(dict1.get('Title'))
print(dict1.items())
print(dict1.keys())
print(dict1.values())
print()

dict = {'a2':'3', 'k1':'89', 'z4':'5', 'd3':'0'}
sortedDict = sorted(dict.items())
for k,v in sortedDict:
    print(k, v)

list = {'Nabil':16,'Tanya':19}
search = int(input('Enter the age you search for: '))
for name, age in list.items():
    if age == search:
        print(name)
    else:
        print('key is not found')



