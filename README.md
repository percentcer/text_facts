text_facts
==========

Facts about text!  Inspired by the examples in python's standard collections module.

usage: analyzer.py [-h] [-v V] [-n N] FILE

Get some facts about the text

positional arguments:
  FILE              path to file that will be analyzed

optional arguments:
  -h, --help        show this help message and exit
  -v V, --screen V  filter out the Vth most common words in English (the, and,
                    of, etc.), according to
                    https://github.com/first20hours/google-10000-english.
                    Defaults to the full file.
  -n N, --count N   maximum words to return
