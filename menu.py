"""THIS IS THE FUNCTION FOR THE MAIN MENU SCREEN"""
import pygame
import pygame_gui

pygame.init()

"""Function draws the main menu screen"""
def mainMenuScreen(window):

    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))

    background_image_file = open("Legend.jpg")
    background_image = pygame.image.load(background_image_file) #LOADS BACKGROUND IMAGE

    pygame.mixer.music.load('Journey.mp3') #LOADS MUSIC
    pygame.mixer.music.play(-1) #PLAYS MUSIC -1 MEANS IN LOOP


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
        start_button : "GameMenu",
        option_button : "Options",
        quit_button : "exit"
    }


    clock = pygame.time.Clock()


    while True: #THE LOOP THAT DOES THE CONSTANT USER INPUT CHECKS AND DRAWS
        pygame.time.delay(10) #This is the function that creates a time delay of x milliseconds
        window.fill((0,0,0))
        window.blit(background_image, (0,0)) #DRAWS THE BACKGROUND IMAGE

        time_delta = clock.tick(60)/1000.0
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"


            #CHECKS QUIT BUTTON
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == option_button:
                        optionsScreen(window)
                    else:
                        background_image_file.close()
                        return button_to_status[event.ui_element]
            manager.process_events(event)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            return "exit"

        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()

    return "exit"


"""Options screen"""
def optionsScreen(window):
    manager = pygame_gui.UIManager((window.get_width(), window.get_height()))

    background_image = pygame.image.load("Legend.jpg") #LOADS BACKGROUND IMAGE

    #pygame.mixer.music.load('mainmenusong.wav') #LOADS MUSIC
    #pygame.mixer.music.play(-1) #PLAYS MUSIC -1 MEANS IN LOOP

    window_size_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//16, window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                             text='Window Size',
                                             manager=manager)

    music_option_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((window.get_width()//16, 3*window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                             text='Music (on/off)',
                                             manager=manager)

    sound_effects_option_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((9 * window.get_width()//16, window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                             text='Sound Effects (on/off)',
                                             manager=manager)

    quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((9 * window.get_width()//16, 3*window.get_height()//5), (6 * window.get_width()//16, window.get_height()//5)),
                                             text='Back',
                                             manager=manager)

    button_to_status = {
        window_size_button : "GameMenu",
        music_option_button : "Options",
        sound_effects_option_button : "Options",
        quit_button : "exit"
    }

    clock = pygame.time.Clock()

    while True: #THE LOOP THAT DOES THE CONSTANT USER INPUT CHECKS AND DRAWS
        pygame.time.delay(10) #This is the function that creates a time delay of x milliseconds
        window.blit(background_image, (0,0)) #DRAWS THE BACKGROUND IMAGE

        time_delta = clock.tick(60)/1000.0
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"


            #CHECKS QUIT BUTTON
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    return button_to_status[event.ui_element]
            manager.process_events(event)

        window.fill((255,255,255))
        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()