## Assignment 1     Scarlette Bello    c0860234

import pandas as pd 
import random


test_grades = [['Rodrigo', 67], ['James', 45], ['John', 56], ['Michael', 90], ['Mary', 89], ['Patricia', 89], ['Jennifer', 99], [ 'Linda', 87], ['David', 45], ['Elizabeth', 78], ['Barbara', 56], ['William', 45], ['Richard', 78], ['Joseph', 61], ['Thomas',37], ['Charles',100], ['Susan',67], ['Jessica', 88], ['Sarah', 53], ['Karen', 87], ['Christopher', 99], ['Daniel', 76], ['Matthew', 41], ['Anthony',99], ['Mark',76], ['Lisa',66], ['Nancy',85], ['Betty', 98], ['Margaret',45], ['Sandra',73], ['Ashley', 100], ['Donald', 76], ['Steven',65], ['Paul', 78], ['Andrew',43], ['Joshua',76], ['Kenneth',35], ['Kevin',89], ['Brian',46], ['George',87], ['Timothy', 89], ['Kimberly',76], ['Emily',65], ['Donna',76], ['Michelle',65], ['Carol',76], ['Amanda',54], ['Dorothy',80], ['Melissa',54], ['Deborah', 38]]

df = pd.DataFrame(test_grades, columns=['Name', 'Grade'])
print(df)
print()


def convert_column_to_list():
    grade_list = df.Grade.values.tolist()
    return grade_list 


def choosing_random_grades():   
    i = 1
    rd_numbers_dict = {}
    while i < 11:
        i += 1
        numbers_content = random.randint(35,100)
        rd_numbers_dict[numbers_content] = 0
    return rd_numbers_dict


def freq_1(counter_dict, counted_list):
    for element in counted_list:
        if element in counter_dict.keys():
            counter_dict[element] += 1
    return counter_dict



my_grades_list = convert_column_to_list()
my_random_grades = choosing_random_grades()
frequency = freq_1(my_random_grades, my_grades_list)


df_calculation= pd.DataFrame(frequency.items(), columns=['Random grades', 'Frequency'])
df_calculation['Cumulative Frequency'] = df_calculation['Frequency'].cumsum()
df_calculation['Cumulative Percent'] = 100*(df_calculation['Cumulative Frequency'] / 50)
print(df_calculation)
print()


minimum_grade= df.min()
print('Minimum grade')
print(minimum_grade)
print()

first_quartile_grades = df.quantile([0.25])
print('First quartile')
print(first_quartile_grades)
print()

median_grades = df['Grade'].median()
print('Median')
print(median_grades)
print()

third_quartile_grades = df.quantile([0.75])
print('Third quartile')
print(third_quartile_grades)
print()

maximum_grade = df.max()
print('Maximum')
print(maximum_grade)
print()