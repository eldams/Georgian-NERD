#!/bin/env python
# -*- coding: utf-8 -*-

import re, sys

sent = []
sentences = []
linecount = 0
maxlines = None
print('read corpus')
for line in sys.stdin:
	if not line.startswith('<'):
		sent.append(line.strip().split('\t')[0])
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
