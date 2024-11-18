import pygame
from sündmused.SündmuseJuhataja import SündmuseJuhataja
from ekraan.Ekraan import Ekraan
from gui.Gui import GUI

class Juhataja:
    def __init__(self):
        """
        See initsialiseerib kõik olulised mudlid
        """
        self.ekraan = Ekraan(640*2, 480*2)
        self.gui = GUI(640, 480, self.ekraan)
        self.sündmuseJuhataja = SündmuseJuhataja(self.ekraan, self.gui)

        # Käivitamise kiirus, et objektid joonistatakse õigel ajal 
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60)
        self.dt_kiirus = 1000
        
        self.jooksmas = True
        

    def programm(self):
        """
        Põhiprogramm tsükel
        """
        while self.jooksmas:
            self.sündmuseJuhataja.töötle_sündmustega()
            
            if not self.jooksmas:
                break

            for i in range(len(self.ekraan.objektid)):
                self.ekraan.objektid[i].dt = self.dt/self.dt_kiirus

            self.dt = self.clock.tick(60)
            
            self.gui.manager.update(self.dt/1000)
            self.ekraan.puhasta()
            
            self.gui.manager.draw_ui(self.ekraan.ekraan)
            self.ekraan.joonista_objekte()

        pygame.quit()

    def lõpeta(self):
        self.jooksmas = False