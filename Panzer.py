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

def button(text, x, y, width, height,inactive_color, active_color, action = None):
    cur = pygame.mouse.get_pos()

    click = pygame.mouse.get_pressed()
    #print(click)
    
    if x + width > cur[0] > x and y + height > cur[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,width,height))
        if click[0] == 1:
            print("Button Clicked")
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
                        paused = False
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        quit()

        

        clock.tick(5)


def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
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
        
        button("Play", 150,500,100,50, red, light_red)
        button("Controls", 350,500,100,50,yellow, light_green )
        button("Quit", 550,500,100,50, blue, light_blue)


        pygame.display.update()

        clock.tick(15)

game_intro()

def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15
    
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
                    pass
                    
                elif event.key == pygame.K_RIGHT:
                    pass
                    
                elif event.key == pygame.K_UP:
                    pass
                    
                    
                elif event.key == pygame.K_DOWN:
                    pass

                elif event.key == pygame.K_p:
                    pause()

                    

        gameDisplay.fill(white)
        
        pygame.display.update()
        
        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()
