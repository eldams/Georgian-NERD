#!/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from pprint import pprint
import csv
import numpy as np
import pandas as pd
from scipy import sparse as ss
import pickle
from gensim.models import Word2Vec
from sklearn.linear_model import LogisticRegression

entypes = ['None', 'GPE', 'Person', 'Organization']
ann_ids = ['1', '2', '3', '8', '13', '33', '49', '50']
# print('loading vectorizer and embeddings')
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
embeddings = Word2Vec.load('ka-embeddings')

def get_brat_annotations(fname):
	anninfos = {}
	with open(fname, 'r') as fann:
		for line in fann:
			anninfo = line.strip().split('\t')[1].split(' ')
			anninfos[int(anninfo[1])] = (int(anninfo[2]), anninfo[0])
	return dict(anninfos)

def get_text(fname):
	with open(fname, 'r') as f:
		return f.read()

def get_toks_x_y(text, bratanns = None):
	token = ''
	ccount = 0
	texttokens = []
	textembeddings = []
	if bratanns:
		ann = ''
		annindex = 0
		textanns = []
	for char in text:
		if len(token) and token[-1].isalpha() != char.isalpha():
			texttokens.append(token)
			if token in embeddings:
				textembeddings.append(embeddings[token])
			else:
				textembeddings.append(np.zeros(100))
			token = char
			if bratanns:
				ann = 'None'
				if annindex:
					ann = bratanns[annindex][1]
				textanns.append(ann)
		else:
			token += char
		if bratanns:
			if not annindex:
				if ccount in bratanns:
					annindex = ccount
			elif ccount > bratanns[annindex][0]:
				annindex = 0
		ccount += 1
	if not len(texttokens):
		return [], None, None
	xout = vectorizer.transform(texttokens)
	textembeddings = ss.csr_matrix(np.vstack(textembeddings))
	xout = ss.hstack((xout, textembeddings))
	yout = None
	if bratanns:
		yout = np.array([entypes.index(ann) for ann in textanns])
	return texttokens, xout, yout

def main():
	trainx = []
	trainy = []
	evalx = []
	evaly = []
	idcount = 0
	for id in ann_ids:
		print('loads annotation'+id)
		text = get_text('data/brat_annotations/'+id+'.txt')
		brat_annotations = get_brat_annotations('data/brat_annotations/'+id+'.ann')
		toks, x, y = get_toks_x_y(text, brat_annotations)
		idcount += 1
		if idcount%5:
			trainx.append(x)
			trainy.append(y)
		else:
			evalx.append(x)
			evaly.append(y)
	trainx = ss.vstack(trainx)
	trainy = np.hstack(trainy)
	evalx = ss.vstack(evalx)
	evaly = np.hstack(evaly)
	print('train model')
	clf = LogisticRegression()
	clf.fit(trainx, trainy)
	pickle.dump(clf, open('model.pkl', 'wb'))
	evalpred = clf.predict(evalx)
	nbeval = evalpred.shape[0]
	print('evaluation on', nbeval,'tokens')
	ones = np.ones((nbeval))
	errors = evalpred - evaly
	errors = np.minimum(errors, ones)
	errors = np.maximum(errors, -ones)
	falses = abs(errors.sum())
	trues = nbeval - falses
	print('error', falses, 'rate', falses/nbeval)
	zeros = np.zeros((nbeval))
	positives = np.minimum(evalpred, ones).sum()
	negatives = nbeval-positives
	falsepositive = np.maximum(errors, zeros).sum()
	truepositives = positives-falsepositive
	falsenegative = -np.minimum(errors, zeros).sum()
	prec = truepositives/positives
	print('precision', prec)
	rec = truepositives/trues
	print('recall', rec)
	fsc = 2*prec*rec/(prec+rec)
	print('fscore', fsc)

if __name__ == '__main__':
	main()
