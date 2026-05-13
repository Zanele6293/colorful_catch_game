import pygame

pygame.init()

BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (128,0,128)
WHITE = (255,255,255)

# We need to have a function  !!
WIDTH =800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Let's catch the Colors")

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running= False

    screen.fill(BLACK) #
    
    pygame.draw.rect(screen,PURPLE,(50,50,100,100))
    pygame.draw.circle(screen,BLUE,(400,300),50)

    pygame.display.flip()   # This updates the color show at the top     
pygame.quit()