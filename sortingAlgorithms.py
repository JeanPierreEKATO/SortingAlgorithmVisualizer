import numpy as np
from enum import Enum

class SortingAlgorithmType(Enum):
    INSERTION_SORT = 1
    QUICK_SORT = 2

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

    # Checks if the data is sorted in ascending order
    def checkIfSorted(self) -> bool:
        for i in range(1, len(self.data)):
            if self.data[i] < self.data[i - 1]:
                self.isSorted = False
                return False
        self.isSorted = True
        return True
    
    
