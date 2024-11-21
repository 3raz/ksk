from andmed.Andmed import Andmed


import pygame_gui

from pygame_gui.elements import UIWindow
from pygame_gui.elements import UIHorizontalSlider
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UIDropDownMenu
from pygame_gui.elements import UILabel

import pygame

andmed = Andmed().andmed

class GUIEkraan(UIWindow):
    def __init__(self, ui_manager):
        ekraani_suurus_x, ekraani_suurus_y  = andmed["resolution"]
        self.pikkus = andmed["gui_pikkus"]
        super().__init__(pygame.Rect((0, ekraani_suurus_y-ekraani_suurus_y/self.pikkus), (ekraani_suurus_x, ekraani_suurus_y/self.pikkus)), ui_manager, object_id='#gui_window', resizable=False, draggable=False)

        # See kustutab tiitliriba GUI sujuvamaks integreerimiseks 
        if self.title_bar is not None:
            self.title_bar.kill()
            self.title_bar = None

        # See kustutab sulgemisnupu GUI sujuvamaks integreerimiseks
        if self.close_window_button is not None:
            self.close_window_button.kill()
            self.close_window_button = None

        self.margin_vertical = self.rect.height/100
        self.margin_horizontal = self.rect.width/100
        print(self.margin_vertical, self.margin_horizontal)

        slider_width = 100+self.margin_horizontal*6.5
        slider_left = self.margin_horizontal*5000
        self.test_slider = UIHorizontalSlider(pygame.Rect((slider_left, self.margin_vertical*15), (slider_width, 25)), 50.0, (0.0, 100.0), self.ui_manager, container=self, click_increment=5)
        self.slider_label = UILabel(pygame.Rect((slider_left, 0), (slider_width, 25)), str(int(self.test_slider.get_current_value())), self.ui_manager, container=self)

        



        esialgne_kiirus_left = self.margin_horizontal*1
        esialgne_kiirus_width = 50+self.margin_horizontal*6.5
        self.esialgne_kiirus = UITextEntryLine(pygame.Rect((esialgne_kiirus_left, self.margin_vertical*15), (esialgne_kiirus_width, 25)), self.ui_manager, container=self)
        if self.esialgne_kiirus.get_text().strip() == '':
            sõne = "Undefined"
        else:
            sõne = self.esialgne_kiirus.get_text()
        self.esialgne_kiirus_sild = UILabel(pygame.Rect((esialgne_kiirus_left, 0), (esialgne_kiirus_width, 25)), "Esialgne Kiirus: "+sõne, self.ui_manager, container=self)
            


        nurk_left = self.margin_horizontal*16
        nurk_width = 50+self.margin_horizontal*6.5
        self.nurk = UITextEntryLine(pygame.Rect((nurk_left, self.margin_vertical*15), (nurk_width, 25)), self.ui_manager, container=self)
        if self.nurk.get_text().strip() == '':
            sõne = "Undefined"
        else:
            sõne = self.nurk.get_text()
        self.nurk_sild = UILabel(pygame.Rect((nurk_left, 0), (nurk_width, 25)), "Nurk: "+sõne, self.ui_manager, container=self)
            


        gravitatsioon_left = self.margin_horizontal*31
        gravitatsioon_width = 50+self.margin_horizontal*6.5
        self.gravitatsioon = UITextEntryLine(pygame.Rect((gravitatsioon_left, self.margin_vertical*15), (gravitatsioon_width, 25)), self.ui_manager, container=self)
        if self.gravitatsioon.get_text().strip() == '':
            sõne = "Undefined"
        else:
            sõne = self.gravitatsioon.get_text()
        self.gravitatsioon_sild = UILabel(pygame.Rect((gravitatsioon_left, 0), (gravitatsioon_width, 25)), "Gravitatsioon: "+sõne, self.ui_manager, container=self)
            


        suurus_left = self.margin_horizontal*46
        suurus_width = 50+self.margin_horizontal*6.5
        self.suurus = UITextEntryLine(pygame.Rect((suurus_left, self.margin_vertical*15), (suurus_width, 25)), self.ui_manager, container=self)
        if self.suurus.get_text().strip() == '':
            sõne = "Undefined"
        else:
            sõne = self.suurus.get_text()
        self.suurus_sild = UILabel(pygame.Rect((suurus_left, 0), (suurus_width, 25)), "Suurus: "+sõne, self.ui_manager, container=self)
            


        värv_left = self.margin_horizontal*61
        värv_width = 50+self.margin_horizontal*6.5
        self.värv = UITextEntryLine(pygame.Rect((värv_left, self.margin_vertical*15), (värv_width, 25)), self.ui_manager, container=self)
        if self.värv.get_text().strip() == '':
            sõne = "Undefined"
        else:
            sõne = self.värv.get_text()
        self.värv_sild = UILabel(pygame.Rect((värv_left, 0), (värv_width, 25)), "Värv: "+sõne, self.ui_manager, container=self)
            


        dt_left = self.margin_horizontal*76
        dt_width = 50+self.margin_horizontal*6.5
        self.dt = UITextEntryLine(pygame.Rect((dt_left, self.margin_vertical*15), (dt_width, 25)), self.ui_manager, container=self)
        if self.dt.get_text().strip() == '':
            sõne = "Undefined"
        else:
            sõne = self.dt.get_text()
        self.dt_sild = UILabel(pygame.Rect((dt_left, 0), (dt_width, 25)), "dt: "+sõne, self.ui_manager, container=self)
            



 






        drop_down_width = 100+self.margin_horizontal*6.5
        current_resolution_string = 'Item 1'
        self.test_drop_down_menu = UIDropDownMenu(['Item 1',
                                                   'Item 2',
                                                   'Item 3'
                                                   ],
                                                  current_resolution_string,
                                                  pygame.Rect((self.margin_horizontal*500, self.margin_vertical*15),
                                                              (drop_down_width, 25)),
                                                  self.ui_manager,
                                                  container=self)


    def update(self, time_delta):
        super().update(time_delta)

        if self.alive() and self.test_slider.has_moved_recently:
            print(self.test_slider.get_current_value())

class GUI:
    def __init__(self):
        self.suurus_x, self.suurus_y = andmed["resolution"]
        self.background = pygame.Surface((self.suurus_x, self.suurus_y))
        self.background.fill(pygame.Color('#707070'))

        self.manager = pygame_gui.UIManager((self.suurus_x, self.suurus_y))

        self.kinematics_window = GUIEkraan(self.manager)

    @property
    def gui_võtja(self):
        return self.manager
    



    
    