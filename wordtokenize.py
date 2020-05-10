#for nltk based tokenization
from nltk.tokenize import sent_tokenize, word_tokenize

#for spacy based tokenization
import spacy
nlp = spacy.load('en_core_web_sm')

#the text that will be your data
data = "My name is Himadri and I am from NIT Trichy."

#for nltk tokenization
print(word_tokenize(data))

#for spacy tokenizatin
doc = nlp(data)
for i in doc:
    print(i.text)
 