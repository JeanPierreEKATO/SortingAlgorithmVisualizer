import pygame
from sortingAlgorithms import SortingData


class SortingVisualizer:

    def __init__(self):
        # pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1000))
        self.display = pygame.display
        self.clock = pygame.time.Clock()
        self.running = True

        # Default Sorting setup
        self.sortingData = SortingData()
        self.sortingData.createData(10)
        self.sortingData.shuffleData()

        # Drawing Setup
        self.barWidth: float
        self.maxHeight: float
        self.offset: float = 1  # Distance between the bars
        self.delay: int = 5  # Delay in milliseconds for each frame
    
    def run(self):
        self.Init()

        self.Loop()

        self.Quit()

    def Init(self):
        self.initDrawingSetup()  

    def initDrawingSetup(self):

        self.barWidth = self.screen.get_width() / len(self.sortingData.data)
        self.maxHeight = max(self.sortingData.data) * 1.0 # Adds a little margin to the max height
        self.offset     # Is dynamic, has standard value of 1 or can be altered by the user befor the run() method is called

    def Loop(self):
        while self.running:
            # poll for events
            self.eventPolling()

            self.drawSorting()

            self.drawFrame()        
    
    def eventPolling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False

    def drawSorting(self):
        while self.sortingData.isSorted == False and self.running == True:
            self.eventPolling() 

            self.sortingData.Sort(self)

    def drawFrame(self):
        self.screen.fill("black")
        self.drawDataset()
        self.display.flip()

    def drawFrameWithDelay(self):
        self.drawFrame()
        pygame.time.delay(self.delay)
        

    def drawDataset(self):
        for idx, value in enumerate(self.sortingData.data):
            x = idx * self.barWidth
            barHeight = int((value / self.maxHeight) * self.screen.get_height())
            y = self.screen.get_height() - barHeight
            pygame.draw.rect(self.screen, (0, 255, 0), (x + self.offset, y, self.barWidth - self.offset, barHeight))

    def Quit(self):
        pygame.quit()


        
         

        
