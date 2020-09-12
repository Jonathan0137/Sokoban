"""THIS IS THE FUNCTION FOR THE MAIN MENU SCREEN"""
import pygame
import pygame_gui

pygame.init()

def mainMenu(window):

    manager = pygame_gui.UIManager((window.get_width(), window.get_height())) 

    mainMenuOn = True #CHECKS THAT THE MENU SHOULD BE DISPLAYED   <---- PROBABLY WILL DELETE

    background_image = pygame.image.load("Legend.jpg") #LOADS BACKGROUND IMAGE

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


    clock = pygame.time.Clock()


    while mainMenuOn: #THE LOOP THAT DOES THE CONSTANT USER INPUT CHECKS AND DRAWS
        pygame.time.delay(10) #This is the function that creates a time delay of x milliseconds
        window.blit(background_image, (0,0)) #DRAWS THE BACKGROUND IMAGE

        time_delta = clock.tick(60)/1000.0
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            manager.process_events(event)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            mainMenuOn = False

        manager.update(time_delta)
        manager.draw_ui(window)
        pygame.display.update()

    return False




