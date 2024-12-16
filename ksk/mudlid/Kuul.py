from mudlid.ObjektKuul import ObjektKuul
import pygame

class Kuul(ObjektKuul):
    def __init__(self, ekraan, esialgne_kiirus: float, nurk: float, gravitatsioon: float=9.81, 
                 suurus: float=10, värv: tuple=(255,255,255), raskus: float=0.00803, dt: float=0.000334, tõmbekoefitsient: float=0.29, 
                 õhu_tihedus: float=1.225, ballistilinekoefitsient: float=0.15, suurus_kordja: float = 10):
        """
        Suurus on tegelikult raadius
        """
        super().__init__(ekraan, esialgne_kiirus, nurk, gravitatsioon, dt, suurus, raskus, värv=värv, 
                         tõmbekoefitsient=tõmbekoefitsient, õhu_tihedus=õhu_tihedus, ballistilinekoefitsient=ballistilinekoefitsient)
        self.tüüp = "Kuul"
        self.suurus_kordja = suurus_kordja

    def _joonista_(self):
        """
        Joonistab kuuli andtud andmetega.
        """
        pygame.draw.circle(self.ekraan, self.värv, (self.positsioon_x, self.algus_y-self.positsioon_y), self.suurus)