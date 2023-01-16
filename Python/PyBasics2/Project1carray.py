# Scarlette Bello Barron    c0860234
#Lab 1c    Pandas Python fatures 


#i. Create a one dimensional array (vector) iterate through all the elements and find the mean of the vector...
import numpy as np


array1 = [345, 678, 980, 234, 23, 133, 76]

sum_Array = sum(array1) 
mean = sum_Array/len(array1)

print(f'The mean of the vector array1 is: {mean}')
print()


#ii. Create a 3X3 array and find the sum of all elements in the second column
array_3d = np.array([
    [[34, 84, 99], [5, 6, 0], [789, 678, 564]],
    [[65, 79, 44], [7, 2, 3], [231, 562, 908]],
    [[11, 76, 45], [3, 9, 8], [543, 765, 980]], 
])

print(array_3d)
# print(array_3d.ndim)
# print(array_3d.shape)
print()

slice1 = array_3d[:3, 0:3, 1]

row1 = sum(slice1[0]) 
row2 = sum(slice1[1]) 
row3 = sum(slice1[2]) 

colum2_sum = row1 + row2 +row3

print(slice1)
print(f'The sum of the elemnts in the second column is: {colum2_sum}')
print()


#iii)	Create array using other standard methods like ones and empty by taking the zeros as reference...

a = np.arange(4)
a = a.reshape((2, 2))
print(a)
print()

array_zeros = np.zeros_like(a)
print(array_zeros)
print()


#i)	Get the diagonal elements and calculate the sum of all the diagonal elements...
my_matrix = np.matrix([[4,5,7,1],[6,7,9,2], [4,0,8,7], [5,9,2,1]]) 
print(my_matrix)

my_matrixdiag = my_matrix.diagonal()
print(f'The diagonal matrix is: {my_matrixdiag}')

sum_diag = np.sum(my_matrixdiag)
print(f'The sum of all the diagonal is: {sum_diag}')
print()


#ii)	Calculate the column wise and row wise mean of the created matrix...

column_means = my_matrix.mean(axis=0)
print(f'The column mean of my_matrix is : {column_means}')

row_means = my_matrix.mean(axis=1)
print(f'The row mean of my_matrix is : {row_means}')
print()


### Can we reshape the array into any shape? If not, then what are the cases?...

# It is possible to reshape the array but not in any way, just in the  way that the numeber of ellements allow it, 
# as long as, the reshaped array turned into a matrix can get complete rows and columns.


##4. Use arange and create a sequence of 6 numbers and try to reshape into all the possible ways and combinations...

arange_vec = np.arange(6)
print(arange_vec)

new_vec1 = arange_vec.reshape(2, 3)
new_vec2 = arange_vec.reshape(3, 2)
new_vec3 = arange_vec.reshape(6)

print(f'This is the vect reshaped in 2,3: {new_vec1}')
print()
print(f'This is the vect reshaped in 3,2: {new_vec2}')



