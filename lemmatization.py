import spacy
nlp = spacy.load('en_core_web_sm')

text = "My name is Himadri. Singing and reading are my hobbies. I am from NIT Trichy and I am currently doing my Btech 3rd year. I have a lenovo laptop."
doc = nlp(text)

for token in doc:
    print(token,token.lemma_)