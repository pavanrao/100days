#Py bites 3
#https://codechalleng.es/bites/3/

import os
import urllib.request
import operator

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    with open(DICTIONARY) as f:
    	words = f.read()
    return words.split()


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    return sum([ LETTER_SCORES[letter] for letter in word.upper()])


def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    #TODO refactor this, check solution on the website
    d = {word: calc_word_value(word) for word in words}
    return max(d.items(), key = operator.itemgetter(1) )[0]
