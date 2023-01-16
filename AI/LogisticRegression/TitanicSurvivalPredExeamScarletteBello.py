## Scarlette Bello Barron    c0860234


#Predicting survivers with the Titanic dataset
#Starting from importing the required libraries...

from email.utils import collapse_rfc2231_value
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import sklearn
from tabulate import tabulate

#Logistic regression model is going to be used for this prediction as ia a categorical one 

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

#Importing the Titanic data...

titanicFrame = pd.read_csv("titanic1.csv")
#titanic.columns = ['Survived', 'Pclass', 'Name', 'Sex',	'Age', 'Siblings/Spouses', 'Aboard', 'Parents/Children', 'Aboard', 'Fare']
print(titanicFrame)
print(titanicFrame.shape)
print(titanicFrame.columns)

#Cleaning the data, 

titanicdf = titanicFrame.drop(["Name","Unnamed: 8","Unnamed: 9"],axis="columns")
print(titanicdf.columns)
print(titanicdf)
print()

N = 1
titanicdff = titanicdf.iloc[:-N , :]
print(titanicdff)

dummies = pd.get_dummies(titanicdff['Sex']) 
print(dummies)

merged = pd.concat([titanicdff,dummies],axis="columns")
print(merged)

titanicdfff = merged.drop(["Sex", "female"],axis="columns")
print(titanicdfff)


#Defining variables and target values...
x = titanicdfff.drop("Survived",axis="columns")
y = titanicdfff.Survived 

print(x.shape)
print(y.shape)

## Now...let's go to split the data...
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.30)

print()
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

#Apliging the algorithm and checking the accuracy...

logistReg = LogisticRegression(max_iter=3200)
trainLogist = logistReg.fit(x_train,y_train) 

y_pred = logistReg.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print()
print("Accuracy is :", accuracy)


#Displaying the confusion matrix...
confMatrix = confusion_matrix(y_test, y_pred)
print(confMatrix)

##Computing correlation matrix to describe the dependence between all predictors...

corr = titanicdfff.corr()

sns.heatmap(corr)
plt.show()








