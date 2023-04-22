#!/usr/bin/python3
''' Pascal Traingle '''


def pascal_triangle(n):

    if n <= 0:
        return []
    pas = [[] for c in range(n)]
    for row in range(n):
        for col in range(row + 1):
            if (col < row):
                if col == 0:
                    pas[row].append(1)
                else:
                    pas[row].append(pas[row-1][col] \
                            + pas[row-1][col-1])
            elif(col == row):
                pas[row].append(1)
    return pas
