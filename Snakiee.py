import pygame

pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Snakie')

#pygame.display.flip()


gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        print(event)
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [400,300,10,50])
    pygame.draw.rect(gameDisplay, red, [400,300,10,10])
    pygame.draw.rect(gameDisplay, blue, [400,300,10,4])

    gameDisplay.fill(red, rect=[200,200,50,10])

    
    pygame.display.update()



pygame.quit()
quit()
