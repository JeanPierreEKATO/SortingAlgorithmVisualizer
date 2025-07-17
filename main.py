import sortVisualizer as sv
from sortingAlgorithms import SortingAlgorithmType

def main():
    visualizer = sv.SortingVisualizer()
    visualizer.sortingData.createAndRandomizeData(100)
    visualizer.sortingData.algorithmType = SortingAlgorithmType.QUICK_SORT
    visualizer.offset = 0
    visualizer.delay = 100

    visualizer.run()

main()

