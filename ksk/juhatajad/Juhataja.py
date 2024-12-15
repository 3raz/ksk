import pygame
from sündmused.SündmuseJuhataja import SündmuseJuhataja
from ekraan.Ekraan import Ekraan
from gui.Gui import GUI
from mudlid.SfäärÕhutakistusega import SfäärÕhutakistusega
from mudlid.Tegeleja import Tegeleja
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
        self.tegeleja = Tegeleja(self.ekraan)

        # Käivitamise kiirus, et objektid joonistatakse õigel ajal 
        self.clock = pygame.time.Clock()
        self.dt = self.clock.tick(60)
        self.dt_kiirus = 1000
        
        self.jooksmas = True


    def programm(self):
        """
        Põhiprogramm tsükel
        """
        if andmed["objektid"] != []:
            for o in andmed["objektid"]:
                self.ekraan.lisa_objekti(self.tegeleja.serialiseerija(o))


        while self.jooksmas:
            self.sündmuseJuhataja.töötle_sündmustega()
            
            if not self.jooksmas:
                break

            for i in range(len(self.ekraan.objektid)):
                self.ekraan.objektid[i].dt = self.dt/(1/andmed["gui_andmed"]["dt"])

            self.dt = self.clock.tick(60)
            
            self.gui.manager.update(self.dt/1000)
            self.ekraan.puhasta()
            
            self.gui.manager.draw_ui(self.ekraan.ekraan)
            self.ekraan.joonista_objekte()

        pygame.quit()

    def lõpeta(self):
        """
        Seab jooksmise muutuja valeks kui programm on lõpetanud
        """
        self.jooksmas = False