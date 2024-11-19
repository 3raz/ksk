import pygame
from sündmused.SündmuseJuhataja import SündmuseJuhataja
from ekraan.Ekraan import Ekraan
from gui.Gui import GUI
from mudlid.Sfäär import Sfäär
from mudlid.Ruut import Ruut
from andmed.Andmed import Andmed

andmed = Andmed().andmed

class Juhataja:
    def __init__(self):
        """
        See initsialiseerib kõik olulised mudlid
        """
        self.ekraan = Ekraan()
        self.gui = GUI()
        self.sündmuseJuhataja = SündmuseJuhataja(self.ekraan, self.gui)

        # Käivitamise kiirus, et objektid joonistatakse õigel ajal 
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60)
        self.dt_kiirus = 1000
        
        self.jooksmas = True

    def serialiseerija(self, andmed: dict) -> object:
        tüüp = andmed["tüüp"]

        if tüüp == "Sfäär":
            return Sfäär(self.ekraan.ekraan, andmed["esialgne_kiirus"], andmed["nurk"], gravitatsioon=andmed["gravitatsioon"], dt=andmed["dt"], suurus=andmed["suurus"], värv=andmed["värv"])

        elif tüüp == "Ruut":
            return Ruut(self.ekraan.ekraan, andmed["esialgne_kiirus"], andmed["nurk"], gravitatsioon=andmed["gravitatsioon"], dt=andmed["dt"], suurus=andmed["suurus"], värv=andmed["värv"])
        
        else:
            return Sfäär(self.ekraan.ekraan, andmed["esialgne_kiirus"], andmed["nurk"], gravitatsioon=andmed["gravitatsioon"], dt=andmed["dt"], suurus=andmed["suurus"], värv=andmed["värv"])

    def programm(self):
        """
        Põhiprogramm tsükel
        """
        print(andmed["objektid"])
        if andmed["objektid"] != []:
            for o in andmed["objektid"]:
                self.ekraan.lisa_objekti(self.serialiseerija(o))

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