#!/usr/bin/python

# https://projecteuler.net/problem=1

#Find the sum of all the multiples of 3 or 5 below 1000
#Author:  Derrick Clarke
#The variable numberCounter holds the sum of the 
#  multiples of 3 and 5
#The function checkForMult3and5 receives an integer and 
#determines if the integer is a multiple of 3 or 5
#if true, the number is returned

#Setup Logging 
import logging

def checkForMult3and5 (idxValue: int) -> int:
    logging.basicConfig(level=logging.INFO)
    #print(f"Current value of x: {x}")
    if idxValue % 3 == 0 or idxValue % 5 == 0:
        #print(f"After Check Current value of x: {x}")
        return idxValue
    return 0

logging.info('Begin Processing...')
logging.basicConfig(level=logging.INFO)

numberCounter = 0
for x in range(1000):
    resultingNumber = checkForMult3and5(x)
    numberCounter += resultingNumber

print(f"The Total: {numberCounter}")
