#!/bin/bash

#python3 extract-mediawikicats.py > data/entities.lst
g++ -std=c++11 -O3 split.cpp -o split
cat data/*.tsv | head -n 1000000 | python tsv2txt.py > data/data.txt
./split