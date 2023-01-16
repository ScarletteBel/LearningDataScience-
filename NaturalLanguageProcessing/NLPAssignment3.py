# Scarlette Bello Barron            c0860234
# Assignment 3 

import nltk
import pandas as pd 
import numpy as np
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_fscore_support as score
from sklearn.metrics import confusion_matrix
import tensorflow as tf
from tensorflow import keras
from tensorflow import Sequential as sc
from tensorflow import layers
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout
import gensim, warnings
from gensim.models import Word2Vec
import string



X_train = pd.read_csv('X_train.csv')
X_test = pd.read_csv('X_test.csv')
y_train = pd.read_csv('y_train.csv')
y_test = pd.read_csv('y_test.csv')

print(X_train.head)



#1. Create TF-IDF Vectors & Fit RandomForestClassifier On Top Of Vectors 

tfidf_vect = TfidfVectorizer()
X_tfidf = tfidf_vect.fit_transform(X_train)
print(X_tfidf.shape)
print(tfidf_vect.get_feature_names())



rf = RandomForestClassifier(n_estimators=50, max_depth=20, n_jobs=-1)
rf_model = rf.fit(X_train, y_train)

sorted(zip(rf_model.feature_importances_, X_train.columns),  reverse =True) [0:10]

y_pred = rf_model.predict(X_test)

precision, recall, fscore, support = score(y_test,y_pred, pos_label ='spam', average ='binary')
print('Precision: {} / Recall: {} / Accuaracy: {}'.format(round(precision, 3),
                                                          round(recall, 3),
                                                          round((y_pred==y_test).sum() / len(y_pred),3)))




#2. Create word2vec Vectors

model_w2v = gensim.models.Word2Vec(X_test, min_count = 1,vector_size = 100, window = 5)
X_test1 = model_w2v.wv.similarity(X_test)
X_train1 = model_w2v.wv.similarity(X_train)



rf = RandomForestClassifier(n_estimators=50, max_depth=20, n_jobs=-1)
rf_model = rf.fit(X_train1, y_train)

sorted(zip(rf_model.feature_importances_, X_train1.columns),  reverse =True) [0:10]

y_pred = rf_model.predict(X_test1)

precision, recall, fscore, support = score(y_test,y_pred, pos_label ='spam', average ='binary')
print('Precision: {} / Recall: {} / Accuaracy: {}'.format(round(precision, 3),
                                                          round(recall, 3),
                                                          round((y_pred==y_test).sum() / len(y_pred),3)))




# 3. Create doc2vec Vectors 


warnings.filterwarnings(action = 'ignore')

def tagged_document(test):
   for i, list_of_words in enumerate(test):
      yield gensim.models.doc2vec.TaggedDocument(list_of_words, [i])
    

tagged_document(X_train)
tagged_document(X_test)


rf = RandomForestClassifier(n_estimators=50, max_depth=20, n_jobs=-1)
rf_model = rf.fit(X_train1, y_train)

sorted(zip(rf_model.feature_importances_, X_train1.columns),  reverse =True) [0:10]

y_pred = rf_model.predict(X_test1)

precision, recall, fscore, support = score(y_test,y_pred, pos_label ='spam', average ='binary')
print('Precision: {} / Recall: {} / Accuaracy: {}'.format(round(precision, 3),
                                                          round(recall, 3),
                                                          round((y_pred==y_test).sum() / len(y_pred),3)))




#4.Build And Evaluate RNN

regressor = sc()
regressor.add(LSTM(units=50, return_sequences = True, input_shape = (X_train.shape[1], 1)))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units=50, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.2))


regressor.add(Dense(units=1))
regressor.complile(optimizer = 'Adam', loss='mean_squared_error')


regressor.fit(X_train, y_train, epochs=100, batch_size=32)
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
print(X_test)

predicted = regressor.predict(X_test)
predicted = sc.inverse_transform(X_test)
print(predicted)




# 5. compare the results(key value metrics)
 
# a)summarize all technique's results.    b)explain which technique is best and why ? 


#The results between the techniques are different. All the results and behaviour of the techniques applied changed because
#      each technique it is better for certain problem to solve. In the case of TF-IDF, it it is useful when the signal in the dataset
#      for making predictions is unknown, as is this project. Gives more wigh to words that appear in a few documents and, it is usefull
#      for compare full documents or categorized them. 
#      The Word2Vec transforms each word as a vector and considers scale and it impacts deppending of the vocabulary. 
#      The Doc2Vec technique transforms each document and it learn the meaning of the underlying words without considering the distance between vectors.
#      RNN on the other side is better for sequence predictions .