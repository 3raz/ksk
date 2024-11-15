import random
import pygame_gui
from collections import deque
from typing import Optional

from pygame_gui import UIManager, PackageResource

from pygame_gui.elements import UIWindow
from pygame_gui.elements import UIButton
from pygame_gui.elements import UIHorizontalSlider
from pygame_gui.elements import UITextEntryLine
from pygame_gui.elements import UIDropDownMenu
from pygame_gui.elements import UIScreenSpaceHealthBar
from pygame_gui.elements import UILabel
from pygame_gui.elements import UIImage
from pygame_gui.elements import UIPanel
from pygame_gui.elements import UISelectionList

from pygame_gui.windows import UIMessageWindow
from pygame_gui.core import ObjectID


import pygame


class GUIEkraan(UIWindow):
    def __init__(self, ui_manager, dimensions=(512,512)):
        super().__init__(pygame.Rect((50, 50), dimensions), ui_manager,
                         window_display_title='GUI',
                         object_id='#gui_window',
                         resizable=True)

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

        self.health_bar = UIScreenSpaceHealthBar(pygame.Rect((int(self.rect.width / 9),
                                                              int(self.rect.height * 0.7)),
                                                             (200, 30)),
                                                 self.ui_manager,
                                                 container=self)

    def update(self, time_delta):
        super().update(time_delta)

        if self.alive() and self.test_slider.has_moved_recently:
            print(self.test_slider.get_current_value())

class GUI:
    def __init__(self, suurus_x, suurus_y):
        self.background = pygame.Surface((suurus_x, suurus_y))
        self.background.fill(pygame.Color('#707070'))

        self.manager = pygame_gui.UIManager((suurus_x, suurus_y), "data/themes/kinematics_theme.json")

        self.kinematics_window = GUIEkraan(self.manager)

    @property
    def gui_võtja(self):
        return self.manager
    



    
    