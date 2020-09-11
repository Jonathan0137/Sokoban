import pygame
from menu import *
from pygame import image as img
from worker import worker
pygame.init()



window = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First Game")

box = img.load('pic/box.png')
box_in_correct_location = img.load('pic/box_in_correct_location.png')
ground = img.load('pic/ground.png')
targetGround = img.load('pic/targetGround.png')
wall = img.load('pic/wall.png')
worker_down = img.load('pic/worker_down.png')
worker_left = img.load('pic/worker_left.png')
worker_right = img.load('pic/worker_right.png')
worker_up = img.load('pic/worker_up.png')

clock = pygame.time.Clock()

man = worker(300, 410, 64, 64)

run = True
while run:
    #refresh rate
    clock.tick(27)
    run = mainMenu(window)
    # exit button works
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #get key presses
    keys = pygame.key.get_pressed()


pygame.quit()