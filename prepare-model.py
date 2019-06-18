import sys
import re
from pprint import pprint
import csv
import numpy as np
import pandas as pd


def get_text_file_path(arg_index, default):
    if len(sys.argv) > arg_index:
        return sys.argv[arg_index]
    else:
        return default


def type_to_int(type_text):
    if type_text == 'GPE':
        return 1
    elif type_text == 'Person':
        return 2
    elif type_text == 'Organization':
        return 3
    else:
        return 0


def get_brat_annotations():
    brat_file_path = get_text_file_path(2, r'./data/brat_annotations/2.ann')
    user_info = pd.read_csv(brat_file_path,
                            delimiter='\t',
                            encoding='utf-8',
                            header=None)
    user_info = user_info[[2, 1]]
    tuples = [tuple(x) for x in user_info.values]
    tuples = [(name, type_to_int(type.split()[0])) for (name, type) in tuples]

    return dict(tuples)


def get_text():
    file_path = get_text_file_path(1, r'./data/text_files/2.txt')
    with open(file_path, encoding="utf8") as f:
        return f.read()


def get_x_y(text, brat_annotations):
    words = re.sub("[^\w]", " ", text).split()
    return np.array([word for word in words]),\
           np.array([brat_annotations.get(word, 0) for word in words])


def main():
    text = get_text()
    brat_annotations = get_brat_annotations()

    x, y = get_x_y(text, brat_annotations)

    np_array = np.column_stack((x, y))
    print(np_array)


if __name__ == "__main__":
    main()
