import pygame
import pygame_gui
import sys
from gui.Gui import GUIEkraan
from andmed.Andmed import Andmed
from mudlid.Sfäär import Sfäär
from gui.GuiParser import GuiParser
from threading import Thread

andmed = Andmed().andmed

class SündmuseJuhataja:
    
    def __init__(self, ekraan, gui):
        self.ekraan = ekraan
        self.gui = gui
        self.gui_parser = GuiParser()

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
                o = self.create_object()
                if o != None:
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
                self.ekraan.värskenda_resolution()

                del vana_ekraan
                del vana_gui
                
                for objekt in self.ekraan.objektid:
                    objekt.alguspunkti_seadja((sündmus.w, sündmus.h-sündmus.h/andmed["gui_pikkus"]))
            

            if sündmus.type == pygame_gui.UI_BUTTON_PRESSED:
                if sündmus.ui_element == self.gui.kinematics_window.puhasta:
                    self.ekraan.kustuta_objekte()
                if sündmus.ui_element == self.gui.kinematics_window.lisa:
                    o = self.create_object()
                    if o == None:
                        print("Bad info")
                    else:
                        self.gui.kinematics_window.set_most_recent_object(o)
                        self.gui.kinematics_window.objekti_menüü.add_options([self.gui.kinematics_window.approximate_color(o.värv)])
                        self.ekraan.lisa_objekti(o)

    def create_object(self) -> object:
        """
        Lisab objekti ekraanile antud andmetega. Saaks ka selle funktsiooni kasutada info kontrollijana.
        """
        esialgne_kiirus = self.gui_parser.positiivne_number(self.gui.kinematics_window.esialgne_kiirus.get_text())
        nurk = self.gui_parser.nurk(self.gui.kinematics_window.nurk.get_text())
        gravitatsioon = self.gui_parser.number(self.gui.kinematics_window.gravitatsioon.get_text())
        dt = self.gui_parser.number(self.gui.kinematics_window.dt.get_text())
        suurus = self.gui_parser.positiivne_number(self.gui.kinematics_window.suurus.get_text())
        värv = self.gui_parser.värv(self.gui.kinematics_window.värv.get_text())

        if dt == None:
            dt = 0.001

        info = [esialgne_kiirus, nurk, gravitatsioon, suurus, värv]
        for asi in info:
            if asi == None:
                return None


        o = Sfäär(self.ekraan.ekraan,
                                        esialgne_kiirus,
                                        nurk, 
                                        gravitatsioon=gravitatsioon,
                                        dt=dt,
                                        suurus=suurus,
                                        värv=värv)
        
        return o

            

