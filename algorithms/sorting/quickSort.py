#!/usr/bin/env python

"""
    1. Reads the input from an array/text
    2. Counts the number of comparison depending on pivot selected
    3.
"""
from main import readInput

test,n= readInput("QuickSort.txt")

#add m - 1  where m is length of subarray
def sortThis(A):
    n = len(A) - 1
    quickSort(A, 0, n)

def quickSort(A,start, n):

    #Partition A around pivot
    if n > start:
        pivot_index = partition(A,start, n)
        #recursively sort 1st part
        quickSort(A,start,pivot_index - 1)
        quickSort(A,pivot_index + 1 ,n)

    return A

def get_pivot(A,low, hi):
    mid = (hi - low)/2

    pivot = hi

    if A[low] < A[mid]:
        if A[mid] < A[hi]:
            pivot = mid
    elif A[low] < A[hi]:
        pivot = low
    return pivot

def partition(A,start,n):

    if n <= 1: return A

    pivot = get_pivot(A,start,n)
    A[0], A[pivot] = A[pivot] , A[0] #puts

    p = A[pivot]
    i, j = start + 1, start + 1

    while j <= n - 1:
        if A[j] < p:
            A[j] ,A[i] = A[i] ,A[j]
            i +=1
        j +=1

    if (i - 1 > 0) :
        A[pivot], A[i-1] = A[i-1], A[pivot]



    return i-1
#Tests
test2 = [3,8,2,5,1,4,7,6]
n2 = len(test2)
print sortThis(test2)