import os
import sys
import re

fname = "data/data.txt"
lines =0
nwords =0
nchars =0
nlemma =0

exists = os.path.isfile(fname)
if exists:
	with open(fname, 'r',encoding="utf8") as f:
		for line in f:
			words=line.split()
			lines+=1
			nwords+=len(words)
			nchars+=len(line)
		print("number of chars of file",fname,"is :", nchars)
		print("number of words of file",fname,"is :", nwords)
		print("number of lines of file",fname,"is :", lines)

		f = open(fname, 'r',encoding="utf8")
		lines = f.readlines()
		for idx, line in enumerate(lines):
		    if not line == '\n':
		        m = re.search(r'\w', line)
		        str = m.group(0)
		    try:
		        if line == '\n' and str in lines[idx-1]: 
		            nlemma +=1
		    except:
		        pass
		        if lines[-1] != '\n':
		            nlemma +=1
		print("number of lemma of file",fname,"is :", nlemma)
else:
    print("File", fname, "does not exist")