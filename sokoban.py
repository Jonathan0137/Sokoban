import pygame
from menu import *

from worker import worker
from Level import Level
pygame.init()

window = pygame.display.set_mode((1800, 1000))

pygame.display.set_caption("Sokoban")



clock = pygame.time.Clock()

man = worker(300, 410, 64, 64)

run = True
while run:
    
    clock.tick(27) #refresh rate
    #run = mainMenu(window) #load main menu
    
    for event in pygame.event.get(): # exit button works
        if event.type == pygame.QUIT:
            run = False

    myLevel = Level(0)
    myLevel.draw_level(window)
          


    keys = pygame.key.get_pressed()#get key presses


pygame.quit()