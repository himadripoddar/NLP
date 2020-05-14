from bs4 import BeautifulSoup

from nltk.tokenize import sent_tokenize

#importing the .xml file and reading it
with open("1.xml", "r") as f:
    contents = f.read()

    #creating an object of the beautifulsoup class
    soup = BeautifulSoup(contents, 'xml')

    #taking all the text tagged as a list
    texts = soup.find_all('TEXT')
    texts = texts[0].get_text()

    #finding the event tagged as a list
    events = soup.find_all('EVENT')



List = []
index = 0
sentences = sent_tokenize(texts)

for sent in sentences:
    words = sent.split()
    for word in words:
        length = len(word)
        index = index + 1
        start = index
        end = index + length
        index = index + length
        List.append([word, start, end, 'O'])


## for checking if the proper mapping has taken place
# print(List)
#
# for i in List:
#     if(i[1] == 1544):
#         print(i[0])
#
for event in events:
    start = event.attrs['start']
    end = event.attrs['end']
    type = event.attrs['type']
    for i in List:
        if (i[1] == int(start) and i[2] == int(end)):
            i[3] = type
        elif(i[1]==int(start)):
            i[3] = "B-" + str(type)
            while(i[2]!=int(end)):
                i = List[List.index(i) + 1]
                i[3] = "I-" + str(type)

            i[3] = "I-" + str(type)


for i in List:
    print(i[0],i[1],i[2],i[3],sep = '\t')

