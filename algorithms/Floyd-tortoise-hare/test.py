from findCycle import *
from random import randint

def FloydTest(test):
    entryPoint = findDupInArray(test)

    return entryPoint if entryPoint else 0


#10 tests
for x in range(1,20):
    n = 10
    array = [randint(1, n - 1) for y in range(n)]
    print('Test #' + str(x) + ' for array: ' + str(array) )
    result = FloydTest(array)
    if (result > 0):
        print('Found cycle entry point : ' + str(result))
    else:
        print('There is no duplicate in the array')
