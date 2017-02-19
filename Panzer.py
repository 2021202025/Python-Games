import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))


pygame.display.set_caption('Tanks')

#icon = pygame.image.load("apple.png")       
#pygame.display.set_icon(icon)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (34,177,76)
yellow = (255,242,0)
blue = (0,0,255)
light_blue = (0,100,255)
light_red = (255,66,0)
light_green = (230
               ,255,0)

clock = pygame.time.Clock()

tankWidth = 50
tankHeight = 20

turretWidth = 6
wheelWidth = 5

ground_height = 35


smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

#img = pygame.image.load('snakehead.png')
#appleimg = pygame.image.load('apple.png')

def score(score):

    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text, [0,0])
    

def text_objects(text, color,size = "small"):

    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = ((buttonx+(buttonwidth/2)), buttony+(buttonheight/2))
    gameDisplay.blit(textSurf, textRect)
   
def message_to_screen(msg,color, y_displace = 0, size = "small"):
    textSurf, textRect = text_objects(msg,color,size)
    textRect.center = (int(display_width / 2), int(display_height / 2)+y_displace)
    gameDisplay.blit(textSurf, textRect)

def tank(x,y,turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x-27, y-2),
                       (x-26, y-5),
                       (x-25, y-8),
                       (x-23, y-12),
                       (x-20, y-14),
                       (x-18, y-15),
                       (x-15, y-17),
                       (x-13, y-19),
                       (x-11, y-21)
                       ]


    
    pygame.draw.circle(gameDisplay, black, ((x),(y)),int(tankHeight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankHeight, y, tankWidth, tankHeight))
    
    pygame.draw.line(gameDisplay, black, (x,y), possibleTurrets[turPos], turretWidth)


    startX = 15
    
    for z in range(9):
        pygame.draw.circle(gameDisplay, black, (x-startX, y+20), wheelWidth)
        startX -= 5

    return possibleTurrets[turPos]



def enemy_tank(x,y,turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x+27, y-2),
                       (x+26, y-5),
                       (x+25, y-8),
                       (x+23, y-12),
                       (x+20, y-14),
                       (x+18, y-15),
                       (x+15, y-17),
                       (x+13, y-19),
                       (x+11, y-21)
                       ]


    
    pygame.draw.circle(gameDisplay, black, ((x),(y)),int(tankHeight/2))
    pygame.draw.rect(gameDisplay, black, (x-tankHeight, y, tankWidth, tankHeight))
    
    pygame.draw.line(gameDisplay, black, (x,y), possibleTurrets[turPos], turretWidth)


    startX = 15
    
    for z in range(9):
        pygame.draw.circle(gameDisplay, black, (x-startX, y+20), wheelWidth)
        startX -= 5

    return possibleTurrets[turPos]


def game_controls():
    
     gcont = True

     while gcont:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        gameDisplay.fill(white)
        message_to_screen("Controls!",green,-100,size="large")
        message_to_screen("Fire: Spacebar",black,-30)
        message_to_screen("Move Turret: Up and Down Arrows",black,10)
        message_to_screen("Move Tank: Left and right Arrows",black,50)
        message_to_screen("Pause: P",black,90)

        button("Play", 150,500,100,50, red, light_red, action="play")
        #button("Main", 350,500,100,50,yellow, light_green, action="main")
        button("Quit", 550,500,100,50, blue, light_blue, action="quit")

        

        pygame.display.update()

        clock.tick(15)


def button(text, x, y, width, height,inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()
    #print(click)
    
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()

            if action == "controls":
                game_controls()

            if action == "play":
                gameLoop()

            
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,width,height))

    text_to_button(text,black,x,y,width,height)

        

def pause():

    paused = True
    message_to_screen("Paused",black,-100,size="large")
    message_to_screen("Press C to continue playing or Q to quit",black,25)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        pau
                        sed = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

        

        clock.tick(5)



def barrier(xlocation,randomHeight,barrier_width):

    pygame.draw.rect(gameDisplay, black, [xlocation, display_height-randomHeight, barrier_width, randomHeight])
    
    
##def fireShell(xy,tankx,tanky,turPos,gun_power):
##    fire = True
##
##    startingShell = list(xy)
##
##    
##    print("FIRE",xy)
##
##    while fire:
##        for event in pygame.event.get():
##            if event.type == pygame.QUIT:
##                pygame.quit()
##                quit()
##
##        print(startingShell[0],startingShell[1])
##        pygame.draw.circle(gameDisplay, red, (startingShell[0],startingShell[1]),5)
##
##        startingShell[0] -= (12 - turPos)*2
##    # y = x**2
##        startingShell[1] += int((((startingShell[0] - xy[0]) *0.01)**2) - (turPos+turPos/(12-turPos)))
##
##        if startingShell[1] > display_height:
##            fire = False
##
##        pygame.display.update()
##        clock.tick(30)


def explosion(x,y, size=50):

    explode = True

    while explode:
         for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

         startPoint = x,y

         colorChoices = [red, light_red, yellow]

         magnitude = 1

         while magnitude < size:

             exploding_bit_x = x + random.randrange(-1*magnitude, magnitude)
             exploding_bit_y = y + random.randrange(-1*magnitude, magnitude)
        
             pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0,3)], (exploding_bit_x,exploding_bit_y), random.randrange(1,4))
             magnitude += 1

             pygame.display.update()
             clock.tick(60)

         explode = False


