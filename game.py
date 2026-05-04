import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Catch the Colors")

print("Pygame is running!")

running = True
while running:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running= False

    screen.fill((0,0,0))
    pygame.display.flip()        
pygame.quit()