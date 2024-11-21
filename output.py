
        esialgne_kiirus_left = self.margin_horizontal*1
        esialgne_kiirus_width = 50+self.margin_horizontal*6.5
        self.esialgne_kiirus = UITextEntryLine(pygame.Rect((esialgne_kiirus_left, self.margin_vertical*15), (esialgne_kiirus_width, 25)), self.ui_manager, container=self)
        if self.esialgne_kiirus.get_text().strip() == '':
            sõne = "Undefined"
        else:
            sõne = self.esialgne_kiirus.get_text()
        self.esialgne_kiirus_sild = UILabel(pygame.Rect((esialgne_kiirus_left, 0), (esialgne_kiirus_width, 25)), "esialgne_kiirus: "+sõne, self.ui_manager, container=self)
            


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
            

