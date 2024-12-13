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
                continue
                self.ekraan.lisa_objekti(self.tegeleja.serialiseerija(o))

        o = SfäärÕhutakistusega(self.ekraan.ekraan, 300, 45, suurus=7.62e-3, raskus=8.4e-3, värv=(255,0,0), tõmbetegur=0.295, suurus_kordja=1000)
        p = SfäärÕhutakistusega(self.ekraan.ekraan, 441, 45, suurus=4.57e-3/2, raskus=5.7e-4, värv=(255,0,255), suurus_kordja=1000)
        q = SfäärÕhutakistusega(self.ekraan.ekraan, 1555, 45, suurus=0.06, raskus=23, värv=(255,255,0), tõmbetegur=0.295, suurus_kordja=100)
        # r = SfäärÕhutakistusega(self.ekraan.ekraan, 200, 45, suurus=0.4,värv=(0,0,255))
        o.alguspunkti_seadja((self.ekraan.suurus_x, self.ekraan.suurus_y-self.ekraan.suurus_y/andmed["gui_pikkus"]))
        p.alguspunkti_seadja((self.ekraan.suurus_x, self.ekraan.suurus_y-self.ekraan.suurus_y/andmed["gui_pikkus"]))
        q.alguspunkti_seadja((self.ekraan.suurus_x, self.ekraan.suurus_y-self.ekraan.suurus_y/andmed["gui_pikkus"]))
        # r.alguspunkti_seadja((self.ekraan.suurus_x, self.ekraan.suurus_y-self.ekraan.suurus_y/andmed["gui_pikkus"]))
        self.ekraan.lisa_objekti(o)
        self.ekraan.lisa_objekti(p)
        self.ekraan.lisa_objekti(q)
        # self.ekraan.lisa_objekti(r)
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