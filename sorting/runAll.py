from codeTimer import time
from mergeSort import sortMerge
from mergeSortThreaded import sortMergeThread
from selectionSort import sortSelection
from csv import writer, QUOTE_MINIMAL
from randomListGen import genRandomList

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

if __name__ == "__main__":
    arraylength = 100000
    with open('sortingData.csv', 'w') as file:
        csvWriter = writer(file, delimiter=',',quotechar='|', quoting=QUOTE_MINIMAL)

        data = genRandomList(arraylength)

        with ProcessPoolExecutor() as executor:
            selectionFuture = executor.submit(time, sortSelection, fileName="selection.csv", arrayLength=arraylength, iterations=1, recursionlimit=arraylength, data=data)
            mergeFuture = executor.submit(time, sortMerge, fileName="merge.csv", arrayLength=arraylength, iterations=1, data=data)
            #mergeThreadFuture = executor.submit(time, sortMergeThread, fileName="mergeThreaded.csv", arrayLength=arraylength, iterations=1, data=data)

            selectionData = ["selection"] + selectionFuture.result()
            mergeData = ["merge"] + mergeFuture.result()
            #mergeThreadData = ["mergeThread"] + mergeThreadFuture.result()

            csvWriter.writerow(selectionData)
            csvWriter.writerow(mergeData)
            #csvWriter.writerow(mergeThreadData)