## Scarlette Bello Barron           c0860234

import pandas as pd
import sklearn as skln
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt
from sklearn.metrics import r2_score
from sklearn.metrics import classification_report, confusion_matrix



data = pd.read_csv('iris.data.csv')
print(data,'\n')
print(data.shape)

data['especie'] = pd.factorize(data['especie'])[0]
print(data)

description = data.describe().transpose()
print(description)

target_column = ['especie']
precistors = list(set(list(data.columns))-set(target_column))
data[precistors] = data[precistors]/data[precistors].max()
description1 = data.describe().transpose()
print(description1)



x = data[precistors].values
y = data[target_column].values

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=40)
print(x_train.shape); print(x_test.shape)



mlp = MLPClassifier(hidden_layer_sizes=(8,8,8,8), activation='relu', solver='adam', max_iter=500)
mlp.fit(x_train, y_train)

predict_train = mlp.predict(x_train)
predict_test = mlp.predict(x_test)



#Performance of the model on training data...
print(confusion_matrix(y_train,predict_train))
print(classification_report(y_train, predict_train))

#Performance of the model on test data...
print(confusion_matrix(y_test,predict_test))
print(classification_report(y_test,predict_test))


# The confusion matrix and the classification report show the performance of the model. 
# The performance of the training data and the test data are shown.
# The accuracy and the F1 on the training data are around 0.96 and 0.94 respectively.
# The perfect model would have a value of 1 in both values but it is not a real scenario.
# Nevertheless, the performance of the test data is, for accuracy and F1 equal to 1. 
# For this case it should be considered an overfitting possibility and a deeper analysis of the results and model


