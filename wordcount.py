#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Wordcount exercise

The main() function is already defined and complete. It calls the
print_words() and print_top() functions, which you fill in.

See the README for instructions.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure. Once that's working, try for the
next milestone.

Implement the create_word_dict() helper function that has been defined in
order to avoid code duplication within print_words() and print_top(). It
should return a dictionary with words as keys, and their counts as values.
"""

# Your name, plus anyone who helped you with this assignment
# Give credit where credit is due.
import sys
__author__ = """
stephguirand,
Help from demo, lessons and activities,
youtube videos in canvas and
own search on youtube,
stack overflow, Tutors, Facilitators and talking about
assignment in study group"""


"""Returns a word/count dict for the given file."""


def create_word_dict(filename):
    f = open(filename, 'r')
    file_info = dict()
    for line in f:
        words = line.split()
        for word in words:
            file_info[word.lower()] = file_info.get(word.lower(), 0) + 1
    f.close()
    return file_info


"""Prints one per line '<word> : <count>', sorted
   by word for the given file."""


def print_words(filename):
    p_words = create_word_dict(filename)
    words = sorted(p_words.keys())
    for word in words:
        print(word, p_words[word])
        # return p_words


"""Prints the top count listing for the given file."""


def print_top(filename):
    p_words = create_word_dict(filename)
    # Sort them so the
    p_wordsList = sorted(p_words.items(), key=get_count, reverse=True)
    for item in p_wordsList[:20]:
        print(item[0], item[1])


"""Returns the count from a dict word/count tuple used for sort"""


def get_count(p_words_tuple):
    return p_words_tuple[1]

    # This basic command line argument parsing code is provided and calls
    # the print_words() and print_top() functions which you must implement.


def main(args):
    if len(args) != 2:
        print('usage: python wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = args[0]
    filename = args[1]

    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)


if __name__ == '__main__':
    main(sys.argv[1:])
