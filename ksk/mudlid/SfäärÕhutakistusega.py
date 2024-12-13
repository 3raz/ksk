from mudlid.ObjektÕhutakistusega import ObjektÕhutakistusega
import pygame

class SfäärÕhutakistusega(ObjektÕhutakistusega):
    def __init__(self, ekraan, esialgne_kiirus: float, nurk: float, gravitatsioon: float=9.81, 
                 suurus: float=10, värv: tuple=(255,255,255), raskus: float=10, dt: float=0.000334, tõmbetegur: float=0.295, õhu_tihedus: float=1.225):
        super().__init__(ekraan, esialgne_kiirus, nurk, gravitatsioon, dt, suurus, raskus, värv=värv, tõmbetegur=tõmbetegur, õhu_tihedus=õhu_tihedus)
        self.tüüp = "Sfäär Õhutakistusega"

    def _joonista_(self):
        """
        Joonistab sfääri andtud andmetega.
        """
        pygame.draw.circle(self.ekraan, self.värv, (self.positsioon_x, self.algus_y-self.positsioon_y), self.suurus*50)