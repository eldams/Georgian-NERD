#!/bin/bash

# python3 extract-mediawikicats.py > data/entities.lst
# cat data/civil-ge.tsv data/tavisupleba.tsv > data/all.tsv
# cat data/all.tsv | python tsv2txt.py > data/all.txt
# python createvectorizer.py
# g++ -std=c++11 -O3 split.cpp -o split && ./split
# cat data/all.tsv | python learnembeddings.py
python preparemodel.py
# g++ -std=c++11 -O3 html2brat.cpp -o html2brat
