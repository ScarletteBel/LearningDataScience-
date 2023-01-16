## Scarlette Bello Barron       c0860234
## Lasso Regression 


import numpy as np
import pandas as pd 
import sklearn 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import Lasso
from tabulate import tabulate
from sklearn import datasets 
from sklearn import svm 
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels as sm

diabetes = datasets.load_diabetes()

columns = diabetes.feature_names
print(columns)
print(tabulate(diabetes.data))

x = diabetes.data
y = diabetes.target

xshape = x.shape
yshape = y.shape 

print(xshape)
print(yshape)

#splitting the data ...
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

print()
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


# Lasso regression ...
model = Lasso()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)
print(y_pred.shape)

print(model.coef_)
print(model.intercept_)
print(model.score(x,y))



sns.regplot(y_test, y_pred, line_kws={'color':'red'}, ci=None)

plt.xlabel('Actual')
plt.ylabel('Predictions')
plt.title('Prediction vs Actual')
plt.show()



