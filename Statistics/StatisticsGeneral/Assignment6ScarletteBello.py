# Scarlette Bello               c0860234
# K nearest neighbour 


import pandas as pd
import numpy as np 
import sklearn as skln
import matplotlib.pyplot as plt

from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix



data = pd.read_csv('mtcars.csv')
print(data,'\n')
print(data.shape)

empty = data.isnull().sum()
print(empty)

x=data.loc[:,['gear','carb']]
y=data.loc[:,'am']
x=preprocessing.scale(x)



x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.30,random_state=10)
print(x_train.shape)

model_knn =KNeighborsClassifier(n_neighbors=3)
model_knn.fit(x_train,y_train)

predict_train = model_knn.predict(x_train)
predict_test = model_knn.predict(x_test)
print('\n')



#Performance of the model on test data...
print(confusion_matrix(y_test,predict_test))
print('\n')
print(classification_report(y_test,predict_test))