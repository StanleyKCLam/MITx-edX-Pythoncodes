# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 22:31:51 2017

@author: stanl
"""


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    wordList = list(secretWord)
    for letter in lettersGuessed:
        while letter in wordList:
            wordList.remove(letter)
    return wordList == []

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    showWord = ""
    for letter in secretWord:
        if letter in lettersGuessed: showWord += letter + " "
        else : showWord += "_ "
    return showWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    allList = list(string.ascii_lowercase)
    for letter in lettersGuessed:
        if letter in allList:
            allList.remove(letter)
    return "".join(allList)


a = "apple"
b = ['i', 'k', 'r', 's', 'e', 'p', 'p', 'p', 'i']
#print(isWordGuessed(a, b))
#print(getGuessedWord(a, b))
print(getAvailableLetters(b))