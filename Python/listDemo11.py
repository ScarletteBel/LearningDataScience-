info = ["Karim","Petros","Passas", "Anna", 'Aris', 'alha']
print(len(info))
print('Remove the first element.', info.pop(0))# removing the first elemnent using indexes
print(info)
print('Remove the last element.', info.pop())# pop removes the last element
print(len(info))
print(info)
popped = info.pop()#pop returns the removed element
print(popped)
print(info)
print('Remove the third element.', info.remove('Anna'))# remove: removes the element from the list but
                                                       # it does not return it
print(info)
'''
print('Remove the third element.', info.pop(2))# using indexes removing Anna
print(len(info))
print(info)
'''
'''
L=[1, 3, 2, 5, 6, 7, 4, 3 ,5, 8, 20, 5]
print (L)
L.append(20)
print(L)
print()
print('Remove the last element.', L.pop())
print(L)
print('Remove the 5th element.', L.pop(1))# remove the second element
print(L)
print('Remove the 5th element.', L.remove(5))'''