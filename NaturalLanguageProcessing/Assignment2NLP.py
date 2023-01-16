## Assignment 2 NLP  ----   Scarlette Bello Barron    c0860234

###Sample of text: 
###“         Jack and jill have made a delicious,       dish. Then they started to play some12 game! and jill attached the # [a] photo frame to the straight9 wall and swung on a sea-saw. She was very happy. After the game, they both went to central London to enjoy some fast food.“

sample_text = '“         Jack and jill have made a delicious,       dish. Then they started to play some12 game! and jill attached the # [a] photo frame to the straight9 wall and swung on a sea-saw. She was very happy. After the game, they both went to central London to enjoy some fast food.“'
print("The saple tet is: ", sample_text)
print()


# 1. Remove punctuation....
#Also numbers from words are removed
import re 

puncts_removed = re.sub(r'[^\w\s]', '', sample_text)
print()

world_range = r'[0-9]'
sample_text1= re.sub(world_range, '', puncts_removed)
print("Sample text with no punctuations neither numbers:", sample_text1)
print()


# 2. Tokenize Sentence...

sample_text2 = re.findall('[A-Z][^A-Z]*', sample_text1)
print("Sample text tokenized by sentences: ", sample_text2)
print()


#3. Tokenize word...

import nltk
nltk.download('punkt')
import nltk.data
from nltk.tokenize import word_tokenize

sample_text3 = word_tokenize(sample_text1)
print("Sample text tokenized by words: ", sample_text3)
print()


# 4. Remove stopwords...

from nltk.corpus import stopwords
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
  
filtered_sentence = [w for w in sample_text3 if not w.lower() in stop_words]
filtered_sentence = []
  
for w in sample_text3:
    if w not in stop_words:
        filtered_sentence.append(w)

sample_text4 = filtered_sentence 
print()
print("Sample text without stopwords: ",sample_text4)


# 5. Stemming text...

from nltk.stem import PorterStemmer
ps = PorterStemmer()

sample_text5 = []

for w in sample_text4:
    word_sec =  ps.stem(w)
    sample_text5.append(word_sec)

print()
print("Steammed sample text: ", sample_text5)


# 6. Lemmatize...

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

sample_text6 = []

for w in sample_text4:
    word_lem =  lemmatizer.lemmatize(w)
    sample_text6.append(word_lem)

print()
print("Lemmatized sample text: ", sample_text6)


# 7. Count vectorization...

from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()
cv_vector = cv.fit_transform(sample_text6)

print()
print(cv_vector.toarray())
print()


# 8. n-grams...
#n-gram range (2,2)...

from nltk import ngrams

sentence = 'Jack and jill have made a delicious dish'

n = 2
twograms = ngrams(sentence.split(), n)

new_arr = []

for elemento in twograms:
    new_string = f"{elemento[0]}  {elemento[1]}"
    new_arr.append(new_string)
print(new_arr)

#n-gram range (2,3)...
sentence = 'Jack and jill have made a delicious dish'

n = 3
threegrams = ngrams(sentence.split(), n)

new_arr1 = []

for elemento in threegrams:
    new_string1 = f"{elemento[0]}  {elemento[1]} {elemento[2]}"
    new_arr1.append(new_string1)
print(new_arr1)
print()


#9. TF-IDF ...

my_dict = {}
for word in sample_text3:
    if word in my_dict:  
        my_dict[word] += 1
    else:                
        my_dict[word] = 1

total_words = len(sample_text3)
for word in my_dict:
    my_dict[word] = round((my_dict[word] / total_words),2)


print("These are the TF of the words: ", my_dict)
print()


from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(sample_text2)
vectorizer.get_feature_names_out()

print("The Tdidf shape is: ", X.shape)
