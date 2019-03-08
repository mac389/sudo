import nltk, json, os, itertools 

from pprint import pprint 
from collections import Counter 

abstracts = json.load(open(os.path.join('..','data','text-of-abstracts.json'),'r'))
stopwords = open(os.path.join('..','data','stopwords')).read().splitlines()

text_of_all_abstracts = [word.lower() for word in nltk.word_tokenize(' '.join(itertools.chain.from_iterable(abstracts.iteritems())))
							if word.isalpha() and word.lower() not in stopwords]

print len(text_of_all_abstracts) #5044
print len(set(text_of_all_abstracts)) #1219


words_freqs =dict(Counter(text_of_all_abstracts))
json.dump(words_freqs,open(os.path.join('..','data','freqs-of-words-in-abstracts.json'),'w'))
words_freqs = nltk.FreqDist(text_of_all_abstracts)

words_freqs.plot(30,cumulative=False)