import pygame, sys
from objektid.šabloonid.objekt import Objekt
import time


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")

o = Objekt(100,45,screen,50,dt=0.001)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((255, 255, 255))
    
    o.protsess()
    print(o.objekti_andmed_võtja)

    # Flip the display
    pygame.display.flip()

    