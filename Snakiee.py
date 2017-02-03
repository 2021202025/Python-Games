import pygame
import time
import random

pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)
yellow = (255,242,0)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snakie')

img = pygame.image.load('Snakiee2.png')

#pygame.display.flip()

clock = pygame.time.Clock()

block_size = 15

FPS = 10

direction = "right"

smallfont = pygame.font.SysFont("comicsansms", 28)
medfont = pygame.font.SysFont("comicsansms", 40)
largefont = pygame.font.SysFont("comicsansms", 80)

def game_intro():

    intro = True

    while intro:
        gameDisplay.fill(black)
        message_to_screen("Snakie", red, -100, "large")
        message_to_screen("Use Arrow Keys to Move the Snake", yellow, -25, "medium")
        message_to_screen("Eat Apples to increase Score", yellow, 20, "medium")

        pygame.display.update()

def snake(block_size, snakelist):

    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)

    if direction == "up":
        head = pygame.transform.rotate(img, 0)

    if direction == "down":
        head = pygame.transform.rotate(img, 180)    
    
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, red, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
        
    return textSurface, textSurface.get_rect()
    
def message_to_screen(msg,color, y_displace=0, size = "small"):
    textSurf, textRect = text_objects(msg, color, size)
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [display_width/2-250, display_height/2-100])
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direction
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0
    
    snakelist = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen("Game Over",
                              yellow,
                              -50,
                              size = "large")
            message_to_screen("Press C to play again and Q to Quit",
                              yellow,
                              0,
                              size = "small")
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

                    if event.key == pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    direction = 'up'
                    lead_y_change = -block_size
                    lead_x_change = 0    
                elif event.key == pygame.K_DOWN:
                    direction = 'down'
                    lead_y_change = block_size
                    lead_x_change = 0
                
                    
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver=True
                    
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(black)

        AppleThickness = 16
        pygame.draw.rect(gameDisplay, blue, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        #gameDisplay.fill(red, rect=[200,200,50,10])

        
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakelist.append(snakeHead)

        if len(snakelist) > snakeLength:
            del snakelist[0]
            
        for eachSegment in snakelist[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
            
        snake(block_size, snakelist)
        
        pygame.display.update()

##        if lead_x == randAppleX and lead_y == randAppleY:
##             randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
##             randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
##             snakeLength +=1

##        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness:
##            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness:
##                 randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
##                 randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
##                 snakeLength +=1

        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:
            #print("X crossover")
            if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
                print("X and Y crossover")
                randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
                randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
                snakeLength +=1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                print("X and Y crossover")
                randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
                randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
                snakeLength +=1
        
        clock.tick(FPS)

    pygame.quit()
    quit()
    
game_intro()

gameLoop()
