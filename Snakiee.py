import pygame
import time
import random

pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snakie')

#pygame.display.flip()

clock = pygame.time.Clock()

block_size = 20

FPS = 15

font = pygame.font.SysFont(None, 32)

def snake(block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, red, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text,color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()
    
def message_to_screen(msg,color):
    textSurf, textRect = text_objects(msg,color)
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [display_width/2-250, display_height/2-100])
    textRect.center = (display_width/2), (display_height/2)
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 0
    lead_y_change = 0
    
    snakelist = []
    snakeLength = 1

    randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(black)
            message_to_screen("You Lost, Press C to play again or Q to quit", white)
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
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0    
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                
                    
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver=True
                    
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(black)

        AppleThickness = 30
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

gameLoop()
