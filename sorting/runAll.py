from codeTimer import time
from mergeSort import sortMerge
from mergeSortThreaded import sortMergeThread
from selectionSort import sortSelection
from csv import writer, QUOTE_MINIMAL

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


if __name__ == "__main__":
    arraylength = 5000
    with open('sortingData.csv', 'w') as file:
        csvWriter = writer(file, delimiter=',',quotechar='|', quoting=QUOTE_MINIMAL)

        with ProcessPoolExecutor() as executor:
            selectionFuture = executor.submit(time, sortSelection, fileName="selection.csv", arrayLength=arraylength, iterations=1, recursionlimit=arraylength)
            mergeFuture = executor.submit(time, sortMerge, fileName="merge.csv", arrayLength=arraylength, iterations=1)
            mergeThreadFuture = executor.submit(time, sortMergeThread, fileName="mergeThreaded.csv", arrayLength=arraylength, iterations=1)

            top = range(arraylength+1)
            csvWriter.writerow(top)

            selectionData = ["selection"] + selectionFuture.result()
            mergeData = ["merge"] + mergeFuture.result()
            mergeThreadData = ["mergeThread"] + mergeThreadFuture.result()

            csvWriter.writerow(selectionData)
            csvWriter.writerow(mergeData)
            csvWriter.writerow(mergeThreadData)




            