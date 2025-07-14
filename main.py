import sortVisualizer as sv
from sortingAlgorithms import SortingAlgorithmType

def main():
    visualizer = sv.SortingVisualizer()
    visualizer.sortingData.createAndRandomizeData(10)
    visualizer.sortingData.algorithmType = SortingAlgorithmType.INSERTION_SORT

    visualizer.run()

main()

