#!/usr/bin/python3
import re
myText=""
def myStrip(word):
    word.replace("	","");
    return word
with open("test1.txt") as file_to_read:
    for line in file_to_read:
        if not "<" in line[0]:
            token=line.split("	")[0];
            if re.match('^[ა-ჰa-zA-Z0-9_]+$',token):
                token=" "+token
            myText+=token;
###
print(myText);
