import pandas as pd
import re
import nltk
from nltk import sent_tokenize, word_tokenize
import heapq



df = pd.read_csv("../Dataset/haberler.csv", decoding='utf8', engine='python')
df['lowercase'] = df['HABERMETNI'].apply(lambda x: x.lower())

def remove_number(text):
    text = re.sub(r'[0-9]+', '', text)
    return text

df['removed_num'] = df['lowercase'].apply(lambda x: remove_number(x))

stopwords = nltk.corpus.stopwords.words('turkish')

word_frequencies = {}
for word in nltk.word_tokenize(text=text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word] / maximum_frequncy)

sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

summary_sentences = heapq.nlargest(1, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)
print(summary)



