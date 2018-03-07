# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:47:05 2017

@author: stanl
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    sum = 0
    for k in aDict:
        sum += len(aDict[k])
    return sum

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
animals['d'].append('dingo')

print(how_many(animals))