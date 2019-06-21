#!/bin/env python
# -*- coding: utf-8 -*-

import re, sys
myText=''
words = {}
for line in sys.stdin:
	line = line.strip()
	if not line.startswith('<'):
		token=line.split("	")[0];
		if not token in words:
			words[token] = 0
		words[token] += 1
		myText+= " "+token
	elif '</div>' in line:
		print(myText)
		myText=''

wrdslstfile = open('data/words.lst', 'w')
for word in sorted(words.keys()):
	wrdslstfile.write(word+'\t'+str(words[word])+'\n')
