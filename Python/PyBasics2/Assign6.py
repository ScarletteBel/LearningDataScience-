# Assignment 6     Scarlette Bello     0860234 
import string
from nltk.tokenize import word_tokenize
import nltk
import nltk.data
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer

# Use NLTK
# •Sample of text we are processing: •This movie made it into one of my top 10 most awful movies. Horrible. There wasn't a continuous minute where there wasn't a fight with one monster or another. There was no chance for any character development, they were too busy running from one sword fight to another. I had no emotional attachment ( except to the big bad machine ## that wanted to destroy them).
sample_text = "This movie made it into one of my top 10 most awful movies. Horrible. There wasn't a continuous minute where there wasn't a fight with one monster or another. There was no chance for any character development, they were too busy running from one sword fight to another. I had no emotional attachment ( except to the big bad machine ## that wanted to destroy them)."


# •Write python code to clean the above text using the textual data cleaning methods discussed earlier and implement all the strategies as functions.
def remove_punctuation(st):
    st1 = st.translate(str.maketrans ('', '', string.punctuation))
    print ('Without punctuation string: ', st1)
    return st1


def tokenize_sentence(st):
    st2 = word_tokenize(st)
    print(st2)
    return st2


def tokenize_word(st):
    nltk.download('punkt')   

    st3 = word_tokenize(st)
    print("Sample text tokenized by words: ", st3)
    print()
    return st3


def remove_stopwords(st2, st3):
    nltk.download('stopwords')

    stop_words = set(stopwords.words('english'))
    
    filtered_sentence = [w for w in st2 if not w.lower() in stop_words]
    filtered_sentence = []
    
    for w in st3:
        if w not in stop_words:
            filtered_sentence.append(w)

    st4 = filtered_sentence 
    print()
    print("Sample text without stopwords: ",st4)
    return st4


def stemming_text(st4):
    ps = PorterStemmer()

    st5 = []

    for w in st4:
        word_sec =  ps.stem(w)
        st5.append(word_sec)

    print()
    print("Steammed sample text: ", st5)
    return st5


def lemmatize(st4):
    nltk.download('wordnet')
    nltk.download('omw-1.4')

    lemmatizer = WordNetLemmatizer()

    st6 = []

    for w in st4:
        word_lem =  lemmatizer.lemmatize(w)
        st6.append(word_lem)

    print()
    print("Lemmatized sample text: ", st6)


# •Using the functions created for cleaning generate summary of the above data by applying TF/IDF scoring.
#TF-IDF ...
def tf(sample_text3):
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
    return my_dict


def shape(sample_text2):
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sample_text2)
    vectorizer.get_feature_names_out()

    print("The Tdidf shape is: ", X.shape)
    return X.shape


print("The saple tet is: ", sample_text)
print()

# sample_text1 = remove_punctuation(sample_text)
# sample_text2 = tokenize_sentence(sample_text1)
# sample_text3 = tokenize_word(sample_text1)
# sample_text4 = remove_stopwords(sample_text2, sample_text3)
# sample_text5 = stemming_text(sample_text4)
# sample_text6 = lemmatize(sample_text4)
# my_dict = tf(sample_text3)
# x_shape = shape(sample_text2)

print("............ ")