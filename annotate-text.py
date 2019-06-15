import sys
import os


def get_cmd_args():
    if len(sys.argv) > 2:
        return sys.argv[1], sys.argv[2]
    else:
        return os.getcwd() + r'/data/sample.txt', \
               os.getcwd() + r'/data/entities-sample.lst'

def get_text_and_words():
    text_path, words_to_match_path = get_cmd_args()

    with open(text_path, 'r') as f:
        text = f.read()

    words = {}
    with open(words_to_match_path) as f:
        for line in f.readlines():
            lineparts = line.strip().split(',')
            if len(lineparts) == 2:
                word = lineparts[0]
                type = lineparts[1]
                words[word] = type

    return text, words


def annotate_word(word, type):
    return '<b entype="'+type+'" link=""> {} </b>'.format(word)


def annotate_text(text, words):
    for word in words:
        type = words[word]
        text = text.replace(word, annotate_word(word, type))

    return text


def main():
    text, words = get_text_and_words()

    print(annotate_text(text, words))


if __name__ == "__main__":
    main()
