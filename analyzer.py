__author__ = 'Spencer'

import re
import os
import argparse
from collections import Counter


def relative(path):
    this_dir, this_filename = os.path.split(__file__)
    DATA_PATH = os.path.join(this_dir, path)
    return DATA_PATH


def common_word_set(n=None):
    try:
        wordlist = common_word_set.__wl
    except AttributeError:
        # cache it
        wordlist = common_word_set.__wl = re.findall(r'\S+', open(relative('common.txt')).read().lower())

    return set(wordlist[:n])


def setup_args():
    parser = argparse.ArgumentParser(description="Get some facts about the text")
    parser.add_argument('text', metavar='FILE', type=argparse.FileType('r'), help='path to file that will be analyzed')
    parser.add_argument('-v', '--screen', metavar='V', type=int,
                        help='filter out the Vth most common words in English (the, and, of, etc.), \
                        according to https://github.com/first20hours/google-10000-english.  Defaults to the full file.',
                        required=False)
    parser.add_argument('-n', '--count', metavar='N', type=int, help='maximum words to return', default=100,
                        required=False)
    args = vars(parser.parse_args())

    args['screen'] = common_word_set(args['screen'])

    return args


def word_count(text, screened=common_word_set(), max_count=100):
    words = re.findall(r'[A-Za-z][A-Za-z-]*\w(?:\'[^s\s]+)?', text.lower())
    return Counter([w for w in words if w not in screened]).most_common(max_count)


def print_word_count(count):
    largest = count[0][1]
    normalized = largest / 76.0
    for word, n in count:
        print("{0}{1}{2}".format(word.ljust(16), '({0}) '.format(n).rjust(8), '-' * int(n / normalized)))


if __name__ == '__main__':
    args = setup_args()
    count = word_count(args['text'].read().lower(), args['screen'], args['count'])
    print_word_count(count)