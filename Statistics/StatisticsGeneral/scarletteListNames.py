name = 'Scarlette'

name1 = name[1:]+name[0]
name2 = name1[1:]+name1[0]
name3 = name2[1:]+name2[0]

print(name1)
print(name2)
print(name3)
print('..........................')

# repetir esa funcion hasta que el numeri de outpus sea = len(name )

for i in name:
    name = i 
    name = name[1:]+name[0]
    print(name)


# i = 1
# while i < len(name):
#     i = name[1:] + name[0]
#     print(i)
   
