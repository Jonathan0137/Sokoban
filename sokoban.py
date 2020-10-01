import pygame
from menu import *
from inGame import *
from worker import worker
from Level import Level


"""Dynamic Function calling"""
def draw_game_based_on_status(status, window):
    arg = window
    if (len(status.split("/")) == 2):
        arg = [window, status.split("/")[1]]
        status = status.split("/")[0]
    
    return game_status_dictionary[status](arg)

def initWindow():
    json_file = open("env.json", "r")
    options_dict = json.load(json_file)
    if(options_dict["resolution"] == "Fullscreen"):
        window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        x = int(options_dict["resolution"].split("x")[0])
        y = int(options_dict["resolution"].split("x")[1])
        window = pygame.display.set_mode((x, y))
    return window


pygame.init()

window = initWindow()

pygame.display.set_caption("Sokoban")

game_status_dictionary = {
    "MainMenu" : mainMenuScreen,
    "InGame" : inGameScreen
}

clock = pygame.time.Clock()


game_status = "MainMenu"
while game_status != "exit":
    clock.tick(27) #refresh rate
    game_status = draw_game_based_on_status(game_status, window) #load main menu
    




pygame.quit()