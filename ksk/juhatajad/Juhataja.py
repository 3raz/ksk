import pygame
from sündmused.SündmuseJuhataja import SündmuseJuhataja
from ekraan.Ekraan import Ekraan
from gui.GUI import GUI

class Juhataja:
    def __init__(self):
        pygame.init()   
        self.ekraan = Ekraan(640, 480)
        self.sündmuseJuhataja = SündmuseJuhataja(self.ekraan)
        self.gui = GUI()

        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60)
        
        self.jooksmas = True

    def programm(self):
        while self.jooksmas:
            self.sündmuseJuhataja.töötle_sündmustega()
            
            if not self.jooksmas:
                break

            for i in range(len(self.ekraan.objektid)):
                self.ekraan.objektid[i].dt = self.dt/250

            self.dt = self.clock.tick(60)
            self.ekraan.puhasta()
            self.ekraan.joonista_objekte()

        pygame.quit()

    def lõpeta(self):
        self.jooksmas = False