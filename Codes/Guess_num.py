# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 00:28:05 2017

@author: stanl
"""

print("Please think of a number between 0 and 100!")
high=100
low=0
guess=int((high+low)/2)
ans=""
while ans!="c":
    print("Is your secret number", guess)
    ans=input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if ans not in "lhc":
        print("Sorry, I did not understand your input.")
    elif ans=="l":
        low=guess
        guess=int((high+low)/2)
    elif ans=="h":
        high=guess
        guess=int((high+low)/2)
print("Game over. Your secret number was:", guess)