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

        self.margin_vertical = self.rect.height/100
        self.margin_horizontal = self.rect.width/100

        self.test_slider = UIHorizontalSlider(pygame.Rect((int(self.margin_horizontal),
                                                           self.margin_vertical),
                                                          (240, 25)),
                                              50.0,
                                              (0.0, 100.0),
                                              self.ui_manager,
                                              container=self,
                                              click_increment=5)

        self.slider_label = UILabel(pygame.Rect((int(self.rect.width / 2) + 250,
                                                 int(self.rect.height * 0.70)),
                                                (28, 25)),
                                    str(int(self.test_slider.get_current_value())),
                                    self.ui_manager,
                                    container=self)

        self.test_text_entry = UITextEntryLine(pygame.Rect((int(self.rect.width / 2),
                                                            int(self.rect.height * 0.50)),
                                                           (200, -1)),
                                               self.ui_manager,
                                               container=self)
        self.test_text_entry.set_forbidden_characters('numbers')

        current_resolution_string = 'Item 1'
        self.test_drop_down_menu = UIDropDownMenu(['Item 1',
                                                   'Item 2',
                                                   'Item 3',
                                                   'Item 4',
                                                   'Item 5',
                                                   'Item 6',
                                                   'Item 7',
                                                   'Item 8',
                                                   'Item 9',
                                                   'Item 10',
                                                   'Item 11',
                                                   'Item 12',
                                                   'Item 13',
                                                   'Item 14',
                                                   'Item 15',
                                                   'Item 16',
                                                   'Item 17',
                                                   'Item 18',
                                                   'Item 19',
                                                   'Item 20',
                                                   'Item 21',
                                                   'Item 22',
                                                   'Item 23',
                                                   'Item 24',
                                                   'Item 25',
                                                   'Item 26',
                                                   'Item 27',
                                                   'Item 28',
                                                   'Item 29',
                                                   'Item 30'
                                                   ],
                                                  current_resolution_string,
                                                  pygame.Rect((int(self.rect.width / 2),
                                                               int(self.rect.height * 0.3)),
                                                              (200, 25)),
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
    



    
    