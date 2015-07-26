#!/usr/bin/env python

"""
    Reads the input from an array/text and returns List of integers
    and the length of the list
"""

def readInput(filename):
    file = open(filename, "r") #read-only
    test_list = file.read().split('\n') #returns a list of strings
    file.close()
    testList = [int(x) for x in test_list]
    # print len(testList) > 0 #array is too large to print in PyCharm
    return testList, len(testList)