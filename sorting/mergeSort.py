import codeTimer

def sort(array):
    length = len(array)

    if length <= 1:
        return array

    leftHalf = sort(array[0:length//2])
    rightHalf = sort(array[length//2:])

    print('compare:  ', leftHalf, " | ", rightHalf)

    newlist = []
    while len(leftHalf) > 0 and len(rightHalf) > 0:
        if leftHalf[0] < rightHalf[0]:
            newlist.append(leftHalf.pop(0))
        else:
            newlist.append(rightHalf.pop(0))
        
    for i in leftHalf:
        newlist.append(i)
    
    for i in rightHalf:
        newlist.append(i)

    print("result: ", newlist)
    return newlist

codeTimer.time(sort, fileName="merge.csv", arrayLength=10, iterations=1)
