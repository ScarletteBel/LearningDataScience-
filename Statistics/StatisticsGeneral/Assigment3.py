#Scarlette Bello Barron   KMeans clustering model....

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

import sklearn
from sklearn.preprocessing import scale 
import sklearn.metrics as sm 
from sklearn.metrics import confusion_matrix,  classification_report

from sklearn.cluster import KMeans
from mpl_toolkits.mplot3d import Axes3D 



# Implementing KMeans clustering model...

data = pd.read_csv('It_salary.csv')
print(data, '\n')

x = data['Age']
y = data['Salary']

plt.scatter(x, y)
plt.show()

data = list(zip(x, y))
print(data, '\n')


inertias = []

for i in range(1,21):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    inertias.append(kmeans.inertia_)

plt.plot(range(1,21), inertias, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.show()



# It is seen that the 'elbow' in the graph becomes more linear at k=2... 

kmeans = KMeans(n_clusters=2)
kmeans.fit(data)

plt.scatter(x, y, c=kmeans.labels_)
plt.show()



#Evaluating the results...

k_range = range(1,21)
sse = []
for k in k_range:
    clustering = KMeans(n_clusters=2)
    clustering.fit(data)
    sse.append(kmeans.inertia_)

plt.xlabel('k')
plt.ylabel('Sum of squared Error')
plt.plot(k_range,sse)
plt.show()



#The correct number of number of clusters is 2.