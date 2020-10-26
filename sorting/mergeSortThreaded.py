import codeTimer
from concurrent.futures import ThreadPoolExecutor

def sortMergeThread(array, theadDepth=2):
    length = len(array)

    if length <= 1:
        return array

    if theadDepth < 1:
        leftHalf = sortMergeThread(array[0:length//2])
        rightHalf = sortMergeThread(array[length//2:])
    else:
        with ThreadPoolExecutor() as executor:
            future = executor.submit(sortMergeThread, array[0:length//2], theadDepth-1)
            rightHalf = sortMergeThread(array[length//2:])
            leftHalf = future.result()

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
