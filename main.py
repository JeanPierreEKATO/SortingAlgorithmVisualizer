import sortVisualizer as sv
from sortingAlgorithms import SortingAlgorithmType

def main():
    visualizer = sv.SortingVisualizer()
    visualizer.sortingData.createAndRandomizeData(1000)
    visualizer.sortingData.algorithmType = SortingAlgorithmType.HEAP_SORT
    visualizer.offset = 0
    visualizer.delay = 1

    visualizer.run()

main()

