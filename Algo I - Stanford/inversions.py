#!/usr/bin/env python

"""
    Reads the input from an array/text and return the number of inversions.
    let i, j => array indices
    An inversion is number of pairs (i,j) where i < j
"""

def readInput():

    arr = []

    return arr

def splitInHalf(A):
    half = len(A)/2
    # from stackoverflow:
    #f = lambda A, n=3: [A[i:i+n] for i in range(0, len(A), n)]
    #f(A)
    return A[:half],A[half:]

def inversionCount():

    A = readInput()

    if not A:
        print "The input array is empty"

    lenA = len(A)

    if lenA == 0:
        return 0
    else:
        halfA = lenA/2
        left , right = splitInHalf(A)

        leftCount= Count(left,halfA)
        rightCount= Count(right,halfA)
        splitCount= CountSplit(A,lenA)


    A = []
    lenA = 0
    return leftCount + rightCount + splitCount

def Count():

    count = 0

    return count

def CountSplit():

    count = 0

    return count

