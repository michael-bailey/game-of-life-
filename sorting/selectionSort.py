import codeTimer

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

codeTimer.time(sort_one, fileName="merge.csv", arrayLength=10, iterations=1)
