import re
from collections import OrderedDict
from os import listdir, linesep
from os.path import isfile, join, basename, splitext

import pygame
import pygame_gui

from pygame_gui.elements import UITextBox

class GUIWindow(pygame_gui.elements.UIWindow):
    def __init__(self, manager):
        super().__init__(pygame.Rect((200, 50), (420, 520)),
                         manager,
                         window_display_title='Kinemaatikud',
                         object_id="#kinematics_window")

        input_bar_top_margin = 2
        input_bar_bottom_margin = 2
        self.input_box = pygame_gui.elements.UITextEntryLine(pygame.Rect((150, input_bar_top_margin), (230, 30)), manager=manager, container=self, parent_element=self)

        self.input_label = pygame_gui.elements.UILabel(pygame.Rect((90, input_bar_top_margin), (56, self.input_box.rect.height)), "Input:", manager=manager, container=self, parent_element=self)

        self.home_button = pygame_gui.elements.UIButton(pygame.Rect((20, input_bar_top_margin), (29, 29)), '', manager=manager, container=self, parent_element=self, object_id='#home_button')

        self.remaining_window_size = (self.get_container().get_size()[0], (self.get_container().get_size()[1] - (self.input_box.rect.height + input_bar_top_margin + input_bar_bottom_margin)))

        self.pages = {}
        page_path = 'ksk/data/kinematics/'
        file_paths = [join(page_path, f) for f in listdir(page_path) if isfile(join(page_path, f))]
        for file_path in file_paths:
            with open(file_path, 'r') as page_file:
                file_id = splitext(basename(file_path))[0]
                file_data = ""
                for line in page_file:
                    line = line.rstrip(linesep).lstrip()
                    if len(line) > 0:
                        if line[-1] != '>':
                            line += ' '
                        file_data += line
                self.pages[file_id] = file_data

        index_page = self.pages['index']
        self.page_y_start_pos = (self.input_box.rect.height + input_bar_top_margin + input_bar_bottom_margin)
        self.page_display = UITextBox(index_page, pygame.Rect((0, self.page_y_start_pos), self.remaining_window_size), manager=manager, container=self, parent_element=self)

    def process_event(self, event):

        if event.type == pygame_gui.UI_TEXT_BOX_LINK_CLICKED:
            self.ava_uus_leht(event.link_target)

        if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_element == self.input_box):
            print(event.text)

        if (event.type == pygame_gui.UI_BUTTON_PRESSED and
                event.ui_object_id == '#kinematics_window.#home_button'):
            self.ava_uus_leht('index')

    def ava_uus_leht(self, page_link: str):
        self.page_display.kill()
        self.page_display = None
        if page_link in self.pages:
            text = self.pages[page_link]

            self.page_display = UITextBox(text, pygame.Rect((0, self.page_y_start_pos), self.remaining_window_size), manager=self.ui_manager, container=self, parent_element=self)


class GUI:
    def __init__(self, suurus_x, suurus_y):
        self.background = pygame.Surface((suurus_x, suurus_y))
        self.background.fill(pygame.Color('#707070'))

        self.manager = pygame_gui.UIManager((suurus_x, suurus_y), "data/themes/kinematics_theme.json")

        self.kinematics_window = GUIWindow(manager=self.manager)

    @property
    def gui_võtja(self):
        return self.manager
    



    
    