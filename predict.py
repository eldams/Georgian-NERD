#!/bin/env python
# -*- coding: utf-8 -*-

import pickle, sys
from preparemodel import get_toks_x_y, entypes

for line in sys.stdin:
	line = line.strip()
	toks, x, y = get_toks_x_y(line)
	if len(toks):
		model = pickle.load(open('model.pkl', 'rb'))
		pred = model.predict(x)
		out = ''
		nbtoks = len(toks)
		prevEn = 0
		for toki in range(nbtoks):
			if prevEn != pred[toki]:
				if prevEn:
					out += '</b>'
				if pred[toki]:
					out += '<b entype="'+entypes[pred[toki]]+'" link="">'
				prevEn = pred[toki]
			out += toks[toki]
		if prevEn:
			out += '</b>'
		print(out)