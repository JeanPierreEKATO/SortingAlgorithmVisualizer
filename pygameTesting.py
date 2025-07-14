# Example file showing a basic pygame "game loop"
import pygame
import sortingAlgorithms as sa

def main():
    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((1920, 1000))
    clock = pygame.time.Clock()
    running = True
    clock.tick(10)  # how often to update the screen (1 FPS for slow visualization)

    # Sorting setup
    sortingData = sa.SortingData()
    sortingData.createData(100)
    sortingData.shuffleData()   

    # Drawing Setup
    barWidth = screen.get_width() / len(sortingData.data)
    maxHeight = max(sortingData.data) * 1.0 # Adds a little margin to the max height
    offset = 1  # Distance between the bars

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE

        # Example: Draw the sorting data as vertical bars
        
        # update dataset one step here
        sortingData.instertionSort()
        
        # flip() the display to put your work on screen
        pygame.display.flip()
        clock.tick(10)


    pygame.quit()
    

def drawDataset(screen: pygame.surface, dataSet: sa.SortingData, barWidth: int, maxHeight: int, offset: int) -> None:
    for idx, value in enumerate(dataSet.data):
        x = idx * barWidth
        barHeight = int((value / maxHeight) * screen.get_height())
        y = screen.get_height() - barHeight
        pygame.draw.rect(screen, (0, 255, 0), (x + offset, y, barWidth - offset, barHeight))

main()
