#bite8
#https://codechalleng.es/bites/8/

from collections import deque
def rotate(string, n):
    """Rotate characters in a string. Expects string and n (int) for 
       number of characters to move.
    """
    word = deque(string)
    word.rotate(-n)
    return ''.join(word)
    