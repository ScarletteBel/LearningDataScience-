dict6 = {'Nabil':16,'Tanya':19, 'Rahul':51}
search = int(input('enter the age you search for: '))
for name, age in dict6.items():

    if age == search:
        print (name)
    else:
        print ('key is not found')
