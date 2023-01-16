import re

re_test = 'This is a made up string to test 2 different regex methods'
re_test_messy = 'This      is a made up     string to test 2    different regex methods'
re_test_messy1 = 'This-is-a-made/up.string*to>>>>test----2""""""different~regex-methods'

# Splitting a sentence into a list of words...

re_test_split = re.split('\s', re_test)
print(re_test_split)
print()

#One single space...

onesp_retest = re.split('\s', re_test_messy)
print(onesp_retest)
print()

# add a + sign one or more space ... removes all the spaces....
edditing_plus = re.split('\s+', re_test_messy)
print(edditing_plus)
print()

exam = re.findall('\S+', "re test_messy1")
print(exam)

exam1 = re.split('\s', "I Love pYTHON prgramming")
print(len(exam1))

print(re.findall('[a-z]+', "I love big Data"))
print()
print(re.findall('[A-Z]+', "i like this Bigdata"))
print()
print(re.split('\s+', "I love big Data"))
print()
print(re.findall('\w+', "re test_messy1"))
print()
print(re.sub('[A-Z]+[0-9]+' , "PEP8 Python Regexguide", "peep8_test"))

print()
print(re.split('\s', "I Love pYTHON prgramming"))
print()
print(re.sub('[A-Z]+[0-9]+' , "PEP8 Python Regexguide", "peep8_test"))

print()
print(re.findall('[A-Z]+', "i like this Bigdata"))
print()
print(re.split('\s+', "I love big Data"))
print()
print(re.sub('[A-Z]+[0-9]+' , "PEP8 Python Regexguide", "peep8_test"))
print(re.findall('\S+', "re test_messy1"))
print(re.findall('[a-z]+', "I love big Data"))
print(re.split('\s+', "I love big Data"))
print(re.findall('\w+', "re test_messy1"))
print(re.findall('[A-Z]+', "i like this Bigdata"))