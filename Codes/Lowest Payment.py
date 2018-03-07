# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 00:27:11 2017

@author: stanl
"""

balance = 3926
annualInterestRate = 0.2

lowestMthPayment = 10
updatedBal = balance
while updatedBal > 0:
    previousBal = balance
    for mth in range(12):
        mthUnpaidBal = previousBal - lowestMthPayment
        updatedBal = round(mthUnpaidBal + annualInterestRate/12 * mthUnpaidBal, 2)
        previousBal = updatedBal
    if updatedBal > 0:
        lowestMthPayment += 10
print("Lowest Payment:", lowestMthPayment)
