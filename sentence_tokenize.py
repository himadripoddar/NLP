from nltk.tokenize import sent_tokenize, word_tokenize
import spacy
nlp = spacy.load('en_core_web_sm')

data = "Hello peeps! I am K.L. Himadri. I would be doing a project on NLP. It will include intensive study of a BERT Model"
#print(word_tokenize(data))

doc = nlp(data)
sentences = list(doc.sents)

for  i in sentences:
    print(i)