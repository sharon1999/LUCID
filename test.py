from textblob import TextBlob
import pickle
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
import re

def cleaning(x):
    inp = [x.lower()]

    #Sentence TOkenizer
    sentence_token=[]
    for sent in inp:
        sent=sent_tokenize(sent)
        sentence_token.append(sent)

    # Word Tokenize
    word_token=[word_tokenize(i) for i in inp]


    #Remove Special Characters
    word_token_1=[]
    for words in word_token:
        clean=[]
        for w in words:
            res=re.sub(r'[^\w\s]',"",w)
            if res!="":
                clean.append(res)
        word_token_1.append(clean) 
 

    # Remove Stop Words
    clean_text_4=[]
    for words in word_token_1:
        w=[]
        for word in words:
            if not word in stopwords.words('english'):
                w.append(word)
        clean_text_4.append(w)
    


    # Lemmatization
    lem=[]
    for words in clean_text_4:
        w=[]
        for word in words:
            w.append(wordnet_lemmatizer.lemmatize(word, pos="v"))
        lem.append(w)
    

    ' '.join(lem[0])

    for i in range(len(lem)):
        lem[i]=' '.join(lem[i])
    
    #Polarity Estimation
    for i in range(len(lem)):
        text1=lem[i]
        blob1=TextBlob(text1)
        y=blob1.sentiment.polarity
    return y


