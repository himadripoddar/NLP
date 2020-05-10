import spacy
nlp = spacy.load('en_core_web_sm')

text = "Ram is eating rice. Shyam is his brother"
doc = nlp(text)

for token in doc:
    print(token.text,token.tag_,token.head.text,token.dep_)
