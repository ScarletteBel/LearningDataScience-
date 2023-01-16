# Lab 5  -Simple Liner regression  


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import sklearn

from pylab import rcParams

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import scale 


2. 
%matplotlib inline
rcParams['figure.figsize'] = 10,8 



test = np.random.rand(100, 1)
test


test1 = test * 3 
test1

# rand function to generate number bewtween 0 - 1 : uniform distribtuon 
rooms = 3 * np.random.rand(100, 1)+ 3 


rooms[1:10]


# randn normal distribtuon 
test4 = np.random.randn(100,1)
test4


test5 = abs(test4)
test5


price = 275 + 6*rooms +abs(np.random.randn(100, 1))
price[1:10]

plt.plot(rooms,price, 'r^')
plt.xlabel("a number of Rooms, 2022 Average")
plt.ylabel("2022 Average home price ,1000s CAD ")

plt.plot(rooms,price, 'r^')
plt.xlabel("a number of Rooms, 2022 Average")
plt.ylabel("2022 Average home price ,1000s CAD ")

X = rooms
y = price 

lin_model = LinearRegression()
lin_model.fit(X,y)
print(lin_model.intercept_, lin_model.coef_)

# Simple Algebra
# y = mx + b
# b = intercept = 275.45
# Estimated Coefficients
# LinReg.coef_ = [6.08] Estimated coefficients for the terms in the linear regression problem.


print(lin_model.score(X,y))






