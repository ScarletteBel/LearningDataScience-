## Scarlette Bello Barron    c0860234

## Distinguish betwen one male and female voice !:D
## Starting from importing the data 

import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
import sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

csvFile = pd.read_csv("voice.csv")
print(csvFile)
print(csvFile.shape)

## Let's assign numerical values to the labels, male=0 & female=1...
dummies = pd.get_dummies(csvFile.label)
#print(dummies)

merged = pd.concat([csvFile,dummies],axis="columns")
#print(merged)

almostdf = merged.drop(["label","male"],axis="columns")
df = almostdf.rename(columns={"female":"gender"})

print(df)

x = df.drop("gender",axis="columns")
y = df.gender 

print(x.shape)
print(x.shape)

## Now...let's go to split the data...

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

print()
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)


logistReg = LogisticRegression(max_iter=3200)
trainLogist = logistReg.fit(x_train,y_train) 

y_pred = logistReg.predict(x_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)
print()
print("Accuracy is :", accuracy)

## Displaying the confusion matrix...
confMatrix = confusion_matrix(y_test, y_pred)
print(confMatrix)
#sns.heatmap(data = confMatrix)
#plt.show()

##Computing correlation matrix to describe the dependence between all predictors...

corr = df.corr()

sns.heatmap(corr)
plt.show()

##After analizing the correlation matrix...
## ..the carrelated variables chosen to delate are: median, Q25, centroid and dfrange..
## close the hetamap correlation matrix for keep runing the code 

x = df.drop("median",axis=1,inplace=True)
x = df.drop("Q25",axis=1,inplace=True)
x = df.drop("centroid",axis=1,inplace=True)
x = df.drop("dfrange",axis=1,inplace=True)

print()
print(df)

# Let's apply the logistic regrassion model to the modifed df (without correlated variables) to compare...

x = df.drop("gender",axis="columns")
y = df.gender 

print(x.shape)
print(x.shape)

## Now...let's go to split the data...

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

print()
print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(y_test.shape)

ogistReg = LogisticRegression(max_iter=3200)
trainLogist = logistReg.fit(x_train,y_train) 

y_pred = logistReg.predict(x_test)

print()
newAccuracy = accuracy_score(y_test, y_pred)
print()
print("Accuracy is :", newAccuracy)

newConfMatrix = confusion_matrix(y_test, y_pred)
print(newConfMatrix)

















