from timeit import timeit
from random import randint
from csv import writer, QUOTE_MINIMAL

numbers = [1,5,4,3,2,3,3,2,4,6,6,4,56,4335,44,6213,62,5724,82,417,258,14,96,2,514,2147,2586,147,286,14,5289,14,5,1,369,175,258,28]

def sort_one(array):

    if len(array) < 1:
        return []

    smallestNumber = array[0]
    smallestIndex = 0

    for i in range(len(array)):
        if array[i] < smallestNumber:
            smallestIndex = i
            smallestNumber = array[i]
    array[smallestIndex], array[0] = array[0], array[smallestIndex]
    newValue = array[0:1]
    solved = newValue + sort_one(array[1:])
    return solved

def genRandomList(size):
    a = []
    for i in range(size):
        n = randint(1,1000)
        a.append(n)
    return a

attemptlist = []
testTimes = []

for i in range(100):
    print(i)
    randList = genRandomList(i)
    print(randList)
    attemptlist.append(i)
    testTimes.append(timeit(lambda: sort_one(randList)))

with open("algorithm.csv", "w", newline='') as File:
    output = writer(File, delimiter=' ', quotechar='|', quoting=QUOTE_MINIMAL)
    output.writerow(attemptlist)
    output.writerow(testTimes)
