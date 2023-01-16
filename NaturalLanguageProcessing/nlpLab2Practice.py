# import regex package
import re

re_test = 'This is a made up string to test 2 different regex methods'
re_test_messy = 'This      is /a made up     string /to test 2    different regex methods'
re_test_messy1 = 'This-is-a-made/up.string*to>>>>test----2""""""different~regex-methods'

#one single space
re_test_splited = re.split('\s', re_test)
print(re_test_splited)

 #One single space
re_test_messy_splited = re.split('\s', re_test_messy)
print(re_test_messy_splited)

 # add a + sign one or more space 
rere = re.split('\s+', re_test_messy)
print(rere)

# run the 3rd string set 
third = re.split('\s', re_test_messy1)
print(third)

 # W Searach for non word character -- can handle white space, a blackslash, quotes,period etc.
rew = re.split('\W+', re_test_messy1)
print(rew)
print()


pep8_test = 'I try to follow PEP8 guidelineW0s'
pep7_test = 'I try to follow PEP7 guidelines'
peep8_test = 'I try to follw1Wow PEEP80 guidelines'


# Any character between A-Z and 0-9 number
az_09 = re.findall('[A-Z]+[0-9]+' , peep8_test)
print(az_09)