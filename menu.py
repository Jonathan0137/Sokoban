"""THIS IS THE FUNCTION FOR THE MAIN MENU SCREEN"""
import pygame

def mainMenu(display):
    mainMenuOn = True #CHECKS THAT THE MENU SHOULD BE DISPLAYED
    background_image = pygame.image.load("Legend.jpg") #LOADS BACKGROUND IMAGE
    pygame.mixer.music.load('Journey.mp3') #LOADS MUSIC
    pygame.mixer.music.play(-1) #PLAYS MUSIC -1 MEANS IN LOOP
    while mainMenuOn: #THE LOOP THAT DOES THE CONSTANT USER INPUT CHECKS AND DRAWS
        pygame.time.delay(10) #This is the function that creates a time delay of x milliseconds
        display.blit(background_image, (0,0)) #DRAWS THE BACKGROUND IMAGE
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            mainMenuOn = False

    return False




