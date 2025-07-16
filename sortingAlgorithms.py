import numpy as np
from enum import Enum

class SortingAlgorithmType(Enum):
    INSERTION_SORT = 1
    QUICK_SORT = 2
    RADIX_SORT = 3
    MERGE_SORT = 4
    HEAP_SORT = 5

class SortingData:
    def __init__(self):
        self.data: list = []
        self.isSorted: bool = False     # Always ascending order
        self.algorithmType: SortingAlgorithmType = SortingAlgorithmType.INSERTION_SORT

    def createData(self, size: int) -> None:

        self.data.clear()

        for i in range(0, size):
            self.data.append(i)
        self.isSorted = True

    
    def createAndRandomizeData(self, size: int) -> None:
        
        self.data.clear()

        for i in range(0, size):
            self.data.append(i)

        np.random.shuffle(self.data)
        self.isSorted = self.checkIfSorted()

    def shuffleData(self) -> None:
        np.random.shuffle(self.data)
        self.isSorted = self.checkIfSorted()

    def Sort(self, sortingVisualizer) -> None:

        match self.algorithmType:

            case SortingAlgorithmType.INSERTION_SORT:
                self.instertionSort(sortingVisualizer)

            case SortingAlgorithmType.QUICK_SORT:
                self.quickSort(self.data, 0, len(self.data) - 1, sortingVisualizer)
            
            case SortingAlgorithmType.RADIX_SORT:
                self.radixSort(self.data, sortingVisualizer)

            case SortingAlgorithmType.MERGE_SORT:
                self.mergeSort(self.data, sortingVisualizer)
            
            case SortingAlgorithmType.HEAP_SORT:
                self.heapSort(self.data, sortingVisualizer)

    def instertionSort(self, sortingVisualizer) -> None:

        for i in range(1, len(self.data)):      # Start from the second element: Needs at least one element to compare with
            currentItem = self.data[i]          # safe item to compare through the list
            itemUnderIndex = i - 1              # index of the item under the current item

            # loop through the list backwards until we find an item that is smaller than the current item
            while itemUnderIndex >= 0 and currentItem < self.data[itemUnderIndex] and sortingVisualizer.running == True:
                # swap the current item with the item under it
                # "= self.data[itemUnderIndex + 1] ..." could be exchanged with "= currentItem ..." since we always swap the current item with the item under it
                self.data[itemUnderIndex], self.data[itemUnderIndex + 1] = self.data[itemUnderIndex + 1], self.data[itemUnderIndex]
                # continue to the next item under the current item
                itemUnderIndex -= 1
                sortingVisualizer.drawFrameWithDelay()

            if(sortingVisualizer.running == False):     # if the user has closed the window, we stop sorting
                return
        self.isSorted = True

    def quickSort(self, array, start, end, sortingVisualizer):

        if start >= end or sortingVisualizer.running == False:  # if we are at the end of the array or the user has closed the window, we stop sorting
            return

        p = self.partition(array, start, end, sortingVisualizer)
        self.quickSort(array, start, p-1, sortingVisualizer)
        self.quickSort(array, p+1, end, sortingVisualizer)
        self.isSorted = True

    def partition(self, array, start, end, sortingVisualizer):
        pivot = array[start]
        low = start + 1
        high = end

        while sortingVisualizer.running == True:
            sortingVisualizer.drawFrameWithDelay()
            while low <= high and array[high] >= pivot:
                high = high - 1

            while low <= high and array[low] <= pivot:
                low = low + 1

            if low <= high:
                array[low], array[high] = array[high], array[low]
            else:
                break

        array[start], array[high] = array[high], array[start]

        return high
    
    def radixSort(self, arr, sortingVisualizer):
        max1 = max(arr)
        exp = 1
        while max1 / exp > 0 and sortingVisualizer.running == True:
            self.countingSort(arr, exp, sortingVisualizer)
            exp *= 10
        self.isSorted = True

    def countingSort(self, arr, exp1, sortingVisualizer):
        n = len(arr)
        output = [0] * (n)
        count = [0] * (10)

        for i in range(0, n):
            index = (arr[i] / exp1)
            count[int(index % 10)] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = (arr[i] / exp1)
            output[count[int(index % 10)] - 1] = arr[i]
            count[int(index % 10)] -= 1
            i -= 1

        i = 0
        for i in range(0, len(arr)):
            if sortingVisualizer.running == False:
                return
            sortingVisualizer.drawFrameWithDelay()
            arr[i] = output[i]
    
    def mergeSort(self, arr, sortingVisualizer):
        sortingVisualizer.drawFrameWithDelay()
        if len(arr) > 1 and sortingVisualizer.running == True:
            
            mid = len(arr)//2
            L = arr[:mid]
            R = arr[mid:]

            self.mergeSort(L, sortingVisualizer)
            self.mergeSort(R, sortingVisualizer)

            i = j = k = 0

            while i < len(L) and j < len(R):
                sortingVisualizer.drawFrameWithDelay()
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        self.isSorted = True
            
    def heapSort(self, arr, sortingVisualizer):
        n = len(arr)

        for i in range(n//2, -1, -1):
            if sortingVisualizer.running == False:
                return
            
            self.heapify(arr, n, i, sortingVisualizer)


        for i in range(n-1, 0, -1):
            if sortingVisualizer.running == False:
                return
            
            arr[i], arr[0] = arr[0], arr[i]

            self.heapify(arr, i, 0, sortingVisualizer)

            if self.checkIfSorted() == True:
                return   
    
    def heapify(self, arr, n, i, sortingVisualizer):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest, sortingVisualizer)
        sortingVisualizer.drawFrameWithDelay()

    # Checks if the data is sorted in ascending order
    def checkIfSorted(self) -> bool:
        print("Checking if sorted")
        for i in range(1, len(self.data)):
            if self.data[i] < self.data[i - 1]:
                self.isSorted = False
                return False
        self.isSorted = True
        return True
    