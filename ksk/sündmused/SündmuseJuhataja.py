import pygame
import pygame_gui
import sys
from gui.Gui import GUIEkraan
from andmed.Andmed import Andmed

a = Andmed()


class SündmuseJuhataja:
    
    def __init__(self, ekraan, gui):
        self.ekraan = ekraan
        self.gui = gui

        self.a = Andmed()

    def töötle_sündmustega(self):
        """Töötle pygame'i sündmustega"""
        for sündmus in pygame.event.get():
            if sündmus.type == pygame.QUIT:
                # Python ei taga destruktorite kutsumist, seega tuleb kasutada seda inetut lahendust
                del self.gui
                self.ekraan.__del__()
                del self.ekraan
                self.a.__del__()
                del self.a
                sys.exit()
            self.gui.manager.process_events(sündmus)

            # Kustutab vana GUI ja ekraani ära ja initsialiseerib uued korraliku suurustega
            if sündmus.type == pygame.VIDEORESIZE:
                self.a.andmed["resolution"] = [sündmus.w, sündmus.h]
                vana_ekraan = self.ekraan.ekraan
                vana_gui = self.gui.manager
                self.ekraan.ekraan = pygame.display.set_mode((sündmus.w, sündmus.h), pygame.RESIZABLE)

                self.gui.manager = pygame_gui.UIManager((sündmus.w, sündmus.h))
                self.gui.kinematics_window = GUIEkraan(self.gui.manager)
                self.ekraan.ekraan.blit(vana_ekraan, (0,0))

                del vana_ekraan
                del vana_gui
                
                for objekt in self.ekraan.objektid:
                    objekt.alguspunkti_seadja((sündmus.w, sündmus.h-sündmus.h/self.a.andmed["gui_pikkus"]))