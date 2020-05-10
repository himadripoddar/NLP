import spacy
nlp = spacy.load('en_core_web_sm')
from collections import Counter

text = "My name is Himadri. Himadri loves Singing and reading are my hobbies. Himadri is  from NIT Trichy and I am currently doing my Btech 3rd year. I have a lenovo laptop."
doc = nlp(text)

#remove stop words
words = [token.text for token in doc
         if not token.is_stop and not token.is_punct]
word_freq = Counter(words)
common_words = word_freq.most_common(5)

print(common_words)

unique_words = [word for (word, freq) in word_freq.items() if freq == 1]
print (unique_words)