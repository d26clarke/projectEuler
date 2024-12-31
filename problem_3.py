#!/usr/bin/python

# https://projecteuler.net/problem=3
# Author: Derrick D. Clarke

import sympy

target = 600851475143

smallestPrimeFactor = 2

"""
To find factors for large numbers, the most efficient method is to use prime factorization - 
break down the number into its prime factors by repeatedly dividing it by the smallest prime number that divides it evenly, 
until you reach 1; then, all possible combinations of these prime factors will be the factors of the original number.

Step 1.
Divide the large number by 2, if it divides evenly, continue dividing the quotient by 2; if not, move to the next prime number (3).

Step 2.
Keep dividing the quotient by the next prime number (3, 5, 7, etc.) until you reach 1.

"""
while target>1:
    if target%smallestPrimeFactor==0:  #Divided Evenly
        target/=smallestPrimeFactor    #Set Target to newly derived quotient
    else:
        smallestPrimeFactor = sympy.nextprime(smallestPrimeFactor)   #Get the next prime

print(f"The Largest Prime Factor: {smallestPrimeFactor}")

