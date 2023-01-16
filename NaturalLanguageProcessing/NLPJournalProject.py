import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

from sklearn import datasets 
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

import re
import nltk
nltk.download('punkt')
import nltk.data
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('omw-1.4')



data = datasets.fetch_20newsgroups()
print(data.target_names)

categories = ['alt.atheism', 'comp.graphics', 'comp.os.ms-windows.misc', 'comp.sys.ibm.pc.hardware', 'comp.sys.mac.hardware', 
                'comp.windows.x', 'misc.forsale', 'rec.autos', 'rec.motorcycles', 'rec.sport.baseball', 'rec.sport.hockey', 'sci.crypt', 
                'sci.electronics', 'sci.med', 'sci.space', 'soc.religion.christian', 'talk.politics.guns', 'talk.politics.mideast', 
                'talk.politics.misc', 'talk.religion.misc']

train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset = 'test', categories=categories)



#______1. read in-text data 
sample_text = train.data[5]
print(sample_text)



#_______2. format using regex and other tools, punctuation , tokenize, remove stop words
#   stem and lemmatize the data. 
# Removing punctuation....
puncts_removed = re.sub(r'[^\w\s]', '', sample_text)
print()
world_range = r'[0-9]'
sample_text1= re.sub(world_range, '', puncts_removed)
print("Sample text with no punctuations neither numbers:", sample_text1)
print()


#Tokenizing Sentence...
sample_text2 = re.findall('[A-Z][^A-Z]*', sample_text1)
print("Sample text tokenized by sentences: ", sample_text2)
print()

#Tokenizing word...
sample_text3 = word_tokenize(sample_text1)
print("Sample text tokenized by words: ", sample_text3)
print()

#Removing stopwords...
stop_words = set(stopwords.words('english'))
filtered_sentence = [w for w in sample_text3 if not w.lower() in stop_words]
filtered_sentence = []
  
for w in sample_text3:
    if w not in stop_words:
        filtered_sentence.append(w)

sample_text4 = filtered_sentence 
print()
print("Sample text without stopwords: ",sample_text4)


# Lemmatizing...
lemmatizer = WordNetLemmatizer()
sample_text6 = []

for w in sample_text4:
    word_lem =  lemmatizer.lemmatize(w)
    sample_text6.append(word_lem)

print()
print("Lemmatized sample text: ", sample_text6)




#_______3. Vectorizing data

cv = CountVectorizer()
cv_vector = cv.fit_transform(sample_text6)
print()
print(cv_vector.toarray())
print()



#_______4. Create and transform features 

x = datasets.fetch_20newsgroups()
y = cv_vector



#_______5. Select 2 algorithms and build 2 models
# First model is based in Multinomial Nayve Bayes.....
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

model.fit(train.data, train.target)
labels = model.predict(test.data)

mat = confusion_matrix(test.target, labels)
sns.heatmap(mat.T, square=True, annot=True, fmt='d', cbar=False, xticklabels=train.target_names, yticklabels=train.target_names)
plt.xlabel('true label')
plt.ylabel('predicted label')
plt.show()


# Second model is based on Random Forest....
# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20, random_state = 0)


# classifier=RandomForestClassifier(n_estimators =400,criterion="entropy",random_state =0)
# classifier.fit(x_train,y_train)

# y_pred = classifier.predict(x_test)


# cm2 = confusion_matrix(y_test, y_pred)
# print(cm2)




#_______6. make predictions & evaluate the results 

def  predict_category(s, train=train, model=model):
    pred= model.predict([s])
    print (train.target_names[pred[0]])
    return train.target_names[pred[0]]
    

predict_category('Jesus Christ')
predict_category('Hockey game')
predict_category('Ferrari is better than BMW')
predict_category('President of US')



