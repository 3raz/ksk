from mudlid.KinemaatikaMudel import KinemaatikaMudel

from abc import ABC, abstractmethod
import pygame
import time

class Objekt(KinemaatikaMudel):
    def __init__(self, esialgne_kiirus, nurk, ekraan, suurus=1, color=(255,0,0), gravitatsioon=9.8, dt=0.1) -> None:
        super().__init__(esialgne_kiirus, nurk, gravitatsioon, dt)
        self.suurus = suurus
        self.ekraan = ekraan
        self.color = color
        self.algus_x = 0
        self.algus_y = 0
    
    @abstractmethod
    def __joonista__(self) -> None:
        """
        Privaatfunktsioon joonistab objekti ekraanile.
        """
        pygame.draw.circle(self.ekraan, self.color, (self.positsioon_x, self.algus_y-self.positsioon_y), self.suurus)
    
    def __uuenda__(self) -> None:
        """
        Privaatfunktsioon uuenda objektiandmeid lapsevanema klassi kaudu.
        """
        super().uuenda()
    
    def alguspunkti_seadja(self, punkt: tuple) -> None:
        self.algus_x = punkt[0]
        self.algus_y = punkt[1]
    
    def protsess(self) -> None:
        self.__joonista__()
        self.__uuenda__()