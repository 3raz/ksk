from mudlid.Objekt import Objekt
import pygame

class Sfäär(Objekt):
    def __init__(self, ekraan, esialgne_kiirus, nurk, gravitatsioon=9.8, dt=0.001, suurus=10, värv=(255,0,0)) -> None:
        super().__init__(ekraan, esialgne_kiirus, nurk, gravitatsioon, dt, suurus, värv)
        self.tüüp = "Sfäär"

    def _joonista_(self):
        """
        Joonistab sfääri andtud andmetega.
        """
        pygame.draw.circle(self.ekraan, self.värv, (self.positsioon_x, self.algus_y-self.positsioon_y), self.suurus)