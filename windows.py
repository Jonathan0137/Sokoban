import pygame
import json


def initWindow():
    """Create a new pygame surface object and return it

    Returns:
        window (pygame.Surface): window to draw on
    """
    json_file = open("env.json", "r")
    options_dict = json.load(json_file)
    if(options_dict["resolution"] == "Fullscreen"):
        window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    else:
        x = int(options_dict["resolution"].split("x")[0])
        y = int(options_dict["resolution"].split("x")[1])
        window = pygame.display.set_mode((x, y))

    return window

def resizeWindow(window):
    """Change the windows size base on the env.json

    Args:
        window (pygame.Surface): window to draw on
    """
    json_file = open("env.json", "r")
    options_dict = json.load(json_file)
    if(options_dict["resolution"] == "Fullscreen"):
        window = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    else:
        x = int(options_dict["resolution"].split("x")[0])
        y = int(options_dict["resolution"].split("x")[1])
        window = pygame.display.set_mode((x, y))