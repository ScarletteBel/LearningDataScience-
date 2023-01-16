
import numpy as np 
import statistics as stats


x = [154, 157, 187, 187, 149, 138, 145, 169, 167, 170,49,45,58,489, 34, 89, 38,40]


def mean(data):
    data_mean = np.mean(data)
    print("The mean is", data_mean)
    

def median(data):
    data_median = np.median(data)
    return data_median


def f(data):
    data_populat = stats.pvariance(data)
    return data_populat

def mode(data):
    data_mode = stats.mode(data)
    print("The mode is", data_mode)
    return data_mode


# This sort of result typically means that all values appear exactly the same number of times
# The mode is more beneficial when looking at discrete data, or categorical data.


def standard_deviation(data):
    data_sd = np.std(data)
    print("The standar deviation is ", data_sd)
    return data_sd

def percentile(no):
    pr_no = np.percentile(x, no, interpolation='midpoint')
    print("The percentile is ", pr_no)
    return pr_no

mean(x)
median(x)
f
f(x)
y = f(x)
print(y)
print(type(y))
# mode(data)

# standard_deviation(x)

# percentile(25)
# percentile(50)
# percentile(75)

