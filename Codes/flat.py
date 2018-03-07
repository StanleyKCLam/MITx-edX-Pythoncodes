# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 22:39:09 2017

@author: stanl
"""

a = [5, 4, 3, [101, 102, 103]]
#a = [5, 4, 3, 101, 102, 103]
#if 'list' in str(type(a[3])):
#    d = a + a.pop()
#    print('###', d)
#else:
#    d = a
#    print('***', d)

#r = [201, 202]
#if 'list' not in str(type(a[3])):
#    r = r + [a.pop()]
#    print('***', r)
#else:
#    r = r + a.pop()
#    print('###', r)


#def flatten(aList):
##    print('new recursion', aList)
##    input('-------------')
#    if aList == []: return []
#    if len(aList) == 1:
#        if 'list' not in str(type(aList[0])):
##            print('Not a list')
#            return aList
#        else:
##            print('Still a list')
#            return flatten(aList[0])
#    else:
#        if 'list' not in str(type(aList[-1])):
#            p = aList.pop()
##            print('Not a list', p)
#            return flatten(aList) + [p]
#        else:
#            p = aList.pop()
##            print('Still a list', p)
#            return flatten(aList) + flatten(p)


def flatten(aList):
    if aList == []: return []
    if len(aList) == 1:
        if 'list' not in str(type(aList[0])): return aList
        else: return flatten(aList[0])
    else:
        if 'list' not in str(type(aList[-1])):
            p = aList.pop()
            return flatten(aList) + [p]
        else:
            p = aList.pop()
            return flatten(aList) + flatten(p)