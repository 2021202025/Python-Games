import pygame

pygame.init()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

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
    pygame.display.update()



pygame.quit()
quit()
