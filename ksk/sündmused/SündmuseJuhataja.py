import pygame
import pygame_gui
import sys
from gui.Gui import GUIEkraan
from andmed.Andmed import Andmed
from mudlid.Sfäär import Sfäär

andmed = Andmed().andmed

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

            if sündmus.type == pygame_gui.UI_BUTTON_PRESSED or sündmus.type == pygame.VIDEORESIZE:
                andmed["gui_andmed"]["esialgne_kiirus"] = float(self.gui.kinematics_window.nurk.get_text())
                andmed["gui_andmed"]["nurk"] = self.gui.kinematics_window.nurk.get_text()
                andmed["gui_andmed"]["gravitatsioon"] = float(self.gui.kinematics_window.gravitatsioon.get_text())
                andmed["gui_andmed"]["dt"] = float(self.gui.kinematics_window.dt.get_text())
                andmed["gui_andmed"]["suurus"] =float(self.gui.kinematics_window.suurus.get_text())
                andmed["gui_andmed"]["värv"] = [int(x) for x in self.gui.kinematics_window.värv.get_text().strip().split(',')]


            # Kustutab vana GUI ja ekraani ära ja initsialiseerib uued korraliku suurustega
            if sündmus.type == pygame.VIDEORESIZE:
                andmed["resolution"] = [sündmus.w, sündmus.h]
                vana_ekraan = self.ekraan.ekraan
                vana_gui = self.gui.manager
                self.ekraan.ekraan = pygame.display.set_mode((sündmus.w, sündmus.h), pygame.RESIZABLE)

                self.gui.manager = pygame_gui.UIManager((sündmus.w, sündmus.h))
                self.gui.kinematics_window = GUIEkraan(self.gui.manager)
                self.ekraan.ekraan.blit(vana_ekraan, (0,0))

                del vana_ekraan
                del vana_gui
                
                for objekt in self.ekraan.objektid:
                    objekt.alguspunkti_seadja((sündmus.w, sündmus.h-sündmus.h/andmed["gui_pikkus"]))
            

            if sündmus.type == pygame_gui.UI_BUTTON_PRESSED:
                if sündmus.ui_element == self.gui.kinematics_window.puhasta:
                    self.ekraan.kustuta_objekte()
                if sündmus.ui_element == self.gui.kinematics_window.lisa:
                    self.ekraan.lisa_objekti(Sfäär(self.ekraan.ekraan,
                                                   float(self.gui.kinematics_window.esialgne_kiirus.get_text()),
                                                   float(self.gui.kinematics_window.nurk.get_text()), 
                                                   gravitatsioon=float(self.gui.kinematics_window.gravitatsioon.get_text()),
                                                   dt=float(self.gui.kinematics_window.dt.get_text()),
                                                   suurus=float(self.gui.kinematics_window.suurus.get_text()),
                                                   värv=tuple([int(x) for x in self.gui.kinematics_window.värv.get_text().strip().split(',')])))
            

