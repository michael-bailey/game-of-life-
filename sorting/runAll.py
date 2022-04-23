from codeTimer import time
from mergeSort import sortMerge
from mergeSortThreaded import sortMergeThread
from selectionSort import sortSelection
from csv import writer, QUOTE_MINIMAL
from randomListGen import genRandomList

from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

if __name__ == "__main__":
    lowBound = 0
    upperBound = 5000

    iterations = 2
    with open('sortingData.csv', 'w') as file:
        csvWriter = writer(file, delimiter=',',quotechar='|', quoting=QUOTE_MINIMAL)

        head = ["arraylength"]
        selectionData = ["selection"]
        mergeData = ["merge"]
        mergeThreadData = ["merge thread"]
        pythonSortData = ["default sort function"]

        with ProcessPoolExecutor() as executor:

            selection_futures = []
            merge_futures = []
            merge_thread_futures = []

            for i in range(lowBound,upperBound):
                data = genRandomList(i)
                selectionFuture = executor.submit(time, sortSelection, fileName="selection.csv", arrayLength=i, iterations=iterations, recursionlimit=i, data=data)
                mergeFuture = executor.submit(time, sortMerge, fileName="merge.csv", arrayLength=i, iterations=iterations, data=data)
                mergeThreadFuture = executor.submit(time, sortMergeThread, fileName="mergeThreaded.csv", arrayLength=i, iterations=iterations, data=data)
                

                head.append(i)
                selection_futures.append(selectionFuture)
                merge_futures.append(mergeFuture)
                merge_thread_futures.append(mergeThreadFuture)

            for i in selection_futures:
                selectionData.append(i.result()[0])

            for i in merge_futures:
                mergeData.append(i.result()[0])

            for i in merge_thread_futures:
                mergeThreadData.append(i.result()[0])

            

            csvWriter.writerow(head)
            csvWriter.writerow(selectionData)
            csvWriter.writerow(mergeData)
            csvWriter.writerow(mergeThreadData)


            