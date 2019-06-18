#!/usr/bin/python3

import re, sys

sent = []
sentences = []
linecount = 0
maxlines = None
print('read corpus')
for line in sys.stdin:
	lineparts = line.strip().split('\t')
	if len(lineparts) > 1:
		lemma = lineparts[1]
		if len(lemma) > 2:
			sent.append(lemma[1:-1])
	if '</div>' in line:
		sentences.append(sent)
		sent = []
	linecount += 1
	if maxlines and linecount > maxlines:
		break

from gensim.models import Word2Vec
print('embeddings')
model = Word2Vec(sentences, size=100, window=5, min_count=2, workers=2)
model.save('ka-embeddings')
print('save')
