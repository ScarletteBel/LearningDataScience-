# Project 2a    Scarlette Bello Barron   c0860234



##Use Pandas 
##1.Use flights.csv dataset to fill the missing values using the Interpolation of data in all the columns...

import pandas as pd 
import numpy as np

df_flights_lenc = pd.read_csv('flights.csv')
print(df_flights_lenc)
print()

newdf_flights = df_flights_lenc.fillna(22, axis='columns')
print(newdf_flights)
print()
print()


##2.Apply one hot encoding to the Industry column in the salary.csv file which is used in One hot encoding practice slides...

df_salary_lenc = pd.read_csv('salary.csv')
print(df_salary_lenc)
print()

df_salary_inddumm = pd.get_dummies(df_salary_lenc, columns=['Industry'])
print(df_salary_inddumm)
print()


##3.Apply Label encoder for both country and industry column for salary.csv dataset...

df_salary_cat = df_salary_lenc['Country'].astype('category')
df_salary_lab = df_salary_cat.cat.codes 
print(df_salary_lab)
print()


##4.Discretize the data into different age bins using the salary dataset Age column...

df_salary_bin = pd.cut(x=df_salary_lenc['Age'], bins=[0,14,24,64,100])
print(df_salary_bin)
print()
print()




## Use ScikitLearn
## 1.In the attached sample.csv dataset fill the missing values using the Interpolation of data in all the columns

from numpy import nan
# from sklearn import imputer
from sklearn.impute import SimpleImputer

df_salary = pd.read_csv('sample.csv')
print(df_salary.columns)
print(df_salary)
print()

no_missvalues = df_salary['Age'].isna().sum()
print(no_missvalues)
print(type(df_salary['Age']))
print()

df_sample_num = df_salary['Age'].astype(float)
imp = SimpleImputer(strategy='mean')
data_age = imp.fit_transform(df_sample_num.values.reshape(-1, 1) )
print(df_sample_num.isna().sum())
print()
print()


##2.Apply one hot encoding to the Industry column in the salary.csv file which is used in One hot encoding practice slides...

import sklearn as sklrn 
from sklearn.preprocessing import OneHotEncoder

print(df_salary_lenc)
print()

ohe = OneHotEncoder()
df_sal_transformed = ohe.fit_transform(df_salary_lenc[['Industry']])
print(df_sal_transformed.toarray())
print()
print()


## 3.Apply Label encoder for both country and industry column for salary.csv data...

from sklearn.preprocessing import LabelEncoder

country_types = df_salary_lenc['Country']
print(country_types)
industry_types = df_salary_lenc['Industry']
print(industry_types)
print()


convert_country_objct = tuple(df_salary_lenc['Country'].tolist())
print(convert_country_objct)

convert_industry_objct = tuple(df_salary_lenc['Industry'].tolist())
print(convert_industry_objct)
print()

lab_coun_df = pd.DataFrame(convert_country_objct, columns=['Country'])
print(lab_coun_df)
lab_ind_df = pd.DataFrame(convert_industry_objct, columns=['Industry'])
print(lab_ind_df)
print()

encoder = LabelEncoder()

values_coun = encoder.fit_transform(lab_coun_df['Country'])
values_ind = encoder.fit_transform(lab_ind_df['Industry'])

print(values_coun)
print(values_ind)