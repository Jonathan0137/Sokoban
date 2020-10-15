"""THIS IS THE FUNCTION FOR THE MAIN MENU SCREEN"""
import pygame
import pygame_gui
import os
import json
from Level import *
from windows import *
from soundeffect import *


pygame.init()


def exitGame(window):
    """returns exit statement to exit menu stack
    Args:
        window (pygame.display): window to draw on
    """
    return "exit"

def level_select_menu(window):
    """draws level select menu on the given window
    Args:
        window (pygame.display): window to draw on
    """
    font = pygame.font.Font('freesansbold.ttf', 32)  
    level_select_txt = font.render("Level Select", True, (100, 100, 0))
    textRect1 = level_select_txt.get_rect()
    textRect1.center = (window.get_width()//2, window.get_height()//12)
    json_file = open("env.json", "r+")
    options_dict = json.load(json_file)
    button_sound_effect = pygame.mixer.Sound('buttonsfx.wav')
    soundVolumeCheck(button_sound_effect)

    index = 0
    entries = os.listdir('level/')
    number_of_levels = len(entries) - 1
    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))

    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((99* window.get_width()//128, 293*window.get_height()//320), (3*window.get_width()//16, window.get_height()//16)),
                                            text='Back',
                                            manager=manager)
    play_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//2 - 3*window.get_width()//32, 10*window.get_height()//12), (3*window.get_width()//16, window.get_height()//16)),
                                            text='Play',
                                            manager=manager)
    right_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((3*window.get_width()//4 - 3*window.get_width()//32, 10*window.get_height()//12), (3*window.get_width()//16, window.get_height()//16)),
                                            text='-->',
                                            manager=manager)
    left_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//4 - 3*window.get_width()//32, 10*window.get_height()//12), (3*window.get_width()//16, window.get_height()//16)),
                                            text='<--',
                                            manager=manager)
    
    font = pygame.font.Font('freesansbold.ttf', 32)  
    

    clock = pygame.time.Clock()
    while True: #THE LOOP THAT DOES THE CONSTANT USER INPUT CHECKS AND DRAWS
        pygame.time.delay(10) #This is the function that creates a time delay of x milliseconds
        time_delta = clock.tick(60)/1000.0

        current_level = "Level " + str(index)
        text = font.render(current_level, True, (255, 165, 0))
        textRect = text.get_rect()
        textRect.center = (window.get_width()//2, window.get_height()//6)

        #DRAWS THE SELECTED LEVEL
        
        myLevel = Level(index)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            #CHECKS BUTTON INPUT
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    button_sound_effect.play()
                    if event.ui_element == left_button:
                        index = index - 1
                        window.fill((211, 235, 217))
                        if index < 0:
                            index = number_of_levels
                    elif event.ui_element == right_button:
                        index = index + 1
                        window.fill((211, 235, 217))
                        if index > number_of_levels:
                            index = 0
                    elif event.ui_element == back_button:
                        return "back"
                    elif event.ui_element == play_button:
                        return "InGame/" + str(index)
            manager.process_events(event)
        window.fill((211, 235, 217))
        manager.update(time_delta)
        manager.draw_ui(window)
        window.blit(level_select_txt, textRect1)
        window.blit(text, textRect)
        myLevel.draw_level_preview(window) 
        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()


def mainMenuScreen(window):
    """draws main menu on the given window
    
    Args:
        window (pygame.display): window to draw on
    """
    sokoban_logo = pygame.image.load("pic\playerFace.png")
    image_rect = sokoban_logo.get_rect()
    image_rect.center = (window.get_width()//2, window.get_height()//4) 

    font = pygame.font.Font('freesansbold.ttf', 32)  
    sokoban_txt = font.render("SOKOBAN", True, (100, 100, 0))
    textRect = sokoban_txt.get_rect()
    textRect.center = (window.get_width()//2, window.get_height()//6)
    

    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))

    button_sound_effect = pygame.mixer.Sound('buttonsfx.wav')
    soundVolumeCheck(button_sound_effect)

    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//2 - window.get_width()//6, 6*window.get_height()//16), (window.get_width()//3, window.get_height()//8)),
                                             text='Start Game',
                                             manager=manager)

    option_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//2 - window.get_width()//6, 9*window.get_height()//16), (window.get_width()//3, window.get_height()//8)),
                                             text='Game Options',
                                             manager=manager)

    quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//2 - window.get_width()//6, 12*window.get_height()//16), (window.get_width()//3, window.get_height()//8)),
                                             text='Exit Game',
                                             manager=manager)

    button_to_status = {
        start_button : gameMenuScreen,
        option_button : optionsScreen,
        quit_button : exitGame
    }

    
    clock = pygame.time.Clock()


    while True: #THE LOOP THAT DOES THE CONSTANT USER INPUT CHECKS AND DRAWS
        pygame.time.delay(10) #This is the function that creates a time delay of x milliseconds

        time_delta = clock.tick(60)/1000.0
        

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            return "exit"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"


            #CHECKS BUTTON INPUT
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    button_sound_effect.play()
                    status_check = button_to_status[event.ui_element](window)
                    if status_check != "back":
                        return status_check
                    manager.set_window_resolution((window.get_width(), window.get_height()))
                    start_button.set_dimensions((window.get_width()//3, window.get_height()//8))
                    option_button.set_dimensions((window.get_width()//3, window.get_height()//8))
                    quit_button.set_dimensions((window.get_width()//3, window.get_height()//8))
                    start_button.set_position((window.get_width()//2 - window.get_width()//6, 6*window.get_height()//16))
                    option_button.set_position((window.get_width()//2 - window.get_width()//6, 9*window.get_height()//16))
                    quit_button.set_position((window.get_width()//2 - window.get_width()//6, 12*window.get_height()//16))
                    start_button.ui_container.set_dimensions((window.get_width(), window.get_height()))
                    option_button.ui_container.set_dimensions((window.get_width(), window.get_height()))
                    quit_button.ui_container.set_dimensions((window.get_width(), window.get_height()))
                    textRect.center = (window.get_width()//2, window.get_height()//6)
                    image_rect.center = (window.get_width()//2, window.get_height()//4)
                    soundVolumeCheck(button_sound_effect)
            manager.process_events(event)

        
        window.fill((211, 235, 217))
        window.blit(sokoban_txt, textRect)
        window.blit(sokoban_logo, image_rect)
        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()

    return "exit"


def optionsScreen(window):
    """draws option menu on the given window

    Args:
        window (pygame.display): window to draw on
    """
    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))

    button_sound_effect = pygame.mixer.Sound('buttonsfx.wav')
    json_file = open("env.json", "r+")
    options_dict = json.load(json_file)
    soundVolumeCheck(button_sound_effect)

    temp_list_screen_size = ["800x600", "1024x768", "Fullscreen"]

    font = pygame.font.Font('freesansbold.ttf', 32)  
    option_txt = font.render("Options", True, (100, 100, 0))
    textRect = option_txt.get_rect()
    textRect.center = (window.get_width()//2, window.get_height()//12)

        

    music_option_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//16, 3*window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                                text='Music: ' + options_dict["music"],
                                                manager=manager)

    sound_effects_option_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((9 * window.get_width()//16, window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                                text='Sound Effects: ' + options_dict["sound_effects"],
                                                manager=manager)

    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((9 * window.get_width()//16, 3*window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                                text='Back',
                                                manager=manager)
                                                
    window_resize_button = pygame_gui.elements.UIDropDownMenu(temp_list_screen_size, "SCREEN SIZE: " + options_dict["resolution"], relative_rect=pygame.Rect((window.get_width()//16, window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                                manager=manager)

    clock = pygame.time.Clock()

    while True: #THE LOOP THAT DOES THE CONSTANT USER INPUT CHECKS AND DRAWS
        pygame.time.delay(10) #This is the function that creates a time delay of x milliseconds
        time_delta = clock.tick(60)/1000.0
        json_file.seek(0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return "exit"


            #CHECKS BUTTON INPUT
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    button_sound_effect.play()
                    if event.ui_element == back_button:
                        return "back"
                    elif event.ui_element == sound_effects_option_button:
                        if options_dict["sound_effects"] == "On":
                            options_dict["sound_effects"] = "Off"
                            sound_effects_option_button.set_text("Sound Effects: Off")
                            button_sound_effect.set_volume(0)
                        else:
                            options_dict["sound_effects"] = "On"
                            sound_effects_option_button.set_text("Sound Effects: On")
                            button_sound_effect.set_volume(1)
                    elif event.ui_element == music_option_button:
                        if options_dict["music"] == "On":
                            options_dict["music"] = "Off"
                            music_option_button.set_text("Music: Off")
                        else:
                            options_dict["music"] = "On"
                            music_option_button.set_text("Music: On")
                        json.dump(options_dict, json_file)
                        json_file.truncate()
                        musicCheck()
                elif event.user_type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                    button_sound_effect.play()
                    options_dict["resolution"] = event.text
                    json.dump(options_dict, json_file)
                    json_file.truncate()
                    resizeWindow(window)
                    manager.set_window_resolution((window.get_width(), window.get_height()))
                    music_option_button.set_dimensions((6 * window.get_width()//16, window.get_height()//5))
                    sound_effects_option_button.set_dimensions((6 * window.get_width()//16, window.get_height()//5))
                    back_button.set_dimensions((6 * window.get_width()//16, window.get_height()//5))
                    window_resize_button.set_dimensions((6 * window.get_width()//16, window.get_height()//5))
                    music_option_button.set_position((window.get_width()//16, 3*window.get_height()//5))
                    sound_effects_option_button.set_position((9 * window.get_width()//16, window.get_height()//5))
                    back_button.set_position((9 * window.get_width()//16, 3*window.get_height()//5))
                    window_resize_button.set_position((window.get_width()//16, window.get_height()//5))
                    music_option_button.ui_container.set_dimensions((window.get_width(), window.get_height()))
                    sound_effects_option_button.ui_container.set_dimensions((window.get_width(), window.get_height()))
                    back_button.ui_container.set_dimensions((window.get_width(), window.get_height()))
                    window_resize_button.ui_container.set_dimensions((window.get_width(), window.get_height()))
                    textRect.center = (window.get_width()//2, window.get_height()//12)
                json.dump(options_dict, json_file)
                json_file.truncate()
            manager.process_events(event)

        window.fill((211, 235, 217))
        window.blit(option_txt, textRect)
        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()


def gameMenuScreen(window):
    """draws game menu on the given window

    Args:
        window (pygame.display): window to draw on
    """
    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))

    button_sound_effect = pygame.mixer.Sound('buttonsfx.wav')
    json_file = open("env.json", "r+")
    options_dict = json.load(json_file)
    if options_dict["sound_effects"] == "Off":
        button_sound_effect.set_volume(0)


    level_select_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//2 - window.get_width()//6, window.get_height()//4), (window.get_width()//3, window.get_height()//8)),
                                            text='Level Select',
                                            manager=manager)

    help_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//2 - window.get_width()//6, 2*window.get_height()//4), (window.get_width()//3, window.get_height()//8)),
                                            text='How To Play',
                                            manager=manager)

    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//2 - window.get_width()//6, 3*window.get_height()//4), (window.get_width()//3, window.get_height()//8)),
                                            text='Back',
                                            manager=manager)

    button_to_status = {
        level_select_button : level_select_menu, #THE VALUE LINKED TO THE KEY SHOULD BE A FUNCTION THAT MODIFIES PROPERTIES OF GAME
        help_button : help_menu, #THE VALUE LINKED TO THE KEY SHOULD BE A FUNCTION THAT MODIFIES PROPERTIES OF GAME
        back_button : "back"
    }

    clock = pygame.time.Clock()

    while True: #THE LOOP THAT DOES THE CONSTANT USER INPUT CHECKS AND DRAWS
        pygame.time.delay(10) #This is the function that creates a time delay of x milliseconds
        time_delta = clock.tick(60)/1000.0
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"


            #CHECKS BUTTON INPUT
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    button_sound_effect.play()
                    if event.ui_element == back_button:
                        return "back"
                    else:
                        current_status = button_to_status[event.ui_element](window)
                        if current_status != "back":
                            return current_status
            manager.process_events(event)

        window.fill((211, 235, 217))
        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()


def help_menu(window):
    """draws help page on the given window

    Args:
        window (pygame.display): window to draw on
    """
    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))
    button_sound_effect = pygame.mixer.Sound('buttonsfx.wav')
    json_file = open("env.json", "r+")
    options_dict = json.load(json_file)
    if options_dict["sound_effects"] == "Off":
        button_sound_effect.set_volume(0)

    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((12* window.get_width()//16, 9*window.get_height()//10), (3*window.get_width()//16, window.get_height()//16)),
                                            text='Back',
                                            manager=manager)

    clock = pygame.time.Clock()

    while True: #THE LOOP THAT DOES THE CONSTANT USER INPUT CHECKS AND DRAWS
        pygame.time.delay(10) #This is the function that creates a time delay of x milliseconds
        time_delta = clock.tick(60)/1000.0

        window.fill((211, 235, 217))
        how_to_play_box(window)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"


            #CHECKS BUTTON INPUT
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    button_sound_effect.play()
                    return "back"
            manager.process_events(event)



        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()

def how_to_play_box(window):
    """This function has everything for the how to play section of the option

    Args:
        window (pygame.Surface): a place where we draw the game on
    """
    starting_location = (window.get_width()//12, window.get_height()//15)

    Header_font = pygame.font.Font('freesansbold.ttf', 32)  
    font = pygame.font.SysFont('freesansbold.ttf', 25)

    sokoban_txt = Header_font.render("Control For Sokoban", True, (100, 100, 0))
    explain_1 = font.render("- Arrow keys for player movement", 1, (0,0,0))
    explain_2 = font.render("- U for restart level", 1, (0,0,0))
    explain_3 = font.render("- N for next level", 1, (0,0,0))
    explain_4 = font.render("- Q for quit to main menu", 1, (0,0,0))

    textRect = sokoban_txt.get_rect()
    textRect.center = (window.get_width()//2, window.get_height()//12)

   
    window.blit(sokoban_txt, textRect)
    window.blit(explain_1, (starting_location[0] * 4, starting_location[1] * 3))
    window.blit(explain_2, (starting_location[0] * 4, starting_location[1] * 4))
    window.blit(explain_3, (starting_location[0] * 4, starting_location[1] * 5))
    window.blit(explain_4, (starting_location[0] * 4, starting_location[1] * 6))


