import codeTimer

def sortSelection(array):

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
    solved = newValue + sortSelection(array[1:])
    return solved
