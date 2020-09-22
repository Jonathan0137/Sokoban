"""THIS IS THE FUNCTION FOR THE MAIN MENU SCREEN"""
import pygame
import pygame_gui
import os
from Level import *


pygame.init()

"""Exit game"""
def exitGame(window):
    return "exit"

def level_select_menu(window):
    index = 0
    entries = os.listdir('level/')
    number_of_levels = len(entries) - 1
    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))

    background_image_file = open("menubackground.png")
    background_image = pygame.image.load(background_image_file) #LOADS BACKGROUND IMAGE

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
    #placeholderting = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//4 - 3*window.get_width()//32, window.get_height()//6), (22*window.get_width()//32, 5*window.get_height()//8)),
     #                                       text='PLACEHOLDER FOR MINI SCREEN SIZE AND X/Y COORDINATES',
      #                                      manager=manager)


    clock = pygame.time.Clock()
    window.blit(background_image, (0,0))
    while True: #THE LOOP THAT DOES THE CONSTANT USER INPUT CHECKS AND DRAWS
        pygame.time.delay(10) #This is the function that creates a time delay of x milliseconds
        time_delta = clock.tick(60)/1000.0

        myLevel = Level(index)
        myLevel.draw_level(window) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            #CHECKS BUTTON INPUT
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == left_button:
                        window.blit(background_image, (0,0))
                        index = index - 1
                        if index < 0:
                            index = number_of_levels
                    elif event.ui_element == right_button:
                        window.blit(background_image, (0,0))
                        index = index + 1
                        if index >= number_of_levels:
                            index = 0
                    elif event.ui_element == back_button:
                        return "back"
            manager.process_events(event)

        
        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()

"""Function draws the main menu screen"""
def mainMenuScreen(window):

    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))

    background_image_file = open("menubackground.png")
    background_image = pygame.image.load(background_image_file) #LOADS BACKGROUND IMAGE

    #pygame.mixer.music.load('Journey.mp3') #LOADS MUSIC
    #pygame.mixer.music.play(-1) #PLAYS MUSIC -1 MEANS IN LOOP


    start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//2 - window.get_width()//6, window.get_height()//4), (window.get_width()//3, window.get_height()//8)),
                                             text='Start Game',
                                             manager=manager)

    option_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//2 - window.get_width()//6, 2*window.get_height()//4), (window.get_width()//3, window.get_height()//8)),
                                             text='Game Options',
                                             manager=manager)

    quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//2 - window.get_width()//6, 3*window.get_height()//4), (window.get_width()//3, window.get_height()//8)),
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
                    status_check = button_to_status[event.ui_element](window)
                    if status_check != "back":
                        return status_check
            manager.process_events(event)

        
        window.fill((0,0,0))
        window.blit(background_image, (0,0)) #DRAWS THE BACKGROUND IMAGE
        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()

    return "exit"


"""Options screen"""
def optionsScreen(window):
    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))

    #pygame.mixer.music.load('mainmenusong.wav') #LOADS MUSIC
    #pygame.mixer.music.play(-1) #PLAYS MUSIC -1 MEANS IN LOOP

    background_image_file = open("menubackground.png")
    background_image = pygame.image.load(background_image_file)

    temp_list_screen_size = ["640x480", "800x600", "1024x768"]

    

    music_option_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//16, 3*window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                             text='Music (on/off)',
                                             manager=manager)

    sound_effects_option_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((9 * window.get_width()//16, window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                             text='Sound Effects (on/off)',
                                             manager=manager)

    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((9 * window.get_width()//16, 3*window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                             text='Back',
                                             manager=manager)
                                             
    window_resize_button = pygame_gui.elements.UIDropDownMenu(temp_list_screen_size, temp_list_screen_size[0], relative_rect=pygame.Rect((window.get_width()//16, window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                             manager=manager)

    button_to_status = {
        music_option_button : "Options", #THE VALUE LINKED TO THE KEY SHOULD BE A FUNCTION THAT MODIFIES PROPERTIES OF GAME
        sound_effects_option_button : "Options", #THE VALUE LINKED TO THE KEY SHOULD BE A FUNCTION THAT MODIFIES PROPERTIES OF GAME
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
                    try:
                        current_status = button_to_status[event.ui_element]
                        if current_status == "back":
                            return current_status
                    except:
                        print("TO DO: ADD LOGIC FOR DROP DOWN MENU")
            manager.process_events(event)

        window.fill((255,255,255))
        window.blit(background_image, (0,0))
        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()

"""Game menu selection"""
def gameMenuScreen(window):
    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))

    background_image_file = open("menubackground.png")
    background_image = pygame.image.load(background_image_file) #LOADS BACKGROUND IMAGE

    #pygame.mixer.music.load('Journey.mp3') #LOADS MUSIC
    #pygame.mixer.music.play(-1) #PLAYS MUSIC -1 MEANS IN LOOP


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
                    if event.ui_element == back_button:
                        return "back"
                    else:
                        current_status = button_to_status[event.ui_element](window)
                        if current_status != "back":
                            return current_status
            manager.process_events(event)

        window.fill((255,196,0))
        window.blit(background_image, (0,0))
        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()


def help_menu(window):
    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))

    background_image_file = open("menubackground.png")
    background_image = pygame.image.load(background_image_file) #LOADS BACKGROUND IMAGE

    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((12* window.get_width()//16, 9*window.get_height()//10), (3*window.get_width()//16, window.get_height()//16)),
                                            text='Back',
                                            manager=manager)

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
                    #current_status = button_to_status[event.ui_element]
                    return "back"
            manager.process_events(event)

        window.fill((255,196,0))
        window.blit(background_image, (0,0))
        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()