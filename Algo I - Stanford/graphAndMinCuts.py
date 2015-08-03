#!/usr/bin/env python

"""
    Reads the input from an array/text and return the number of minimum number of crossing edges.
    Uses the Randomized contraction algorithm
"""

from main import readGraphInput
import random
import math
import copy

def countMinCuts(graph):
    graph2 = graph
    minCutCount = 0
    if len(graph2) <= 2:
        return graph2, minCutCount
    else:
        # choose random edge
        graph2 = {}
        minCutCount = 0
        # contract edges into single vertex
        #remove self-loops

    return graph2,minCutCount

#TESTS
graph_dict = readGraphInput("kargerMinCut.txt")