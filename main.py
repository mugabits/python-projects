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



def readGraphInput(filename):
    with open(filename, "r") as rows:
        graph_dict = {}
        row_list = []
        for row in rows:
            row_list = row.strip().split("\t")
            graph_dict[int(row_list.pop(0))] = list(map(int,row_list[1:]))

    return graph_dict

