# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 13:30:30 2017

@author: stanl
"""

class Bird(object):
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print('Aaaah ...')
            self.hungry = False
        else:
            print('No, thanks!')

#class Coordinate(object):
#    def __init__(self, x, y):
#        self.x= x
#        self.y= y
#    def distance(self, other):
#        x_diff_sq= (self.x-other.x)**2
#        y_diff_sq= (self.y-other.y)**2
#        return (x_diff_sq+y_diff_sq)**0.5