# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 06:24:56 2017

@author: stanl
"""


s='dc'
lg=""
for p in range(len(s)):
    m=p+1
    l=s[p]
    while m<len(s):
        if s[m-1]<=s[m]:
            l+=s[m]
            m+=1
        else:
            break
    if len(lg)<len(l):
        lg=l
print(lg)