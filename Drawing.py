import pygame

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
blue = (0,100,255)
green = (0,255,0)

gameDisplay = pygame.display.set_mode((800,600))

gameDisplay.fill(blue)

Pix = pygame.PixelArray(gameDisplay)

#Pix[200][300] = red

pygame.draw.line(gameDisplay, red, (200,300), (500,500), 5)

pygame.draw.circle(gameDisplay, red, (200,200), 100)

pygame.draw.rect(gameDisplay, black, (150,150,200,100))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()        
