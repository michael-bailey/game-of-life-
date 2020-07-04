from timeit import timeit
from randomListGen import genRandomList

def time(function, fileName="changeme.csv", arrayLength=100, iterations=1, recursionlimit=1000, data=None):

    import sys

    sys.setrecursionlimit(recursionlimit+100)

    attemptlist = ["attempt"]
    testTimes = []

    if data == None:
        for i in range(arrayLength):
            print(i)
            randList = genRandomList(i)
            # print(randList)
            attemptlist.append(i)
            testTimes.append(timeit(lambda: function(randList), number=iterations))
            print(testTimes[-1])
    else:
        attemptlist.append(1)
        testTimes.append(timeit(lambda: function(data), number=iterations))
    
    return testTimes