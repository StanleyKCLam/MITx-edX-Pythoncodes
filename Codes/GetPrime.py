# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:00:08 2017

@author: stanl
"""

def genPrimes():
    p = 1
    while True:
        p += 1
        for n in range(1, p):
            if p%(p-n) == 0: break
        if (p-n) == 1: yield p


#def genPrimes():
#    primes = []   # primes generated so far
#    last = 1      # last number tried
#    while True:
#        last += 1
#        for p in primes:
#            if last % p == 0:
#                break
#        else:
#            primes.append(last)
#            yield last