import spacy
nlp = spacy.load('en_core_web_sm')

txt = " My name is Himadri. I have a Samsung mobile"

data = nlp(txt)

for ent in data.ents:
    print(ent.text,ent.start_char,ent.end_char,ent.label_)
