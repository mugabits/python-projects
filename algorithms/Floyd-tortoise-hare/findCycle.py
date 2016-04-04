def findDupInArray(a):
    assert len(a) > 0

    n = len(a) - 1

    #both start at the end of array
    tortoise = n
    hare = n

    # Find loop
    while True:

        tortoise = a[tortoise]  #f(slow)
        hare = a[a[hare]]       #f(f(fast))

        if tortoise == hare:   #found loop
            break

    # Find entry point
    finder = n

    while True:
            tortoise = a[tortoise]
            finder = a[finder]

            if tortoise == finder:  #intersection
                return tortoise     #return dup
