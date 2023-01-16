#Scarlette Bello Barron    c0860234 
#Importing a xml file...

import xml.etree.ElementTree as ET 

xmlfile = 'Sample.xml'

tree = ET.parse(xmlfile)
root = tree.getroot()

ET.dump(tree)

#2.	Importing a JSON file and analyzing how different parts of JSON file can be parsed according to 
#   the business use case...

import pandas as pd 

filename = 'example_2.json'
df = pd.read_json(filename)
df.head()

print(df)
print()

# 3. Importing the breast cancer dataset from sklearn library and 
#    attach the target variable data to the features data and store it in a JSON file..

from sklearn.datasets import load_breast_cancer
from tabulate import tabulate 
import numpy as np
import json

data = load_breast_cancer()
columns = data.feature_names

print(tabulate(data.data))


print(data.target_names)
print(columns)

dataframe = pd.DataFrame(data=data.data, columns=data.feature_names)
dataframe['target'] = data.target
print(dataframe) 

predjson = dataframe.to_json(orient = 'table')

print(predjson)
print(type(predjson))


json_object = json.loads(predjson)

json_formatted_str = json.dumps(json_object, indent=2)

print(json_formatted_str)


file =open("testjson.json","w") 

with open('testjson.json', 'w') as f:
    f.write(json_formatted_str)



# 4. Make a regression dataset (500) with 7 features while having 
#    4 informative features and store them on disk in a csv file...

from sklearn import datasets 
from sklearn import linear_model 
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

diabetes = datasets.load_diabetes()
#print(diabetes)

columns = diabetes.feature_names
print(columns)
data = tabulate(diabetes.data)
print(data)

x = diabetes.data
y = diabetes.target

xshape = x.shape
yshape = y.shape 

print(xshape)
print(yshape)

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

print()
# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)

model = linear_model.LinearRegression()
trainmodel = model.fit(x_train, y_train)

y_pred = model.predict(x_test)


import csv

with open('regression.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(y_pred)

print(....)

import numpy as np
k=np.array([[1,2,3],[9,9,9]])
print(k.shape)




