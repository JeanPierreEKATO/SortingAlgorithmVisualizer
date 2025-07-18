import pygame
from sortingAlgorithms import SortingData
from sortingAlgorithms import SortingAlgorithmType


class SortingVisualizer:

    def __init__(self, SCREEN_WIDTH = 1920, SCREEN_HEIGHT = 1080, DATA_SIZE = 10, SORTING_ALGORITHM_TYPE = SortingAlgorithmType.INSERTION_SORT, OFFSET = 1, DELAY = 5):
        # Default pygame setup
        self.screenWidth: int = SCREEN_WIDTH
        self.screenHeight: int = SCREEN_HEIGHT
        self.screen: pygame.Surface | None = None
        self.display: pygame.Surface | None = None
        self.clock: pygame.time.Clock | None = None
        self.running: bool | None = None
        self.paused: bool | None = None

        # Default Sorting setup
        self.sortingData = SortingData(SORTING_ALGORITHM_TYPE)
        self.sortingData.createData(DATA_SIZE)
        self.sortingData.shuffleData()

        # Default Drawing Setup
        self.barWidth: float | None = None
        self.barMaxHeight: float | None = None
        self.offset: float = OFFSET  # Distance between the bars
        self.delay: int = DELAY  # Delay in milliseconds for each frame
    
    def run(self):
        self.Init()

        self.Loop()

        self.Quit()

    def Init(self):
        self.initPygameSetup()
        #Note: There is no "initSortingSetup()" Method needed, since its dynamic, has default values and can be altered by the user befor the run() method is called => should not be altered here
        self.initDrawingSetup()  

    def initPygameSetup(self):
        pygame.init()
        #Note: self.screenWidth is dynamic, has default value of 1920 and can be altered by the user befor the run() method is called => should not be altered here
        #Note: self.screenHeight is dynamic, has standard value of 1000 and can be altered by the user befor the run() method is called => should not be altered here
        self.screen = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.display = pygame.display
        self.clock = pygame.time.Clock()
        self.running = True
        self.paused = False

    def initDrawingSetup(self):

        self.barWidth = self.screen.get_width() / len(self.sortingData.data)
        self.barMaxHeight = max(self.sortingData.data) * 1.0 # Adds a little margin to the max height if > 1.0
        #Note: self.offset is dynamic, has default value of 1 and can be altered by the user befor the run() method is called => should not be altered here
        #Note: self.delay is dynamic, has standard value of 5 and can be altered by the user befor the run() method is called => should not be altered here
    
    def Loop(self):
        while self.running:

            self.eventPolling()

            self.drawSorting()

            self.drawFrame()        
    
    def eventPolling(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.pause()
    
    def pause(self):

        self.paused = True

        while self.paused == True:
           for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.paused = False
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.paused = False

    def drawSorting(self):
        while self.sortingData.isSorted == False and self.running == True:

            self.sortingData.Sort(self)

    def drawFrame(self):
        self.screen.fill("black")
        self.drawDataset()
        self.display.flip()

    def drawFrameWithDelay(self):
        self.eventPolling()
        self.drawFrame()
        pygame.time.delay(self.delay)
        

    def drawDataset(self):
        for idx, value in enumerate(self.sortingData.data):
            x = idx * self.barWidth
            barHeight = int((value / self.barMaxHeight) * self.screen.get_height())
            y = self.screen.get_height() - barHeight
            pygame.draw.rect(self.screen, (0, 255, 0), (x + self.offset, y, self.barWidth - self.offset, barHeight))

    def Quit(self):
        pygame.quit()


        
         

        
