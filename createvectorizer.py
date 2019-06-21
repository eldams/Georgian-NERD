#!/bin/env python
# -*- coding: utf-8 -*-

from sklearn.feature_extraction.text import CountVectorizer
corpus = []
with open('data/all.txt') as alltxt:
	for l in alltxt:
		corpus.append(l.strip())
vectorizer = CountVectorizer()
vectorizer.fit(corpus)

import pickle
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
