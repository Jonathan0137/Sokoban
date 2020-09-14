from pygame import image as img
import pygame
class Level(object):

    matrix = []
    def __init__(self,level_num):
        del self.matrix[:]
        # Create level
        f = open("level/"+str(level_num)+".txt", "r")
        for row in f.read().splitlines():
            self.matrix.append(list(row.split()))
        
    def printMatrix(self):
        print(self.matrix)

    def draw_level(self, window):
        #LOAD pictures
        box = img.load('pic/box.png')
        box_in_correct_location = img.load('pic/box_in_correct_location.png')
        ground = img.load('pic/ground.png')
        targetGround = img.load('pic/targetGround.png')
        wall = img.load('pic/wall.png')
        worker_down = img.load('pic/worker_down.png')
        worker_left = img.load('pic/worker_left.png')
        worker_right = img.load('pic/worker_right.png')
        worker_up = img.load('pic/worker_up.png')

        images = {'0': ground, '1': wall, '2': box, '3': targetGround, '4': box_in_correct_location}
        
        box_size = 64
        #Draw worker
        worker_location = ((int(self.matrix[1][0]))*box_size, (int(self.matrix[1][1]))*box_size)
        

        #Draw wall ground box and targetGround
        # Iterate all Rows
        for i in range (2, int(self.matrix[0][1])+2):
            # Iterate all columns of the row
            for c in range (0, int(self.matrix[0][0])):
                if(c*box_size == worker_location[0] and (i-2)*box_size == worker_location[1]):
                    window.blit(ground, worker_location)
                    window.blit(worker_down, worker_location)
                else:
                    window.blit(images[self.matrix[i][c]], (c*box_size, (i-2)*box_size))
        pygame.display.update()

    def screen_size(self):
        x = int(self.matrix[0][0])
        y = int(self.matrix[0][1])
        return (x * 64, y * 64)
