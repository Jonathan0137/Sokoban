import pygame
from worker import worker
from Level import Level


def inGameScreen(arg):

    window = arg[0]
    level_num = arg[1]

    pygame.init()

    pygame.display.set_caption("Sokoban")

    number_of_moves = 0
    currentLevel = int(level_num)
    myLevel = Level(currentLevel)

    font = pygame.font.SysFont('arial', 20, True)
    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(27) #refresh rate

        
        for event in pygame.event.get(): # exit button works
            if event.type == pygame.QUIT:
                run = False
                return "exit"
            window.fill((117, 81, 17))

            level_text = font.render("Level : " + str(currentLevel), 1, (0,0,0))
            Moves_text = font.render("Moves : " + str(number_of_moves), 1, (0,0,0))
            
            window.blit(level_text, (10, 10))
            window.blit(Moves_text, (10, 35))


            myLevel.draw_level(window) #level class
            myWorker = worker(myLevel)  #worker class

            keys = pygame.key.get_pressed()#get key presses

            if keys[pygame.K_UP]:
                myWorker.movePlayer("up", myLevel)
                number_of_moves += 1
            elif keys[pygame.K_DOWN]:
                myWorker.movePlayer("down", myLevel)
                number_of_moves += 1
            elif keys[pygame.K_LEFT]: 
                myWorker.movePlayer("left", myLevel)
                number_of_moves += 1
            elif keys[pygame.K_RIGHT]:
                myWorker.movePlayer("right", myLevel)
                number_of_moves += 1
            elif keys[pygame.K_1]: # restart button pressed
                myLevel = Level(currentLevel)
                number_of_moves = 0
            elif keys[pygame.K_2]: # skip this level
                currentLevel = myLevel.getCurrentLevel() + 1
                if(currentLevel == 30):
                    print("GameOver")
                    run = False
                    return "MainMenu"
                print("Current Level = " + str(currentLevel))
                window = arg[0]
                myLevel = Level(currentLevel)
                number_of_moves = 0
            elif keys[pygame.K_DELETE]: # back to main menu
                print("Back")
                run = False
                return "MainMenu"

            if(myLevel.LevelComplete() == True):
                print("LEVEL " + str(currentLevel) + " COMPLETE")
                currentLevel = myLevel.getCurrentLevel() + 1
                window = arg[0]
                myLevel = Level(currentLevel)
                number_of_moves = 0
            if(currentLevel == 30):
                print("GameOver")
                run = False
                return "MainMenu"



