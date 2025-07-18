import sortVisualizer as sv
from sortingAlgorithms import SortingAlgorithmType

def main():
    try:
        width = 1920
        height = 1080
        fullscreen = True
        sizeOfData = 100
        algorithmType = SortingAlgorithmType.RADIX_SORT
        visualDataOffset = 0
        delayBetweenFrames = 10

        visualizer = sv.SortingVisualizer(SCREEN_WIDTH = width, SCREEN_HEIGHT = height, FULLSCREEN = fullscreen, DATA_SIZE = sizeOfData, SORTING_ALGORITHM_TYPE = algorithmType, OFFSET = visualDataOffset, DELAY = delayBetweenFrames)

        visualizer.run()
    except Exception as e:
        print(f"An Error has accured: {e}")

main()

