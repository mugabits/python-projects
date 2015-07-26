#!/usr/bin/env python

"""
    Reads the input from an array/text and return the number of inversions.
    let i, j => array indices
    An inversion is number of pairs (i,j) where i < j
"""

from main import readInput

def inversionSortCount(A):
    #print "A: " + A.__str__()
    if not A:
        print "The input array is empty"

    lenA = len(A)
    #print "lenA: " + lenA.__str__()
    if lenA <= 1:
        return A, 0
    else:
        leftSorted, leftCount = inversionSortCount(A[:lenA/2])
        rightSorted, rightCount = inversionSortCount(A[lenA/2:])
        totalSorted, splitCount = MergeCountSplit(leftSorted, rightSorted)

    A = []
    lenA = 0
    return totalSorted, leftCount + rightCount + splitCount


def MergeCountSplit(L, R):
    C = []
    inversionCount = 0

    while len(L) >= 0 or len(R) >= 0:
    #if L or R:
        if len(L) == 0 or not L:
            C += R
            break
        elif len(R) == 0 or not R:
            C += L
            break
        elif L[0] <= R[0]:
            C.append(L.pop(0))
        else:
            C.append(R.pop(0))
            inversionCount += len(L)
    return C, inversionCount

    # #Option 2
    # lenA, lenB = len(sortedA), len(sortedB)
    # #print "len(sortedA): " + lenA.__str__()
    # #print "len(sortedB): " + lenB.__str__()
    # while i < lenA or j < lenB:
    #     k = min(sortedA[i],sortedB[j])
    #     print "min k: " + k.__str__()
    #     C.append(k)
    #     print "C: " + C.__str__()
    #     if k == sortedB[j]:
    #         j += 1
    #         inversionCount += lenA - i
    #     else:
    #         i += 1
    # #print inversionCount.__str__()
    # #print C
    # return C, inversionCount

def Solution(A):
    sortedC, invCount = inversionSortCount(A)
    return "inversion Count: " + invCount.__str__()


# TESTS
original, n1 = readInput("testInv1.txt")
test = [1, 3, 5, 2, 4, 6]
test2 = [1, 3, 4, 2]
n2 = len(test)

# inversionSortCount(original, n1)
print Solution(original)
