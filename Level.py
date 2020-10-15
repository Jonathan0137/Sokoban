from pygame import image as img
import pygame
class Level(object):

    matrix = []     #stores matrix got from the txt file
    SimpleMatrix = []   #stores matrixs without first 2 line. Without player location and size of the matrix
    direction = "down"  #init direction for the sprite
    def __init__(self,level_num):
        """Constructor for class Level. Reads txt file given a level number
        Get content from thoes txt files and save them

        Args:
            level_num (int): level number
        """
        self.currentLevel = level_num   #set current level to the given level
        
        del self.matrix[:]  #delete previous level matrix
        del self.SimpleMatrix[:]    #delete previous level matrix
        # Create level
        f = open("level/"+str(level_num)+".txt", "r")
        for row in f.read().splitlines():
            self.matrix.append(list(row.split()))
        self.SimpleMatrix = self.matrix[2:]
        self.worker_location = (int(self.matrix[1][0]), int(self.matrix[1][1]))
        
    def getSimpleMatrix(self):
        """Get simple matrix

        Returns:
            [list[str]]: simple matrix
        """
        return self.SimpleMatrix

    def getCurrentLevel(self):
        """Get current level

        Returns:
            [int]: current level
        """
        return self.currentLevel

    def getWorkerLocation(self):
        """Get worker current location

        Returns:
            [tuple(int, int)]: return worker current location
        """
        return self.worker_location

    def updateWorkerLocation(self, x, y, direction):
        """Update worker location and it's direction

        Args:
            x (int): x corrd of worker 
            y (int): y corrd of worker
            direction (str): direction of worker
        """
        self.worker_location = (x, y)
        self.direction = direction

    def updateMatrixGivenSimpleMatrix(self, SimpleMatrix):
        """update matrix given simple matrix for function draw_level

        Args:
            SimpleMatrix ([list[str]]): updated simplematrix
        """
        self.matrix[2:] = SimpleMatrix

    def getUnPlacedBoxes(self, SimpleMatrix):   
        """this is used to find how many unplaced 
        boxes are left to determine if player pass the level or no

        Args:
            SimpleMatrix (list[str]): get the matrix and find number of boxes

        Returns:
            [int]: number of boxes are left in the matrix
        """
        count = 0
        for i in range(len(SimpleMatrix)):
            for j in range(len(SimpleMatrix[0])):
                if(SimpleMatrix[i][j] == '2'):
                    count = count + 1
        return count
    def draw_level_preview(self, window):
        """This is a function that draws preview level for the level select screen.

        Args:
            window (pygame.Surface): a place where we draw the game on
        """
        box_size = 40   #sprite is 64 by 64
        w, h = pygame.display.get_surface().get_size()

        if(int(self.matrix[0][1]) / int(self.matrix[0][0])) == 1:
            box_size = h // (int(self.matrix[0][0])*2)
        elif(int(self.matrix[0][1]) / int(self.matrix[0][0])) > 1:
            box_size = w // (int(self.matrix[0][0])*3)
        else:
            box_size = w // (int(self.matrix[0][1])*3)
        
        if (box_size > 64):
            box_size = 64
            
        self.draw_level(window, box_size)


    def draw_level(self, window, box_size):
        """Draw the level

        Args:
            window (pygame.Surface): a place where we draw the game on
            box_size (int): size of the object
        """
        #LOAD pictures
        box = img.load('pic/box.png')
        box_in_correct_location = img.load('pic/box_in_correct_location.png')
        ground = img.load('pic/ground.png')
        targetGround = img.load('pic/targetGround.png')
        wall = img.load('pic/wall.png')
        wall = pygame.transform.scale(wall, (box_size,box_size))
        box = pygame.transform.scale(box, (box_size,box_size))
        box_in_correct_location = pygame.transform.scale(box_in_correct_location, (box_size,box_size))
        ground = pygame.transform.scale(ground, (box_size,box_size))
        targetGround = pygame.transform.scale(targetGround, (box_size,box_size))

        images = {'0': ground, '1': wall, '2': box, '3': targetGround, '4': box_in_correct_location}

        startingCorr = self.findStartingCord(box_size)  #get the starting corrd to make sure the game is always center
        workerCorr = (startingCorr[0]+self.worker_location[0]*box_size , startingCorr[1]+self.worker_location[1]*box_size) #get the workers location

        # draw the game
        # Iterate all Rows
        for i in range (2, int(self.matrix[0][1])+2):
            # Iterate all columns of the row
            for c in range (0, int(self.matrix[0][0])):
                if(i == 2 and c == 0):# first block
                    window.blit(wall, startingCorr)
                elif(startingCorr[0] + c*box_size == workerCorr[0] and startingCorr[1] + (i-2)*box_size == workerCorr[1]): # add worker
                    window.blit(ground, workerCorr) #put ground first
                    self.workerSprite(window, self.direction, workerCorr, box_size) # add worker
                elif(self.matrix[i][c] == '3'):
                    window.blit(ground, (startingCorr[0] + c*box_size, startingCorr[1] + (i-2)*box_size))
                    window.blit(images[self.matrix[i][c]], (startingCorr[0] + c*box_size, startingCorr[1] + (i-2)*box_size))
                else:
                    window.blit(images[self.matrix[i][c]], (startingCorr[0] + c*box_size, startingCorr[1] + (i-2)*box_size))
        pygame.display.update()

    def workerSprite(self, window, direction, workerCorr, box_size):
        """Draw worker onto the game

        Args:
            window (pygame.Surface): window to draw on
            direction (str): user input to find out which sprite to use
            workerCorr (tuple): worker location to draw on
        """
        worker_down = img.load('pic/worker_down.png')
        worker_left = img.load('pic/worker_left.png')
        worker_right = img.load('pic/worker_right.png')
        worker_up = img.load('pic/worker_up.png')
        worker_down = pygame.transform.scale(worker_down, (box_size,box_size))
        worker_left = pygame.transform.scale(worker_left, (box_size,box_size))
        worker_right = pygame.transform.scale(worker_right, (box_size,box_size))
        worker_up = pygame.transform.scale(worker_up, (box_size,box_size))

        if (direction == "up"):
            window.blit(worker_up, workerCorr)  #if user press up arrow we should have a sprite where worker is moving upward
        elif (direction == "down"):
            window.blit(worker_down, workerCorr) #if user press down arrow we should have a sprite where worker is moving down
        elif (direction == "left"):
            window.blit(worker_left, workerCorr) #if user press left arrow we should have a sprite where worker is moving left
        else:
            window.blit(worker_right, workerCorr) #if user press right arrow we should have a sprite where worker is moving right

    
    def LevelComplete(self): 
        """Check if user have completed the level or not

        Returns:
            [boolean]: return True if game is done. None otherwise
        """
        if self.getUnPlacedBoxes(self.getSimpleMatrix()) == 0:
            return True


    def findStartingCord(self, box_size):
        """find the starting location of the game to load 
        given current size of the screen to make sure it is always center

        Args:
            box_size (int): [size of the object]

        Returns:
            [tuple[float]]: [Starting location of the game]
        """
        w, h = pygame.display.get_surface().get_size()
        
        game_row = int(self.matrix[0][0])/2 
        game_col = int(self.matrix[0][1])/2 

        game_midpoint = (game_row, game_col)
        startingCorr = (w/2 - game_row*box_size, h/2 - game_col*box_size)

        return startingCorr
