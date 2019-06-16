#!/usr/bin/python3
import re, sys
myText=""
for line in sys.stdin:
    line = line.strip()
    if not "<" in line[0]:
        token=line.split("	")[0];
        if re.match('^[ა-ჰa-zA-Z0-9_]+$',token):
            token=" "+token
        myText+=token
    elif '</div>' in line:
        myText+='\n'
print(myText)
