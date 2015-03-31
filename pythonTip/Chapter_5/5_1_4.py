#!usr/bin/env python

matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
]

re_matrix = [[row[i] for row in matrix] for i in range(4)]

print re_matrix

print "Test function <zip>"

print list(zip(*matrix))
