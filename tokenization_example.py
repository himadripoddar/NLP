import spacy
nlp = spacy.load('en_core_web_sm')

text = "My name is Himadri. I am from NIT Trichy and I am currently doing my Btech 3rd year. I have a lenovo laptop."
spacy_doc = nlp(text)

for i in spacy_doc:
    print(i.text,i.idx,i.is_stop,i.is_space,i.is_punct)

