import pygame, sys
from objektid.šabloonid.objekt import Objekt


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")

o = Objekt(10,45,screen,2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    o.protsess()