#!/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from pprint import pprint
import csv
import numpy as np
import pandas as pd
from scipy import sparse as ss

def type_to_int(type_text):
    if type_text == 'GPE':
        return 1
    elif type_text == 'Person':
        return 2
    elif type_text == 'Organization':
        return 3
    else:
        return 0

def int_to_type(type_int):
    if type_int == 1:
        return 'GPE'
    elif type_int == 2:
        return 'Person'
    elif type_int == 3:
        return 'Organization'
    else:
        return "None"

def get_brat_annotations(fname):
    anninfos = {}
    with open(fname, 'r') as fann:
        for line in fann:
            anninfo = line.strip().split('\t')[1].split(' ')
            anninfos[int(anninfo[1])] = (int(anninfo[2]), anninfo[0])
    return dict(anninfos)

def get_text(fname):
    with open(fname, 'r', encoding="utf8") as f:
        return f.read()

def get_x_y(text, bratanns, vectorizer, embeddings):
    ybratanns = []
    texttokens = []
    textembeddings = []
    token = ''
    annot = ''
    currentannotindex = 0
    ccount = 0
    for char in text:
        if char == ' ':
            texttokens.append(token)
            if token in embeddings:
                textembeddings.append(embeddings[token])
            else:
                textembeddings.append(np.zeros(100))
            currentannot = None
            token = ''
            if currentannotindex:
                currentannot = bratanns[currentannotindex][1]
            ybratanns.append(type_to_int(currentannot))
        else:
            token += char
        if not currentannotindex:
            if ccount in bratanns:
                currentannotindex = ccount
        elif ccount > bratanns[currentannotindex][0]:
            currentannotindex = 0
        ccount += 1
    xout = None
    tokensonehot = vectorizer.transform(texttokens)
    xout = tokensonehot
    textembeddings = ss.csr_matrix(np.vstack(textembeddings))
    xout = ss.hstack((xout, textembeddings))
    return vectorizer.transform(texttokens), np.array(ybratanns)


def get_x(text, vectorizer, embeddings):
    texttokens = []
    textembeddings = []
    token = ''
    for char in text:
        if char == ' ':
            texttokens.append(token)
            if token in embeddings:
                textembeddings.append(embeddings[token])
            else:
                textembeddings.append(np.zeros(100))
            currentannot = None
            token = ''
        else:
            token += char
    xout = None
    tokensonehot = vectorizer.transform(texttokens)
    xout = tokensonehot
    textembeddings = ss.csr_matrix(np.vstack(textembeddings))
    xout = ss.hstack((xout, textembeddings))
    return texttokens, vectorizer.transform(texttokens)

def main():

    allx = None
    ally = None

    import pickle
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
    from gensim.models import Word2Vec
    embeddings = Word2Vec.load('ka-embeddings')
    for i in range(10):
        for id in ['1', '2', '3', '8', '13', '33', '49', '50']:
            text = get_text('data/brat_annotations/'+id+'.txt')
            brat_annotations = get_brat_annotations('data/brat_annotations/13.ann')
            x, y = get_x_y(text, brat_annotations, vectorizer, embeddings)
            if allx is None and ally is None:
                allx = x
                ally = y
            else:
                allx = ss.vstack((allx, x))
                ally = np.hstack((ally, y))

    print(allx.shape, allx.sum())
    print(ally.shape, ally.sum())

    # from sklearn.naive_bayes import MultinomialNB
    # clf = MultinomialNB()
    from sklearn.linear_model import LogisticRegression
    clf = LogisticRegression()
    clf.fit(allx, ally)

    text = 'მიხეილ სააკაშვილი (დ. 21 დეკემბერი, 1967, თბილისი) — ქართველი პოლიტიკოსი, საქართველოს პრეზიდენტი 2004 წლის 25 იანვრიდან 2007 წლის 25 ნოემბრამდე და 2008 წლის 20 იანვრიდან – 2013 წლის 17 ნოემბრამდე. პოლიტიკური პარტია „ერთიანი ნაციონალური მოძრაობის“ დამფუძნებელი, ვარდების რევოლუციის ერთ-ერთი წინამძღოლი. ყველაზე ახალგაზრდა სახელმწიფო მეთაური ევროპაში (პრეზიდენტის მოვალეობას შეუდგა 36 წლის ასაკში). 2015 წლის 13 თებერვლიდან უკრაინის რეფორმების საერთაშორისო მრჩეველთა საბჭოს ხელმძღვანელი.[1] 2015-2016 წლებში იყო ოდესის ოლქის გუბერნატორი. მეუღლე წარმოშობით ნიდერლანდელი — სანდრა რულოვსი, ჰყავთ შვილები, ედუარდი და ნიკოლოზი.'
    toks, x = get_x(text, vectorizer, embeddings)
    prediction = clf.predict(x)
    for i in range(len(toks)):
        print(toks[i], int_to_type(prediction[i]))

if __name__ == "__main__":
    main()
