# from nltk.corpus import stopwords
# from nltk.tokenize import sent_tokenize
# from nltk.tokenize import word_tokenize
# from nltk import pos_tag
#
# stop_words = set(stopwords.words('english'))
#
# txt = "Hello peeps! I am Himadri. I would be doing a project on NLP. It will include intensive study of a BERT Model "
#
# tokenized = sent_tokenize(txt)
# for i in tokenized:
#
#     wordsList = word_tokenize(i)
#
#     # removing stop words from wordList
#     #wordsList = [w for w in wordsList if not w in stop_words]
#
#     tagged = pos_tag(wordsList)
#
#     print(tagged)


#using spacy

import spacy
nlp = spacy.load('en_core_web_sm')

txt = "Hello peeps! I am Himadri. I would be doing a project on NLP. It will include intensive study of a BERT Model "
doc = nlp(txt)

for token in doc:
    print(token.text,token.tag_,spacy.explain(token.tag_))