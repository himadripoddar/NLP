import spacy
nlp = spacy.load('en_core_web_sm')

text = 'my name is H.S. Poddar'
doc = nlp(text)
for token in doc:
    print(token.text,token.pos_,token.dep_)
