# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 00:59:48 2017

@author: stanl
"""

balance = 320000
annualInterestRate = 0.2
nMax = 100
tolr = 0.1
lowerBound = balance/12
upperBound = (balance * (1 + annualInterestRate/12)**12)/12
updatedBal = balance
n = 0
while n < nMax and abs(updatedBal)>tolr:
    previousBal = balance
    lowestMthPayment = round((lowerBound + upperBound)/2, 2)
    print(n, lowestMthPayment)
    for mth in range(12):
        mthUnpaidBal = previousBal - lowestMthPayment
        updatedBal = round(mthUnpaidBal + annualInterestRate/12 * mthUnpaidBal, 2)
        previousBal = updatedBal
    if updatedBal > 0:
        lowerBound=lowestMthPayment
    else:
        upperBound=lowestMthPayment
    n += 1
print("Lowest Payment:", lowestMthPayment)