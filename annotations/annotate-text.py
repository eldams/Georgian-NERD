# p1 = text file,
# p2 = annotated file
# tag text
# return annotated text
import sys
import os


def get_cmd_args():
    if len(sys.argv) > 2:
        return sys.argv[0], sys.argv[1]
    else:
        return os.getcwd() + r'\annotations\text-input.txt', \
               os.getcwd() + r'\annotations\words-to-match.txt'


def get_text_and_words():
    text_path, words_to_match_path = get_cmd_args()

    with open(text_path, 'r') as f:
        text = f.read()

    with open(words_to_match_path) as f:
        words = [line.strip() for line in f.readlines()]

    return text, words


def main():
    text, words = get_text_and_words()

    print(text)
    print(words)






if __name__ == "__main__":
    main()
