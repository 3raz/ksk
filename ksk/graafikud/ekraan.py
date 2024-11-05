import pygame, sys
from objektid.šabloonid.objekt import Objekt
from utils.kaunistused import Singleton
import time

@Singleton.singleton
class Ekraan(object):

    def __init__(self, suurus_x, suurus_y):
        self.suurus_x = suurus_x
        self.suurus_y = suurus_y
        self.ekraan = pygame.display.set_mode((self.suurus_x, self.suurus_y))
    
    @property
    def ekraani_võtja(self):
        return self.ekraan




pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Hello World")

o = Objekt(100,45,screen,50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((255, 255, 255))
    
    o.protsess()
    print(o.objekti_andmed_võtja)
    time.sleep(0.1)

    # Flip the display
    pygame.display.flip()

    