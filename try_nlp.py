# -*- coding: utf-8 -*-

from urllib import request
import nltk
from collections import defaultdict
import re

nlp_dir = '/Users/Shared/miniconda3/nltk_data'
nlp_list = ['names', 'stopwords', 'treebank', 'state_union', 'punkt', 'twitter_samples', 'movie_reviews', 'averaged_perceptron_tagger', 'vader_lexicon', 'maxent_ne_chunker', 'words']
# nltk.download(nlp_list, download_dir=nlp_dir)

url = 'http://www.gutenberg.org/files/2554/2554-0.txt'
response = request.urlopen(url)
raw = response.read().decode('utf8')
text = raw[:12345]

sentences = nltk.sent_tokenize(text)
token_sentences = [nltk.word_tokenize(sent) for sent in sentences]
pos_sentences = [nltk.pos_tag(sent) for sent in token_sentences]
chunked_sentences = nltk.ne_chunk_sents(pos_sentences, binary=True)

# Extract and print all Named Entities Recognition
ner_categories = defaultdict(int)
for sent in chunked_sentences:
    for chunk in sent:
        if hasattr(chunk, "label"):
            print(chunk)
            ner_categories[chunk.label()] += 1

labels = list(ner_categories.keys())
print(ner_categories.items())

fd = nltk.FreqDist(token_sentences[1])
print(fd.most_common(5))

import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp(text)
for ent in doc.ents:
    print(ent.label_, ent.text)

wordlist = [w for w in nltk.corpus.treebank.words() if w.islower()]
print(set([w for w in wordlist if re.search('(ued|ier)$', w)]))

stopwords = nltk.corpus.stopwords.words("english")
wordlist = [w for w in nltk.corpus.state_union.words() if w.isalpha() and w.lower() not in stopwords]
print(len(wordlist))


