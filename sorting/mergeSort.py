import codeTimer

def sortMerge(array):
    length = len(array)

    if length <= 1:
        return array

    leftHalf = sortMerge(array[0:length//2])
    rightHalf = sortMerge(array[length//2:])

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

    return newlist