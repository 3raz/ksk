from andmed.Andmed import Andmed


import pygame_gui

from pygame_gui.elements import UIWindow
from pygame_gui.elements import UIButton
from pygame_gui.elements import UIHorizontalSlider
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UIDropDownMenu
from pygame_gui.elements import UIScreenSpaceHealthBar
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
        self.test_slider = UIHorizontalSlider(pygame.Rect((self.margin_horizontal, self.margin_vertical*15), (slider_width, 25)), 50.0, (0.0, 100.0), self.ui_manager, container=self, click_increment=5)
        self.slider_label = UILabel(pygame.Rect((self.margin_horizontal, 0), (slider_width, 25)), str(int(self.test_slider.get_current_value())), self.ui_manager, container=self)

        self.test_text_entry = UITextEntryLine(pygame.Rect((int(self.rect.width / 2), int(self.rect.height * 0.50)), (200, -1)), self.ui_manager, container=self)
        self.test_text_entry.set_forbidden_characters('numbers')

        drop_down_width = 100+self.margin_horizontal*6.5
        current_resolution_string = 'Item 1'
        self.test_drop_down_menu = UIDropDownMenu(['Item 1',
                                                   'Item 2',
                                                   'Item 3'
                                                   ],
                                                  current_resolution_string,
                                                  pygame.Rect((self.margin_horizontal*5+slider_width, self.margin_vertical*15),
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
    



    
    