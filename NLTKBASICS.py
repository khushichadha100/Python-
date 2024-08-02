import nltk
from nltk.tokenize import word_tokenize , sent_tokenize
from nltk import pos_tag 
#nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import PorterStemmer , \
RegexpStemmer , SnowballStemmer, LancasterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.collocations import BigramCollocationFinder , \
TrigramCollocationFinder , ngrams
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.wsd import lesk

x="Natural language processing (NLP) is an interdisciplinary subfield . of computer science and artificial intelligence . It is primarily concerned . with providing computers the ability to process data encoded in natural language . is thus closely related to information retrieval, knowledge representation and computational linguistics . a subfield of linguistics." 
'''
sent=sent_tokenize(x)
print("senetence tokenization\n")
for i in sent:
    print(i)
    print()
'''

print("word tokenization\n")
w=word_tokenize(x)
for j in w:
    print(j)
print()
    
print("assigning parts of speech\n")
p=pos_tag(w)
print(p)
print()
 
#print(" this is nltk.corpus stopwords list\n")
stp=stopwords.words('english')
#print(stp)

stop_words_list=list(punctuation) + stp
#print(stop_words_list)

'''
print("removing stop words")
for i in w:
    if i not in stop_words_list:
        print(i)
'''
#stemming
p=PorterStemmer()
r=RegexpStemmer('ed' )
s=SnowballStemmer('english')
l=LancasterStemmer()
print(p.stem("changing"))
print(r.stem("changed"))
print(s.stem("changing"))
print(l.stem("changing"))

#lemmatization
wl=WordNetLemmatizer()
print(wl.lemmatize('changing'))
print(wl.lemmatize('mice'))

b=BigramCollocationFinder.from_words(w)
op=b.ngram_fd
dictop=dict(op)
print(dictop)
t=TrigramCollocationFinder.from_words(w)
op=t.ngram_fd
dictop=dict(op)
print(dictop)
print("ngrams :")
n=ngrams(w,3)
for i in n:
    print(i)
print()
#vectorization
l=["my name is khushi","i am coding right now in python"]
df=pd.DataFrame({"data":l})
print("this is dataframe \n")
print(df)

cv=CountVectorizer()
new_data=cv.fit_transform(df['data']).toarray()
print("dataframe converted into vector \n")
print(new_data) #dataframe converted into vector

#word_sense_diambiguation
k="sun is a  star which is hot and present in the solar system"
x=lesk(word_tokenize(k),'sun')
print(x)
print(x.definition())

