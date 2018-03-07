# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 23:56:47 2017

@author: stanl
"""

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
previousBal = balance
for mth in range(12):
    minPay = monthlyPaymentRate * previousBal
    mthUnpaidBal = previousBal - minPay
    updatedBal = round(mthUnpaidBal + annualInterestRate/12 * mthUnpaidBal, 2)
    print("Month", mth+1, "Remaining balance:", updatedBal)
    previousBal = updatedBal
print("Remaining balance:", updatedBal)
