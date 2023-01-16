## Scarlette Bello     c0860234

# •Implement Feature extraction using PCA with the following data.
# •array([[7, 6], [5, 2], [9, 8]])


import numpy as np 
import sklearn as kln 
import pandas as pd

from numpy import array
from sklearn.decomposition import PCA 

my_array = ([[7, 6], [5, 2], [9, 8]])
print(f'This is my array:\n {my_array}\n')

my_array_df = pd.DataFrame(my_array)
print(my_array_df)
print('\n')

pca = PCA(2)
pca.fit(my_array)

print(f'This are the pca components:\n {pca.components_}\n')
print(f'This is the explained variance:\n {pca.explained_variance_}\n')

transformed_array = pca.transform(my_array)
print(f'This is my array transformed:\n {transformed_array}\n')

