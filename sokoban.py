import pygame
from menu import *

from worker import worker
from Level import Level

"""Dynamic Function calling"""
def draw_game_based_on_status(status, arg):
    return game_status_dictionary[status](arg)

pygame.init()

window = pygame.display.set_mode((1800, 1000))

pygame.display.set_caption("Sokoban")

game_status_dictionary = {
    "MainMenu" : mainMenuScreen,
    "Options" : optionsScreen,
    #"GameMenu" : gameMenuScreen,
    #"LevelSelect" : levelSelectScreen,
    #"InGame" : inGameScreen
}

clock = pygame.time.Clock()

man = worker(300, 410, 64, 64)

game_status = "MainMenu"
while game_status != "exit":
    clock.tick(27) #refresh rate
    game_status = draw_game_based_on_status(game_status, window) #load main menu



pygame.quit()