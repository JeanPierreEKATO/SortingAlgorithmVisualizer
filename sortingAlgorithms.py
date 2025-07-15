import numpy as np
from enum import Enum

class SortingAlgorithmType(Enum):
    INSERTION_SORT = 1

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
            # case SortingAlgorithmType.BUBBLE_SORT:
            #     self.bubbleSort(sortingVisualizer)
            # ...weitere Algorithmen...

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

            if(sortingVisualizer.running == False):
                return
        self.isSorted = True

    

    # Checks if the data is sorted in ascending order
    def checkIfSorted(self) -> bool:
        for i in range(1, len(self.data)):
            if self.data[i] < self.data[i - 1]:
                self.isSorted = False
                return False
        self.isSorted = True
        return True
    
    
