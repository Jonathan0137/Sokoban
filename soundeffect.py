import json
import pygame
    
    
def soundEffect():
    """This is a function that plays the box moving sound when a box is pushed
    """
    json_file = open("env.json", "r")
    options_dict = json.load(json_file)
    if(options_dict["sound_effects"] == "On"):
        move_box_sound = pygame.mixer.Sound("box_moving.wav")
        move_box_sound.play()


def soundVolumeCheck(sound_object):
    """This is a function that plays the button pressing sound when a button is pressed

    Args:
        sound_object (pygame.mixer): the sound
    """
    json_file = open("env.json", "r")
    options_dict = json.load(json_file)
    if(options_dict["sound_effects"] == "Off"):
        sound_object.set_volume(0)
    else:
        sound_object.set_volume(1)
