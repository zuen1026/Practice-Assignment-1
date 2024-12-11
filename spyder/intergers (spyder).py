# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 21:03:53 2024

@author: leejo
"""
# print integers between 1 and 10
def print_numbers(n):
    if n <= 10:
        print(n)
        print_numbers(n + 1)

print_numbers(1)

# Printing integers from 1 to 10
for i in range(1, 11):
    print(i) 
    
