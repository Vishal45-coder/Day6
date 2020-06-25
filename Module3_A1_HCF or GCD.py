# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:05:45 2020

@author: vishal
"""

def findgcd(num1, num2):
    if(num1 == 0):
        print("\n HCF of {0} and {1} = {2}".format(a, b, b))

    while(num2 != 0):
        if(num1 > num2):
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1

a = float(input(" Please Enter the First Value a: "))
b = float(input(" Please Enter the Second Value b: "))

gcd = findgcd(a, b)  
print("\n HCF of {0} and {1} = {2}".format(a, b, gcd))