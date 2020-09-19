from pygame import image as img
import pygame
class Level(object):

    matrix = []
    SimpleMatrix = []
    direction = "down"
    def __init__(self,level_num):
        self.currentLevel = level_num
        
        del self.matrix[:]
        del self.SimpleMatrix[:]
        # Create level
        f = open("level/"+str(level_num)+".txt", "r")
        for row in f.read().splitlines():
            self.matrix.append(list(row.split()))
        self.SimpleMatrix = self.matrix[2:]
        self.worker_location = (int(self.matrix[1][0]), int(self.matrix[1][1]))
        
    def getSimpleMatrix(self):
        return self.SimpleMatrix

    def getCurrentLevel(self):
        return self.currentLevel

    def getWorkerLocation(self):
        return self.worker_location

    def updateWorkerLocation(self, x:int, y:int, direction:str):
        self.worker_location = (x, y)
        self.direction = direction

    def updateMatrixGivenSimpleMatrix(self, SimpleMatrix):
        self.matrix[2:] = SimpleMatrix

    def getUnPlacedBoxes(self, SimpleMatrix):
        count = 0
        for i in range(len(SimpleMatrix)):
            for j in range(len(SimpleMatrix[0])):
                if(SimpleMatrix[i][j] == '2'):
                    count = count + 1
        return count

    def draw_level(self, window):
        #LOAD pictures
        box = img.load('pic/box.png')
        box_in_correct_location = img.load('pic/box_in_correct_location.png')
        ground = img.load('pic/ground.png')
        targetGround = img.load('pic/targetGround.png')
        wall = img.load('pic/wall.png')

        images = {'0': ground, '1': wall, '2': box, '3': targetGround, '4': box_in_correct_location}
        box_size = 64
        startingCorr = self.findStartingCord(window, box_size)
        workerCorr = (startingCorr[0]+self.worker_location[0]*box_size , startingCorr[1]+self.worker_location[1]*box_size)

        # Iterate all Rows
        for i in range (2, int(self.matrix[0][1])+2):
            # Iterate all columns of the row
            for c in range (0, int(self.matrix[0][0])):
                if(i == 2 and c == 0):# first block
                    window.blit(wall, startingCorr)
                elif(startingCorr[0] + c*box_size == workerCorr[0] and startingCorr[1] + (i-2)*box_size == workerCorr[1]):
                    window.blit(ground, workerCorr)
                    self.workerSprite(window, self.direction, workerCorr)
                elif(self.matrix[i][c] == '3'):
                    window.blit(ground, (startingCorr[0] + c*box_size, startingCorr[1] + (i-2)*box_size))
                    window.blit(images[self.matrix[i][c]], (startingCorr[0] + c*box_size, startingCorr[1] + (i-2)*box_size))

                else:
                    window.blit(images[self.matrix[i][c]], (startingCorr[0] + c*box_size, startingCorr[1] + (i-2)*box_size))
        pygame.display.update()

    def workerSprite(self, window, direction, workerCorr):

        worker_down = img.load('pic/worker_down.png')
        worker_left = img.load('pic/worker_left.png')
        worker_right = img.load('pic/worker_right.png')
        worker_up = img.load('pic/worker_up.png')
        if (direction == "up"):
            window.blit(worker_up, workerCorr)
        elif (direction == "down"):
            window.blit(worker_down, workerCorr)
        elif (direction == "left"):
            window.blit(worker_left, workerCorr)
        else:
            window.blit(worker_right, workerCorr)

    
    def LevelComplete(self):
        if self.getUnPlacedBoxes(self.getSimpleMatrix()) == 0:
            return True


    def findStartingCord(self, window, box_size):

        w, h = pygame.display.get_surface().get_size()
        
        game_row = int(self.matrix[0][0])/2 
        game_col = int(self.matrix[0][1])/2 

        game_midpoint = (game_row, game_col)
        startingCorr = (w/2 - game_row*box_size, h/2 - game_col*box_size)

        return startingCorr




    #def screen_size(self):
        #x = int(self.matrix[0][0])
        #y = int(self.matrix[0][1])
        #return (x * 64, y * 64)
        
