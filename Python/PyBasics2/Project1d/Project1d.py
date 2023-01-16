

#1.	Take a matrix and implement matrix multiplication logic using pandas apply function on each column to compute the result.

import numpy as np 
import pandas as pd 

matrix1 = np.matrix([[45, 78, 90, 23], [635, 879, 908, 675], [7, 6, 1, 5]])

matrix2 = np.matrix([[23, 78, 67], [54, 89, 89], [76, 11, 10], [23, 90, 18]])

def showing_df(mat):
    df = pd.DataFrame(data= mat)
dataFrame1 = pd.DataFrame(data=matrix1)
dataFrame2 = pd.DataFrame(data=matrix2)

print("Matrix1:")
print(dataFrame1)
print("Dimension:")
print(dataFrame1.shape)
print()

print("Matrix2:")
print(dataFrame2)
print("Dimension:")
print(dataFrame2.shape)
print()

matrix_multipl = dataFrame1.dot(dataFrame2)

print("Multiply: ")
print(matrix_multipl)
print()


#2.	Implement Merge sort logic using pandas DataFrames

values1 = {
    "Country": ["Mexico", "China", "Hong Kong"],
    "ID Number": [678, 980, 453]
}

values2 = {
    "Name": ['Simon', 'Naty', 'Sara'],
    "ID Number": [678, 980, 453]
}

df1 = pd.DataFrame(values1)
df2 = pd.DataFrame(values2)

print('Data Frame 1: ')
print(df1)
print()
print('Data Frame 2: ')
print(df2)
print()

df3 = df2.merge(right= df1, sort= True)
print(df3) 
print()


#3.	Import any csv file using Pandas and reindex the DataFrame. 
#Reshape the pandas DataFrame and store only data related to any 2 columns

import csv

print('Data Frame imported: ')

df = pd.read_csv (r'ProjectContent.csv')
print (df)
print()

print('Data Frame reindexed: ')

newidx = [2,1,3,5,4,6,7,0]
newdf = df.reindex(newidx)

print(newdf)
print()

x = np.array([[2,3,4], [5,6,7]])      
new_df1 = pd.DataFrame(np.reshape(df.to_numpy(),(4, 8)))

print(new_df1)
print()

print('Reshaped df, two columns: ')

dftwo_column = new_df1[[2, 4]]
print(dftwo_column)
print()


#4.	Implement changing index columns and row indexes in pandas

print("Changing index column: ")

df_i = new_df1.set_index(1)
print(df_i)
print()

df_ic = new_df1.set_index(7)
print(df_ic)


#............................................................................................
