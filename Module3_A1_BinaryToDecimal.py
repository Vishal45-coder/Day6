# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 18:49:56 2020

@author: vishal
"""



def binaryToDecimal(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    print(decimal)     
      
  
# Driver code 
if __name__ == '__main__': 
    bi=int(input("enter a Binary value"))
    binaryToDecimal(bi)