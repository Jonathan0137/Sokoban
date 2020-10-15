import pygame
from menu import *
from windows import *
from inGame import *
from worker import worker
from Level import Level
from soundeffect import *


"""Dynamic Function calling"""
def draw_game_based_on_status(status, window):
    arg = window
    if (len(status.split("/")) == 2):
        arg = [window, status.split("/")[1]]
        status = status.split("/")[0]
    
    return game_status_dictionary[status](arg)

pygame.init()

window = initWindow()
programIcon = pygame.image.load('pic/playerFace.png')

pygame.display.set_icon(programIcon)
pygame.display.set_caption("Sokoban")

game_status_dictionary = {
    "MainMenu" : mainMenuScreen,
    "InGame" : inGameScreen
}

clock = pygame.time.Clock()


game_status = "MainMenu"
while game_status != "exit":
    clock.tick(27) #refresh rate
    pygame.mixer.music.load("backgroundmusic.wav")
    musicCheck()
    game_status = draw_game_based_on_status(game_status, window) #load main menu
    




pygame.quit()