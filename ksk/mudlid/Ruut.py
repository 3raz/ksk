from mudlid.Objekt import Objekt
import pygame
from andmed.Andmed import Andmed

andmed = Andmed().andmed

class Ruut(Objekt):
    def __init__(self, ekraan, esialgne_kiirus, nurk, gravitatsioon=9.8, dt=0.001, suurus=10, värv=(255,0,0)) -> None:
        super().__init__(ekraan, esialgne_kiirus, nurk, gravitatsioon=gravitatsioon, dt=dt, suurus=suurus, värv=värv)
        self.tüüp = "Ruut"

    def _joonista_(self):
        """
        Joonistab ruuti andtud andmetega.
        """
        pygame.draw.rect(self.ekraan, self.värv, pygame.Rect(self.positsioon_x, self.algus_y-self.positsioon_y, self.suurus/andmed["scale"], self.suurus/andmed["scale"]))