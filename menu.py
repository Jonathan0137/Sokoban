"""THIS IS THE FUNCTION FOR THE MAIN MENU SCREEN"""
import pygame
import pygame_gui

pygame.init()

"""Exit game"""
def exitGame(window):
    return "exit"

"""Function draws the main menu screen"""
def mainMenuScreen(window):

    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))

    background_image_file = open("Legend.jpg")
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
        window.fill((0,0,0))
        window.blit(background_image, (0,0)) #DRAWS THE BACKGROUND IMAGE

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


        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()

    return "exit"


"""Options screen"""
def optionsScreen(window):
    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))

    #pygame.mixer.music.load('mainmenusong.wav') #LOADS MUSIC
    #pygame.mixer.music.play(-1) #PLAYS MUSIC -1 MEANS IN LOOP

    temp_list_screen_size = ["640x480", "800x600", "1024x768"]

    window_size_button = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(temp_list_screen_size, temp_list_screen_size[0], relative_rect=pygame.Rect((window.get_width()//16, window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                             manager=manager)

    music_option_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//16, 3*window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                             text='Music (on/off)',
                                             manager=manager)

    sound_effects_option_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((9 * window.get_width()//16, window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                             text='Sound Effects (on/off)',
                                             manager=manager)

    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((9 * window.get_width()//16, 3*window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                             text='Back',
                                             manager=manager)

    button_to_status = {
        #window_size_button : "Options", #THE VALUE LINKED TO THE KEY SHOULD BE A FUNCTION THAT MODIFIES PROPERTIES OF GAME
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
                    current_status = button_to_status[event.ui_element]
                    return current_status
            manager.process_events(event)

        window.fill((255,255,255))
        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()

"""Game menu selection"""
def gameMenuScreen(window):
    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))

    background_image_file = open("Legend.jpg")
    background_image = pygame.image.load(background_image_file) #LOADS BACKGROUND IMAGE

    #pygame.mixer.music.load('Journey.mp3') #LOADS MUSIC
    #pygame.mixer.music.play(-1) #PLAYS MUSIC -1 MEANS IN LOOP


    continue_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//2 - window.get_width()//6, window.get_height()//4), (window.get_width()//3, window.get_height()//8)),
                                            text='Continue',
                                            manager=manager)

    level_select_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//2 - window.get_width()//6, 2*window.get_height()//4), (window.get_width()//3, window.get_height()//8)),
                                            text='Level Select',
                                            manager=manager)

    back_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//2 - window.get_width()//6, 3*window.get_height()//4), (window.get_width()//3, window.get_height()//8)),
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
                    current_status = "back"
                    return current_status
            manager.process_events(event)

        window.fill((255,196,0))
        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()
