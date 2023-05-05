#!/usr/bin/python3
'''
minimum operations
''' 

def minOperations(n):
    if n == 1:
        return 0
    if n < 1:
        return 0
    operations = 0
    i = 2
    while i <= n:
        while n % i == 0:
            operations += 2
            n //= i
        i += 1
    return operations
