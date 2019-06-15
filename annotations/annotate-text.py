import sys
import os


def get_cmd_args():
    if len(sys.argv) > 2:
        return sys.argv[0], sys.argv[1]
    else:
        return os.getcwd() + r'\text-input.txt', \
               os.getcwd() + r'\words-to-match.txt'


def get_text_and_words():
    text_path, words_to_match_path = get_cmd_args()

    with open(text_path, 'r') as f:
        text = f.read()

    with open(words_to_match_path) as f:
        words = [line.strip() for line in f.readlines()]

    return text, words


def annotate_word(word):
    return '<b> {} </b>'.format(word)


def annotate_text(text, words):
    for word in words:
        text = text.replace(word, annotate_word(word))

    return text


def main():
    text, words = get_text_and_words()

    print(annotate_text(text, words))


if __name__ == "__main__":
    main()
