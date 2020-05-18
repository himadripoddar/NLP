from bs4 import BeautifulSoup
import csv

from nltk.tokenize import sent_tokenize

# importing the .xml file and reading it
with open("1.xml", "r") as f:
    contents = f.read()

    # creating an object of the beautifulsoup class
    soup = BeautifulSoup(contents, 'xml')

    # taking all the text tagged as a list
    texts = soup.find_all('TEXT')
    texts = texts[0].get_text()

    # finding the event tagged as a list
    events = soup.find_all('EVENT')

    times = soup.find_all('TIMEX3')

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
        List.append([word, start, end, 'O', 'O', 'O', 'O', 'O'])
    List.append([None, None,None,None,None,None,None,None])
#
# # for checking if the proper mapping has taken place
# print(List)
#
# for i in List:
#     if(i[1] == 2400):
#         print(i[0])
#
for event in events:
    start = event.attrs['start']
    end = event.attrs['end']
    type = event.attrs['type']
    modality = event.attrs['modality']
    polarity = event.attrs['polarity']
    identity = event.attrs['id']
    for i in List:
        if i[1] == int(start) and i[2] == int(end):
            i[3] = identity
            i[4] = "B-" + str(type)
            i[5] = "B-" + str(modality)
            i[6] = "B-" + str(polarity)
        elif i[1] == int(start):
            i[3] = identity
            i[4] = "B-" + str(type)
            i[5] = "B-" + str(modality)
            i[6] = "B-" + str(polarity)
            while (i[2] != int(end)):
                i = List[List.index(i) + 1]
                i[3] = identity
                i[4] = "I-" + str(type)
                i[5] = "I-" + str(modality)
                i[6] = "I-" + str(polarity)

            i[3] = identity
            i[4] = "I-" + str(type)
            i[5] = "I-" + str(modality)
            i[6] = "I-" + str(polarity)


# for i in List:
#     print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],sep = '\t')


for time in times:
    start = time.attrs['start']
    end = time.attrs['end']
    type = time.attrs['type']
    modality = time.attrs['mod']
    value = time.attrs['val']
    identity = time.attrs['id']
    for i in List:
        if i[1] == int(start) and i[2] == int(end):
            i[3] = identity
            i[4] = "B-" + str(type)
            i[5] = modality
            i[7] = value
        elif i[1] == int(start):
            i[3] = identity
            i[4] = "B-" + str(type)
            i[5] = modality
            i[7] = value
            while (i[2] != int(end)):
                i = List[List.index(i) + 1]
                i[3] = identity
                i[4] = "I-" + str(type)
                i[5] = modality
                i[7] = value

            i[3] = identity
            i[4] = "I-" + str(type)
            i[5] = modality
            i[7] = value


# for i in List:
#     print(i[0], i[1], i[2], i[3], i[4], i[5], i[6],i[7], sep='\t')

with open('1.tsv', mode='w') as csv_file:
    fieldnames = ['word', 'start', 'end', 'identity', 'type', 'modality', 'polarity','value']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames,delimiter = '\t', lineterminator = '\n')

    writer.writeheader()
    for i in List:
        writer.writerow({'word': i[0], 'start': i[1], 'end': i[2], 'identity': i[3], 'type': i[4], 'modality': i[5],
                         'polarity': i[6], 'value': i[7]})


#
# for time in times:
#     print(time)