def fireShell2(xy,tankx,tanky,turPos,gun_power,xlocation,barrier_width,randomHeight,tank="enemy"):
    fire = True

    startingShell = list(xy)

    
    print("FIRE",xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print(startingShell[0],startingShell[1])
        pygame.draw.circle(gameDisplay, green, (startingShell[0],startingShell[1]),5)

        if tank == "enemy":
            startingShell[0] += (12 - turPos)
        else:
            startingShell[0] -= (12 - turPos)*2
            
    # y = x**2
        startingShell[1] += int((((startingShell[0] - xy[0]) *0.015/(gun_power/50))**2) - (turPos+turPos/(12-turPos)))

        if startingShell[1] > display_height-ground_height:
            
            print("Last Shell: ",startingShell[0],startingShell[1])
            hit_x = int((startingShell[0]*display_height-ground_height)/startingShell[1])
            hit_y = int(display_height-ground_height)
            print("Impact: ",hit_x,hit_y)
            explosion(hit_x,hit_y)
            
            fire = False

        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            
              print("Last Shell: ",startingShell[0],startingShell[1])
              hit_x = int(startingShell[0])
              hit_y = int(startingShell[1])
              print("Impact: ",hit_x,hit_y)
              explosion(hit_x,hit_y)
            
              fire = False
            

        pygame.display.update()
        clock.tick(60)
    
def power(level):
    text = smallfont.render("Power: "+str(level)+"%", True,black)
    gameDisplay.blit(text, [display_width/2-40,0])



def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pydgame.K_c:
                        intro = False
                    elif event.key == pygame.K_q:
                        
                        pygame.quit()
                        quit()

        gameDisplay.fill(white)
        message_to_screen("Welcome to Tanks!",green,-100,size="large")
        message_to_screen("The objective is to shoot and destroy",black,-30)
        message_to_screen("the enemy tank before they destroy you.",black,10)
        message_to_screen("The more enemies you destroy, the harder they get.",black,50)
        #message_to_screen("Press C to play, P to pause or Q to quit",black,180)

##        cur = pygame.mouse.get_pos()
##
##        if 150+100 > cur[0] > 150 and 500+50 > cur[1] > 500:
##            pygame.draw.rect(gameDisplay, light_red, (150,500,100,50))
##        else:
##            pygame.draw.rect(gameDisplay, red, (150,500,100,50))
##
##        if 350+100 > cur[0] > 350 and 500+50 > cur[1] > 500:
##            pygame.draw.rect(gameDisplay, light_green, (350,500,100,50))
##        else:
##            pygame.draw.rect(gameDisplay, yellow, (350,500,100,50))
##        
##        if 550+100 > cur[0] > 550 and 500+50 > cur[1] >500:
##            pygame.draw.rect(gameDisplay, light_blue, (550,500,100,50))
##        else:
##            pygame.draw.rect(gameDisplay, blue, (550,500,100,50))
        
        button("Play", 150,500,100,50, red, light_red, action="play")
        button("Controls", 350,500,100,50,yellow, light_green, action="controls" )
        button("Quit", 550,500,100,50, blue, light_blue, action="quit")


        pygame.display.update()

        clock.tick(15)


def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15

    barrier_width=40
    
    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0

    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9
    
    fire_power = 50
    power_change = 0

    xlocation = (display_width/2) + random.randint(-0.2*display_width, 0.2*display_width)
   
    randomHeight = random.randrange(display_height*0.1, display_height*0.5)
    


    while not gameExit:
        
        
        if gameOver == True:
            #gameDisplay.fill(white)
            message_to_screen("Game Over",red,-50,size="large")
            message_to_screen("Press C to play again or Q to exit",black,50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:
                            
                            gameExit = True
                            gameOver = False
         


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5
                    
                elif event.key == pygame.K_RIGHT:
                    tankMove = 5
                    
                elif event.key == pygame.K_UP:
                    changeTur = 1
                    
                    
                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_p:
                    pause()

                elif event.key == pygame.K_SPACE:
                    #fireShell(gun,mainTankX,mainTankY,currentTurPos,fire_power)
                    fireShell2(gun,mainTankX,mainTankY,currentTurPos,fire_power,xlocation,barrier_width,randomHeight)
                    
                elif event.key == pygame.K_a:
                    power_change = -1

                elif event.key == pygame.K_d:
                    power_change = 1

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a:
                    power_change = 0

                if event.key == pygame.K_d:
                    power_change = 0

                    

        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0

        if mainTankX - (tankWidth/2) < xlocation + barrier_width:
            mainTankX += 5 

        gameDisplay.fill(white)
        gun = tank(mainTankX,mainTankY,currentTurPos)
        enemy_gun = enemy_tank(enemyTankX,enemyTankY,7)

        fire_power += power_change

        power(fire_power)


##        if mainTankX-int(tankWidth/2.0) < xlocation+barrier_width:
##            mainTankX = xlocation+int(tankWidth/2.0)+barrier_width
##        elif mainTankX+int(tankWidth/2.0) > display_width:
##            mainTankX = display_width-int(tankWidth/2.0)﻿
        


        barrier(xlocation,randomHeight,barrier_width)
        gameDisplay.fill(green, rect=[0, display_height-ground_height, display_width, ground_height])
        
        pygame.display.update()
        
        clock.tick(FPS)

    pygame.quit()
    quit()

game_intro()
gameLoop()
