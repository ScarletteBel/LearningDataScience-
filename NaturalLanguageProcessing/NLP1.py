#1. Reading the text
from asyncore import read
import csv

rawData = open("SMSSpamCollection.tsv")
read_data = csv.reader(rawData, delimiter="\t")

for row in read_data:
    print(row)

rawData.close()
print()

#2. Print the raw data 1st 200 charactors 
# rawData = open("SMSSpamCollection.tsv")
# read_data = csv.reader(rawData, delimiter="\t")

# from itertools import islice

# with rawData as myfile:
#     head = list(islice(myfile, 200))
# print(head)

# rawData.close()
# print()

# 3. replace and make a list 

rawData = open("SMSSpamCollection.tsv")
read_data = csv.reader(rawData, delimiter="\t")

# with read_data as f:
#     data = f.readlines()
#     for line in data:
#         line = line.replace(' ',',')
  
#         print(line)

# for row in read_data:
#     for row[2] in row:
#         rowLists = row[1].replace (' ',',')
#     print(rowLists)

# rawData.close()


