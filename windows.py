import pygame
import json


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

def resizeWindow(window):
    json_file = open("env.json", "r")
    options_dict = json.load(json_file)
    if(options_dict["resolution"] == "Fullscreen"):
        window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        x = int(options_dict["resolution"].split("x")[0])
        y = int(options_dict["resolution"].split("x")[1])
        window = pygame.display.set_mode((x, y))
    
    return window