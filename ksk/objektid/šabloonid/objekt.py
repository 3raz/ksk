from mudlid.KinemaatikaMudel import KinemaatikaMudel

import pygame
import time

class Objekt(KinemaatikaMudel):
    def __init__(self, esialgne_kiirus, nurk, screen, suurus=1, color=(255,0,0), gravitatsioon=9.8, dt=0.1):
        super().__init__(esialgne_kiirus, nurk, gravitatsioon, dt)
        self.suurus = suurus
        self.screen = screen
        self.color = color
        
    def __joonista__(self):
        """
        Joonistab objekti ekraanile.
        """
        pygame.draw.circle(self.screen, self.color, (self.positsioon_x, self.positsioon_y), self.suurus)
    
    def __uuenda__(self):
        super().uuenda()
        
    def protsess(self):
        self.__joonista__()
        self.__uuenda__()