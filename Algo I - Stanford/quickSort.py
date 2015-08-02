#!/usr/bin/env python

"""
    1. Reads the input from an array/text
    2. Counts the number of comparison depending on pivot selected
    3.
"""

from main import readInput

test,n= readInput("QuickSort.txt")
#print n


#add m - 1  where m is length of subarray

def quickSort(A,n):
    comparisons,l,r = 0,0,0

    if n <= 1:
        return A

    pivot_index = chosingPivot(A,l,r)
    #print pivot

    #Partition A around pivot
    A = partition(A,pivot_index,n)

    #recursively sort 1st part
    if pivot_index > 1:
        comparisons += (r - l) + pivot_index
        quickSort(A,l,r)
    else:
        #return sorted array with python
        A.sort()


    return A,comparisons

def chosingPivot(A,l,r):
    index = 0
    return index

def partition(A,pivot_index,n):
    p = A[pivot_index]
    i, j = pivot_index + 1, pivot_index + 1
    n -= 1

    while j <= n:
        if A[j] < p:
            A[j] ,A[i] = A[i] ,A[j]
            i +=1
        j +=1
    A[pivot_index], A[i-1] = A[i-1], A[pivot_index]

    return A

def Sort(L):





    return A


#Tests
test2 = [3,8,2,5,1,4,7,6]
n2 = len(test2)
quickSort(test2, n2)