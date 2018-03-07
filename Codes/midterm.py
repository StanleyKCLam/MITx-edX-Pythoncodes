# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 21:47:51 2017

@author: stanl
"""

def score(word, f):
    """
       word, a string of length > 1 of alphabetical 
             characters (upper and lowercase)
       f, a function that takes in two int arguments and returns an int

       Returns the score of word as defined by the method:

    1) Score for each letter is its location in the alphabet (a=1 ... z=26) 
       times its distance from start of word.  
       Ex. the scores for the letters in 'adD' are 1*0, 4*1, and 4*2.
    2) The score for a word is the result of applying f to the
       scores of the word's two highest scoring letters. 
       The first parameter to f is the highest letter score, 
       and the second parameter is the second highest letter score.
       Ex. If f returns the sum of its arguments, then the 
           score for 'adD' is 12 
    """
    l = []
    wordl = word.lower()
    for d in range(len(word)):
        s = 'abcdefghijklmnopqrstuvwxyz'.find(wordl[d]) + 1
        print('s=', s, 'd=', d)
        l = l + [s*d]
    print(l)
    h1 = 0
    h2 = 0
    if l != []:
        h1 = max(l)
        while h1 in l:
            l.remove(h1)
        if l != []: h2 = max(l)
    return f(h1, h2)

def f(a,b):
    return a+b