from csv import writer, QUOTE_MINIMAL
from timeit import timeit
from randomListGen import genRandomList

def time(function, fileName="changeme.csv", arrayLength=100, iterations=1, recursionlimit=1000):

    import sys

    sys.setrecursionlimit(recursionlimit)

    attemptlist = ["attempt"]
    testTimes = ["time"]

    for i in range(arrayLength):
        print(i)
        randList = genRandomList(i)
        print(randList)
        attemptlist.append(i)
        testTimes.append(timeit(lambda: function(randList), number=iterations))
        print(testTimes[-1])

    with open(fileName, "w", newline='') as File:
        output = writer(File, delimiter=',', quotechar='|', quoting=QUOTE_MINIMAL)
        output.writerow(attemptlist)
        output.writerow(testTimes)