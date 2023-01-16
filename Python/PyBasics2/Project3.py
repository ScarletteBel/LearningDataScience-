# Project3      Scarlette Bello    c0860234
# Linear regression implementation...


import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score



dataset = pd.read_csv('advertising.csv')
print(dataset)

x = dataset['TV'].values
y = dataset['Sales'].values

data_plot = plt.scatter(x,y, color = 'pink')
plt.show()


print(f"x values: \n{x}, \n")
print(f"y values: \n{y}, \n")

x = x.reshape(len(y),1)
y = y.reshape(len(y),1)



#Training and model...

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=1/3, random_state=2)

model = LinearRegression()

model.fit(x_train, y_train)
coef_model = model.coef_
model_intercept = model.intercept_

print(f'This is the model coeficient: {coef_model}\n')
print(f'This is the model interception: {model_intercept}\n')
print(f'Ecuation will be: Sales = {coef_model}*Tv + {model_intercept}\n')

model_evaluate =  model.score(x, y)
print(f"Model evaluation: {model_evaluate} \n")



# Predicting on test data...

y_pred = model.predict(x_test)
r2 = r2_score(y_test, y_pred)

print(f'This is the r2 score: {r2}\n')



#Training Data visualization....

plt.figure(figsize=(10, 8))
plt.scatter(x_train, y_train, color = 'blue')
plt.plot(x_train, model.predict(x_train), color = 'purple')
plt.title('Training data')
plt.xlabel('TV')
plt.ylabel('Sales')
plt.show()



#Testing Data visualization...

plt.figure(figsize=(10, 8))
plt.scatter(x_test, y_test, color = 'blue')
plt.plot(x_train, model.predict(x_train), color='green')
plt.title('Test data')
plt.xlabel('Hour')
plt.ylabel('Score')
plt.show()

