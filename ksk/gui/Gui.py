from andmed.Andmed import Andmed


import pygame_gui

from pygame_gui.elements import UIWindow
from pygame_gui.elements import UIHorizontalSlider
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UIDropDownMenu
from pygame_gui.elements import UILabel
from pygame_gui.elements import UIButton

import pygame

andmed = Andmed().andmed

class GUIEkraan(UIWindow):
    def __init__(self, ui_manager):
        ekraani_suurus_x, ekraani_suurus_y  = andmed["resolution"]
        self.pikkus = andmed["gui_pikkus"]
        super().__init__(pygame.Rect((0, ekraani_suurus_y-ekraani_suurus_y/self.pikkus), (ekraani_suurus_x, ekraani_suurus_y/self.pikkus)), ui_manager, object_id='#gui_window', resizable=False, draggable=False)

        self.o = None

        # See kustutab tiitliriba GUI sujuvamaks integreerimiseks ekraaniga (et GUI ei näe välja nagu iseseisev osa, kuid klanitud osa põhiprogrammis). 
        if self.title_bar is not None:
            self.title_bar.kill()
            self.title_bar = None

        # See kustutab sulgemisnupu GUI sujuvamaks integreerimiseks
        if self.close_window_button is not None:
            self.close_window_button.kill()
            self.close_window_button = None


        # -------------------- GUI NUPUDE, TEKSTKASTIDE, TEKSTISILTIDE JA RIPPUMENÜÜDE OSA -------------------- #  

        self.margin_vertical = self.rect.height/100
        self.margin_horizontal = self.rect.width/150

        measurements = {"veerg_1": self.margin_horizontal*1, "rida_1": self.margin_vertical*1, "veerg_2": self.margin_horizontal*16, "rida_2": self.margin_vertical*16, "veerg_3": self.margin_horizontal*31, "rida_3": self.margin_vertical*31, "veerg_4": self.margin_horizontal*46, "rida_4": self.margin_vertical*46, "veerg_5": self.margin_horizontal*61, "rida_5": self.margin_vertical*61, "veerg_6": self.margin_horizontal*76, "rida_6": self.margin_vertical*76, "veerg_7": self.margin_horizontal*91, "rida_7": self.margin_vertical*91, "veerg_8": self.margin_horizontal*106, "rida_8": self.margin_vertical*106, "veerg_9": self.margin_horizontal*121}

        nupp_laius = 50+self.margin_horizontal*6.5

        self.esialgne_kiirus = UITextEntryLine(pygame.Rect((measurements["veerg_1"], measurements["rida_2"]), (nupp_laius, 25)), self.ui_manager, container=self)
        self.esialgne_kiirus.set_text(str(andmed["gui_andmed"]["esialgne_kiirus"]))
        if self.esialgne_kiirus.get_text().strip() == '':
            sõne = "Määratlemata"
            self.esialgne_kiirus.set_text("0")
        else:
            sõne = self.esialgne_kiirus.get_text()
        self.esialgne_kiirus_sild = UILabel(pygame.Rect((measurements["veerg_1"], measurements["rida_1"]), (nupp_laius, 25)), "Esialgne kiirus: "+sõne, self.ui_manager, container=self)
            

        self.nurk = UITextEntryLine(pygame.Rect((measurements["veerg_2"], measurements["rida_2"]), (nupp_laius, 25)), self.ui_manager, container=self)
        self.nurk.set_text(str(andmed["gui_andmed"]["nurk"]))
        if self.nurk.get_text().strip() == '':
            sõne = "Määratlemata"
            self.nurk.set_text("0")
        else:
            sõne = self.nurk.get_text()
        self.nurk_sild = UILabel(pygame.Rect((measurements["veerg_2"], measurements["rida_1"]), (nupp_laius, 25)), "Nurk: "+sõne, self.ui_manager, container=self)
            


        self.gravitatsioon = UITextEntryLine(pygame.Rect((measurements["veerg_3"], measurements["rida_2"]), (nupp_laius, 25)), self.ui_manager, container=self)
        self.gravitatsioon.set_text(str(andmed["gui_andmed"]["gravitatsioon"]))
        if self.gravitatsioon.get_text().strip() == '':
            sõne = "Määratlemata"
            self.gravitatsioon.set_text("0")
        else:
            sõne = self.gravitatsioon.get_text()
        self.gravitatsioon_sild = UILabel(pygame.Rect((measurements["veerg_3"], measurements["rida_1"]), (nupp_laius, 25)), "Gravitatsioon: "+sõne, self.ui_manager, container=self)
            


        self.suurus = UITextEntryLine(pygame.Rect((measurements["veerg_4"], measurements["rida_2"]), (nupp_laius, 25)), self.ui_manager, container=self)
        self.suurus.set_text(str(andmed["gui_andmed"]["suurus"]))
        if self.suurus.get_text().strip() == '':
            sõne = "Määratlemata"
            self.suurus.set_text("0")
        else:
            sõne = self.suurus.get_text()
        self.suurus_sild = UILabel(pygame.Rect((measurements["veerg_4"], measurements["rida_1"]), (nupp_laius, 25)), "Suurus: "+sõne, self.ui_manager, container=self)
            


        self.värv = UITextEntryLine(pygame.Rect((measurements["veerg_5"], measurements["rida_2"]), (nupp_laius, 25)), self.ui_manager, container=self)
        _ = andmed["gui_andmed"]["värv"]
        self.värv.set_text(str(f"{_[0]},{_[1]},{_[2]}"))
        if self.värv.get_text().strip() == '':
            sõne = "Määratlemata"
            self.värv.set_text("0,0,0")
        else:
            sõne = self.värv.get_text()
        self.värv_sild = UILabel(pygame.Rect((measurements["veerg_5"], measurements["rida_1"]), (nupp_laius, 25)), "Värv: "+sõne, self.ui_manager, container=self)
            


        self.dt = UITextEntryLine(pygame.Rect((measurements["veerg_6"], measurements["rida_2"]), (nupp_laius, 25)), self.ui_manager, container=self)
        self.dt.set_text(str(andmed["gui_andmed"]["dt"]))
        if self.dt.get_text().strip() == '':
            sõne = "Määratlemata"
            self.dt.set_text("0")
        else:
            sõne = self.dt.get_text()
        self.dt_sild = UILabel(pygame.Rect((measurements["veerg_6"], measurements["rida_1"]), (nupp_laius, 25)), "dt: "+sõne, self.ui_manager, container=self)


        self.raskus = UITextEntryLine(pygame.Rect((measurements["veerg_6"], measurements["rida_4"]), (nupp_laius, 25)), self.ui_manager, container=self)
        self.raskus.set_text(str(andmed["gui_andmed"]["raskus"]))
        if self.raskus.get_text().strip() == '':
            sõne = "Määratlemata"
            self.raskus.set_text("1")
        else:
            sõne = self.raskus.get_text()
        self.raskus_sild = UILabel(pygame.Rect((measurements["veerg_6"], measurements["rida_3"]), (nupp_laius, 25)), "Raskus (kg): "+sõne, self.ui_manager, container=self)
        

        self.tõmbetegur = UITextEntryLine(pygame.Rect((measurements["veerg_7"], measurements["rida_4"]), (nupp_laius, 25)), self.ui_manager, container=self)
        self.tõmbetegur.set_text(str(andmed["gui_andmed"]["tõmbetegur"]))
        if self.tõmbetegur.get_text().strip() == '':
            sõne = "Määratlemata"
            self.tõmbetegur.set_text("0.47")
        else:
            sõne = self.tõmbetegur.get_text()
        self.tõmbetegur_sild = UILabel(pygame.Rect((measurements["veerg_7"], measurements["rida_3"]), (nupp_laius, 25)), "Tõmbetegur: "+sõne, self.ui_manager, container=self)
            

        self.õhu_tihedus = UITextEntryLine(pygame.Rect((measurements["veerg_8"], measurements["rida_4"]), (nupp_laius, 25)), self.ui_manager, container=self)
        self.õhu_tihedus.set_text(str(andmed["gui_andmed"]["õhu_tihedus"]))
        if self.õhu_tihedus.get_text().strip() == '':
            sõne = "Määratlemata"
            self.õhu_tihedus.set_text("1.225")
        else:
            sõne = self.õhu_tihedus.get_text()
        self.õhu_tihedus_sild = UILabel(pygame.Rect((measurements["veerg_8"], measurements["rida_3"]), (nupp_laius, 25)), "Õhu tihedus: "+sõne, self.ui_manager, container=self)
            

        järjend = [key for key, _ in andmed["session_objects"].items()]
        self.objekti_menüü = UIDropDownMenu(järjend,
                                                    '',
                                                  pygame.Rect((measurements["veerg_1"], measurements["rida_4"]), (nupp_laius, 25)),
                                                  self.ui_manager,
                                                  container=self)
        self.objekti_menüü.expand_direction = "up"
        

        self.lisa = UIButton(pygame.Rect((measurements["veerg_2"], measurements["rida_4"]), (nupp_laius, 25)), "Lisa Objekt", self.ui_manager,container=self)

        self.puhasta = UIButton(pygame.Rect((measurements["veerg_3"], measurements["rida_4"]), (nupp_laius, 25)), "Puhasta ekraan", self.ui_manager,container=self)

        self.lisa_järjendist = UIButton(pygame.Rect((measurements["veerg_2"], measurements["rida_3"]), (nupp_laius, 25)), "Lisa järjendist", self.ui_manager,container=self)

        self.lisa_kõike = UIButton(pygame.Rect((measurements["veerg_4"], measurements["rida_4"]), (nupp_laius, 25)), "Lisa Kõike Järjendist", self.ui_manager,container=self)

        self.kustuta_kõike = UIButton(pygame.Rect((measurements["veerg_3"], measurements["rida_3"]), (nupp_laius, 25)), "Puhasta järjendi", self.ui_manager,container=self)

        self.salvesta = UIButton(pygame.Rect((measurements["veerg_4"], measurements["rida_3"]), (nupp_laius, 25)), "Salvesta andmed", self.ui_manager,container=self)


        self.aeg = UILabel(pygame.Rect((measurements["veerg_7"], measurements["rida_2"]), (nupp_laius, 25)), "Reaalaeg: Määratlemata", self.ui_manager, container=self)

        self.kaugus = UILabel(pygame.Rect((measurements["veerg_8"], measurements["rida_2"]), (nupp_laius, 25)), "X-positsioon: Määratlemata", self.ui_manager, container=self)

        self.kõrgus = UILabel(pygame.Rect((measurements["veerg_9"], measurements["rida_2"]), (nupp_laius, 25)), "Y-positsioon: Määratlemata", self.ui_manager, container=self)

        self.režiimi_sild = UILabel(pygame.Rect((measurements["veerg_5"], measurements["rida_3"]), (nupp_laius, 25)), "Ilma õhutakistuseta", self.ui_manager, container=self)
        self.režiim = UIButton(pygame.Rect((measurements["veerg_5"], measurements["rida_4"]), (nupp_laius, 25)), "Vaheta režiimi", self.ui_manager,container=self)

        # -------------------- GUI NUPUDE, TEKSTKASTIDE, TEKSTISILTIDE JA RIPPUMENÜÜDE OSA LÕPP -------------------- #  

    def set_most_recent_object(self, o: object):
        """
        Seab kõige uusima objekti
        """
        self.o = o

    def update(self, time_delta):
        """
        Värskendab aja tekstisildi ja 
        """
        super().update(time_delta)
        if self.o != None:
            self.aeg.set_text("Reaalaeg: " + str(round(self.o.aeg, 2)))
            self.kaugus.set_text("X-positsioon: " + str(round(self.o.positsioon_x*andmed["scale"], 2)))
            self.kõrgus.set_text("Y-positsioon: " + str(round(self.o.positsioon_y*andmed["scale"], 2)))

    @staticmethod
    def approximate_color(rgb):
        """
        Ligikaudne RGB-väärtuse värvinimi.
        """

        reference_colors = {
            "must": (0, 0, 0),
            "valge": (255, 255, 255),
            "punane": (255, 0, 0),
            "roheline": (0, 255, 0),
            "sinine": (0, 0, 255),
            "kollane": (255, 255, 0),
            "tsüaan": (0, 255, 255),
            "magenta": (255, 0, 255),
            "hall": (128, 128, 128),
            "oranž": (255, 165, 0),
            "roosa": (255, 182, 193),
            "lilla": (128, 0, 200),
            "tumepunane": (139, 0, 0),
            "tumeroheline": (0, 100, 0),
            "tumesinine": (0, 0, 139),
            "helesinine": (173, 216, 230),
            "heleroheline": (144, 238, 144),
            "helepunane": (255, 102, 102),
            "tumehall": (64, 64, 64),
            "helehall": (192, 192, 192),
        }

        # Kaugus kahe punktide vahel
        def color_distance(c1, c2):
            return ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2 + (c1[2] - c2[2]) ** 2) ** 0.5

        # Leiab kaugusi color_distance'i funktsiooniga len(reference_colors)'iga siis tagastab see värv, mis on kõige lähedal.
        closest_color = min(reference_colors, key=lambda color: color_distance(rgb, reference_colors[color]))

        return closest_color
        

class GUI:
    def __init__(self):
        self.suurus_x, self.suurus_y = andmed["resolution"]
        self.background = pygame.Surface((self.suurus_x, self.suurus_y))
        self.background.fill(pygame.Color('#707070'))

        self.manager = pygame_gui.UIManager((self.suurus_x, self.suurus_y), 'ksk/andmed/themes/theme.json')

        self.kinematics_window = GUIEkraan(self.manager)
        
    @property
    def gui_võtja(self):
        return self.manager
    



    
    