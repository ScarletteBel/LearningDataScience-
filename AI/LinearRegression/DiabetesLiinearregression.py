## Let's practice machine learning introduction concepts as linear regresion
## Diabates data set used...

import sklearn 
import pandas as pd 
from tabulate import tabulate
from sklearn import datasets 
from sklearn import svm 

diabetes = datasets.load_diabetes()
#print(diabetes)

columns = diabetes.feature_names
print(columns)
print(tabulate(diabetes.data))

#print(diabetes.target)
###print(diabetes.target_names)
#print(diabetes.DESCR)

x = diabetes.data
y = diabetes.target

xshape = x.shape
yshape = y.shape 

print(xshape)
print(yshape)

##Now...let's go to split the data 
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

print()
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

##let's go to model the linear regression!!!
from sklearn import linear_model 
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

model = linear_model.LinearRegression()
trainmodel = model.fit(x_train, y_train)

y_pred = model.predict(x_test)

##Linear regression model performance verifiers...
print()
print("Coeficients:",model.coef_)
print("Intercept:",model.intercept_)
print("Mean squared error (MSE): ", mean_squared_error(y_test,y_pred))
print("Coefficient of determination (R^2): ", r2_score(y_test,y_pred))

##Making a scatter plot....
import matplotlib.pyplot as plt
import seaborn as sns 

sns.scatterplot(x = y_test,y = y_pred, alpha = 0.5)
plt.show()





