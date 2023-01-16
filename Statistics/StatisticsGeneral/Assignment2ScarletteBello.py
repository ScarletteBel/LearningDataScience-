## Scarlette Bello Barron      c0860234


####### Q1 ########
## Affairs Data ###

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 1) Please state what each of the 9 variables are with respect to their type (refer to Week 1). Ex, continuous, nominal, etc [4.5 marks]

# 1. affairs: countinuous 
# 2. gender: nominal 
# 3. age: continuous 
# 4. yearsmarried: continuous 
# 5. children(yes or no): nominal 
# 6. religiousness: ordinal 
# 7. education: ordinal 
# 8. occupation: nominal
# 9. rating: ordinal 

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# The mean and media of the children column data can not be calculated because this is a nominal data type(yes/no), 
# no a numerical value; instead, the mean and media of the age is calculated 

import pandas as pd 
import numpy as np 
from scipy import stats
import matplotlib.pyplot as plt


data= pd.read_csv("Affairs.csv")
print(data)


def mean(data):
    data_mean = np.mean(data)
    print("The mean is", data_mean)
    return mean 

def median(data):
    data_median = np.median(data)
    print("The median is", data_median)
    return data_median

def trimmed_mean(data, percent):
    trimmed_data = stats.trim_mean(data , percent) 
    print(f"The trimmed meann of {percent*100} %: {trimmed_data}")
    return trimmed_data


def iqr(data):
    q3, q1 = np.percentile(data, [75 ,25])
    iqr = q3 - q1
    print(f'q3 is {q3}')
    print(f'q1 is {q1}')
    print(f"The IQR is: {iqr}")
    return iqr


mean(data.age)
median(data.age)
trimmed_mean(data.affairs, 0.10)
iqr(data.affairs)



# 7) Make a histogram of the affairs (label your axis and title name). What is the distribution like?

affairs_histog = data['affairs'].plot.hist()
plt.title('Affairs Histogram')
plt.xlabel('Affairs')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.75)
plt.show()

print('The Affairs Histogram has a right skewed distribution')

# 8) Make a boxplot for age. Are there any outliers ? 

age_boxplot = data['age'].plot(kind='box')
plt.show()
print('The Age boxplot shows lower and upper outliers')


