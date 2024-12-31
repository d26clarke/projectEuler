#!/usr/bin/python

# https://projecteuler.net/problem=2

#Generate a list even fibonacci numbers
#Author:  Derrick Clarke
About Python Lists
"""
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets

List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index[0] the second item has index[1] the last item has index[-1] to get next to the last item index[-2]

Since lists are indexed, lists can have items with the same value
"""

def build_fibonacci_sequence(limit: int):
    while True:
        fibo.append(fibo[-1]+fibo[-2])
        if fibo[-1]>limit:        return

#Setup Logging 
import logging

fibo=[1,2]

build_fibonacci_sequence(4000000)

print( sum(filter(lambda x:x%2==0,fibo)) )
