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

        # See kustutab tiitliriba GUI sujuvamaks integreerimiseks ekraaniga (et GUI ei näe välja nagu iseseisev osa, kuid klanitud osa põhiprogrammis). 
        if self.title_bar is not None:
            self.title_bar.kill()
            self.title_bar = None

        # See kustutab sulgemisnupu GUI sujuvamaks integreerimiseks
        if self.close_window_button is not None:
            self.close_window_button.kill()
            self.close_window_button = None

        self.margin_vertical = self.rect.height/100
        self.margin_horizontal = self.rect.width/100

        measurements = {"veerg_1": self.margin_horizontal*1, "rida_1": self.margin_vertical*1, "veerg_2": self.margin_horizontal*16, "rida_2": self.margin_vertical*16, "veerg_3": self.margin_horizontal*31, "rida_3": self.margin_vertical*31, "veerg_4": self.margin_horizontal*46, "rida_4": self.margin_vertical*46, "veerg_5": self.margin_horizontal*61, "rida_5": self.margin_vertical*61, "veerg_6": self.margin_horizontal*76, "rida_6": self.margin_vertical*76, "veerg_7": self.margin_horizontal*91, "rida_7": self.margin_vertical*91, "veerg_8": self.margin_horizontal*106, "rida_8": self.margin_vertical*106}
        slider_width = 100+self.margin_horizontal*6.5
        slider_left = self.margin_horizontal*5000
        self.test_slider = UIHorizontalSlider(pygame.Rect((slider_left, self.margin_vertical*15), (slider_width, 25)), 50.0, (0.0, 100.0), self.ui_manager, container=self, click_increment=5)
        self.slider_label = UILabel(pygame.Rect((slider_left, 0), (slider_width, 25)), str(int(self.test_slider.get_current_value())), self.ui_manager, container=self)

        




        esialgne_kiirus_left = measurements["veerg_1"]
        esialgne_kiirus_width = 50+self.margin_horizontal*6.5
        self.esialgne_kiirus = UITextEntryLine(pygame.Rect((esialgne_kiirus_left, measurements["rida_2"]), (esialgne_kiirus_width, 25)), self.ui_manager, container=self)
        self.esialgne_kiirus.set_text(str(andmed["gui_andmed"]["esialgne_kiirus"]))
        if self.esialgne_kiirus.get_text().strip() == '':
            sõne = "Undefined"
            self.esialgne_kiirus.set_text("0")
        else:
            sõne = self.esialgne_kiirus.get_text()
        self.esialgne_kiirus_sild = UILabel(pygame.Rect((esialgne_kiirus_left, measurements["rida_1"]), (esialgne_kiirus_width, 25)), "esialgne_kiirus: "+sõne, self.ui_manager, container=self)
            


        nurk_left = measurements["veerg_2"]
        nurk_width = 50+self.margin_horizontal*6.5
        self.nurk = UITextEntryLine(pygame.Rect((nurk_left, measurements["rida_2"]), (nurk_width, 25)), self.ui_manager, container=self)
        self.nurk.set_text(str(andmed["gui_andmed"]["nurk"]))
        if self.nurk.get_text().strip() == '':
            sõne = "Undefined"
            self.nurk.set_text("0")
        else:
            sõne = self.nurk.get_text()
        self.nurk_sild = UILabel(pygame.Rect((nurk_left, measurements["rida_1"]), (nurk_width, 25)), "Nurk: "+sõne, self.ui_manager, container=self)
            


        gravitatsioon_left = measurements["veerg_3"]
        gravitatsioon_width = 50+self.margin_horizontal*6.5
        self.gravitatsioon = UITextEntryLine(pygame.Rect((gravitatsioon_left, measurements["rida_2"]), (gravitatsioon_width, 25)), self.ui_manager, container=self)
        self.gravitatsioon.set_text(str(andmed["gui_andmed"]["gravitatsioon"]))
        if self.gravitatsioon.get_text().strip() == '':
            sõne = "Undefined"
            self.gravitatsioon.set_text("0")
        else:
            sõne = self.gravitatsioon.get_text()
        self.gravitatsioon_sild = UILabel(pygame.Rect((gravitatsioon_left, measurements["rida_1"]), (gravitatsioon_width, 25)), "Gravitatsioon: "+sõne, self.ui_manager, container=self)
            


        suurus_left = measurements["veerg_4"]
        suurus_width = 50+self.margin_horizontal*6.5
        self.suurus = UITextEntryLine(pygame.Rect((suurus_left, measurements["rida_2"]), (suurus_width, 25)), self.ui_manager, container=self)
        self.suurus.set_text(str(andmed["gui_andmed"]["suurus"]))
        if self.suurus.get_text().strip() == '':
            sõne = "Undefined"
            self.suurus.set_text("0")
        else:
            sõne = self.suurus.get_text()
        self.suurus_sild = UILabel(pygame.Rect((suurus_left, measurements["rida_1"]), (suurus_width, 25)), "Suurus: "+sõne, self.ui_manager, container=self)
            


        värv_left = measurements["veerg_5"]
        värv_width = 50+self.margin_horizontal*6.5
        self.värv = UITextEntryLine(pygame.Rect((värv_left, measurements["rida_2"]), (värv_width, 25)), self.ui_manager, container=self)
        _ = andmed["gui_andmed"]["värv"]
        self.värv.set_text(str(f"{_[0]},{_[1]},{_[2]}"))
        if self.värv.get_text().strip() == '':
            sõne = "Undefined"
            self.värv.set_text("0,0,0")
        else:
            sõne = self.värv.get_text()
        self.värv_sild = UILabel(pygame.Rect((värv_left, measurements["rida_1"]), (värv_width, 25)), "Värv: "+sõne, self.ui_manager, container=self)
            


        dt_left = measurements["veerg_6"]
        dt_width = 50+self.margin_horizontal*6.5
        self.dt = UITextEntryLine(pygame.Rect((dt_left, measurements["rida_2"]), (dt_width, 25)), self.ui_manager, container=self)
        self.dt.set_text(str(andmed["gui_andmed"]["dt"]))
        if self.dt.get_text().strip() == '':
            sõne = "Undefined"
            self.dt.set_text("0")
        else:
            sõne = self.dt.get_text()
        self.dt_sild = UILabel(pygame.Rect((dt_left, measurements["rida_1"]), (dt_width, 25)), "dt: "+sõne, self.ui_manager, container=self)
            




        drop_down_left = self.margin_horizontal
        drop_down_width = 50+self.margin_horizontal*6.5
        self.test_drop_down_menu = UIDropDownMenu([''],
                                                    '',
                                                  pygame.Rect((drop_down_left, measurements["rida_4"]), (drop_down_width, 25)),
                                                  self.ui_manager,
                                                  container=self)
        self.test_drop_down_menu.expand_direction = "up"

        lisa_left = self.margin_horizontal*16
        lisa_width = 50+self.margin_horizontal*6.5
        self.lisa = UIButton(pygame.Rect((lisa_left, measurements["rida_4"]), (lisa_width, 25)), "Lisa Objekti", self.ui_manager,container=self)

        puhasta_left = measurements["veerg_3"]
        puhasta_width = 50+self.margin_horizontal*6.5
        self.puhasta = UIButton(pygame.Rect((puhasta_left, measurements["rida_4"]), (puhasta_width, 25)), "Puhasta ekraani", self.ui_manager,container=self)


    def update(self, time_delta):
        super().update(time_delta)

        if self.test_slider.has_moved_recently:
            print(self.test_slider.get_current_value())
        

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
    



    
    