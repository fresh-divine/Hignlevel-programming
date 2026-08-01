#!/usr/bin/
"""a module that displays number divisible by itself and one"""

for n in range(2, 51):
    is_prime=True
    for m in range(2, n):
        if n % m==0:
            is_prime=False
            break
    if is_prime:
        print(n, end=", ")
    
        

