import pygame
from sündmused.SündmuseJuhataja import SündmuseJuhataja
from ekraan.Ekraan import Ekraan
from gui.GUI import GUI

class Juhataja:
    def __init__(self): 
        self.ekraan = Ekraan(640, 480)
        self.gui = GUI(640, 480)
        self.sündmuseJuhataja = SündmuseJuhataja(self.ekraan, self.gui)

        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60)
        self.dt_kiirus = 100000
        
        self.jooksmas = True
        

    def programm(self):
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