import json
import pygame
    
    
def soundEffect():
    json_file = open("env.json", "r")
    options_dict = json.load(json_file)
    if(options_dict["sound_effects"] == "On"):
        move_box_sound = pygame.mixer.Sound("box_moving.wav")
        move_box_sound.play()
