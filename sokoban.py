import pygame
from menu import *
from worker import worker
from Level import Level

"""Dynamic Function calling"""
def draw_game_based_on_status(status, arg):
    return game_status_dictionary[status](arg)

pygame.init()


pygame.init()
window = pygame.display.set_mode((1800, 1000))

pygame.display.set_caption("Sokoban")

currentLevel = 0
myLevel = Level(currentLevel)



run = True
while run:
    pygame.display.flip()
    clock = pygame.time.Clock()
    clock.tick(60) #refresh rate
    
    #run = mainMenu(window) #load main menu
    
    for event in pygame.event.get(): # exit button works
        if event.type == pygame.QUIT:
            run = False

        myLevel.draw_level(window) #level class
        myWorker = worker(myLevel)  #worker class

        keys = pygame.key.get_pressed()#get key presses

        if keys[pygame.K_UP]:
            myWorker.movePlayer("up", myLevel)
        elif keys[pygame.K_DOWN]:
            myWorker.movePlayer("down", myLevel)
        elif keys[pygame.K_LEFT]: 
            myWorker.movePlayer("left", myLevel)
        elif keys[pygame.K_RIGHT]:
            myWorker.movePlayer("right", myLevel)
        elif keys[pygame.K_1]: # restart button pressed
            myLevel = Level(currentLevel)
        elif keys[pygame.K_2]: # skip this level
            currentLevel = myLevel.getCurrentLevel() + 1
            print("Current Level = " + str(currentLevel))
            window = pygame.display.set_mode((1800, 1000))
            myLevel = Level(currentLevel)
        if(myLevel.LevelComplete() == True):
            print("LEVEL " + str(currentLevel) + " COMPLETE")
            currentLevel = myLevel.getCurrentLevel() + 1
            window = pygame.display.set_mode((1800, 1000))
            myLevel = Level(currentLevel)
        
pygame.quit()