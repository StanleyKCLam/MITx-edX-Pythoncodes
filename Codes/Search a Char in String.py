# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 22:06:40 2017

@author: stanl
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    b=0
    e=len(aStr)
    if e<=1:
        return char==aStr
    if char<=aStr[e//2-1]:
        e=e//2
    else:
        b=e//2
    print(b,e,aStr[b:e])
    return isIn(char, aStr[b:e])
print(isIn("e", "abcdeg"))