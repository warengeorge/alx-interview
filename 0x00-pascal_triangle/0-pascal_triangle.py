#!/usr/bin/python3
""" pascal triangle
"""

def pascal_triangle(n):
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]
    pascal = [[1], [1, 1]]
    for i in range(2, n):
        pascal.append([1])
        for j in range(1, i):
            pascal[i].append(pascal[i - 1][j - 1] + pascal[i - 1][j])
        pascal[i].append(1)
    return pascal
