import pygame
import pygame_gui
import sys
from gui.Gui import GUIEkraan
from andmed.Andmed import Andmed
from mudlid.Sfäär import Sfäär
from mudlid.SfäärÕhutakistusega import SfäärÕhutakistusega
from mudlid.Tegeleja import Tegeleja
from gui.GuiParser import GuiParser

andmed = Andmed().andmed

class SündmuseJuhataja:
    
    def __init__(self, ekraan, gui):
        self.ekraan = ekraan
        self.gui = gui
        self.gui_parser = GuiParser()
        self.tegeleja = Tegeleja(self.ekraan)

        self.a = Andmed()

    def töötle_sündmustega(self):
        """
        Töötleb pygame'i ja pygame_gui sündmustega
        """
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

            # pygame_gui värskendab ja kustutab kõik andmed. Seega peaks käsitsi salvestama.
            if sündmus.type == pygame_gui.UI_BUTTON_PRESSED or sündmus.type == pygame.VIDEORESIZE:
                o = self.create_object()

                # Jälgib, et objekt on korralikult loonud.
                if o != None:
                    andmed["gui_andmed"]["esialgne_kiirus"] = float(self.gui.kinematics_window.esialgne_kiirus.get_text())
                    andmed["gui_andmed"]["nurk"] = float(self.gui.kinematics_window.nurk.get_text())
                    andmed["gui_andmed"]["gravitatsioon"] = float(self.gui.kinematics_window.gravitatsioon.get_text())
                    andmed["gui_andmed"]["dt"] = float(self.gui.kinematics_window.dt.get_text())
                    andmed["gui_andmed"]["suurus"] = float(self.gui.kinematics_window.suurus.get_text())
                    andmed["gui_andmed"]["värv"] = [int(x) for x in self.gui.kinematics_window.värv.get_text().strip().split(',')]
                    andmed["gui_andmed"]["raskus"] = float(self.gui.kinematics_window.raskus.get_text())
                    andmed["gui_andmed"]["tõmbetegur"] = float(self.gui.kinematics_window.tõmbetegur.get_text())
                    andmed["gui_andmed"]["õhu_tihedus"] = float(self.gui.kinematics_window.õhu_tihedus.get_text())

            # Määrab muutujat rippmenüü praeguse tekstiga, kui rippmenüü praeguse tekst on muutnud. 
            if sündmus.type == pygame_gui.UI_DROP_DOWN_MENU_CHANGED:
                andmed["cur_object"] = sündmus.text

            button_pressed = False
            if sündmus.type == pygame_gui.UI_BUTTON_PRESSED:
                button_pressed = True

            # Kustutab vana GUI ja ekraani ära ja initsialiseerib uued korraliku suurustega
            if sündmus.type == pygame.VIDEORESIZE or (button_pressed and sündmus.ui_element == self.gui.kinematics_window.salvesta):
                try:
                    andmed["resolution"] = [sündmus.w, sündmus.h]
                except AttributeError:
                    sündmus.w, sündmus.h = andmed["resolution"]
                self.a.salvesta_faili()
                vana_ekraan = self.ekraan.ekraan
                vana_gui = self.gui.manager
                self.ekraan.ekraan = pygame.display.set_mode((sündmus.w, sündmus.h), pygame.RESIZABLE)

                self.gui.manager = pygame_gui.UIManager((sündmus.w, sündmus.h), 'ksk/andmed/themes/theme.json')
                self.gui.kinematics_window = GUIEkraan(self.gui.manager)
                self.ekraan.ekraan.blit(vana_ekraan, (0,0))
                self.ekraan.värskenda_resolution()

                del vana_ekraan
                del vana_gui
                
                for objekt in self.ekraan.objektid:
                    objekt.alguspunkti_seadja((sündmus.w, sündmus.h-sündmus.h/andmed["gui_pikkus"]))
            
            # Jälgib mis juhtus, kui nupp on vajutatud
            if button_pressed:
                
                # Puhasta ekraan nupp
                if sündmus.ui_element == self.gui.kinematics_window.puhasta:
                    self.ekraan.kustuta_objekte()

                # Objekti lisamise nupp
                if sündmus.ui_element == self.gui.kinematics_window.lisa:
                    o = self.create_object()
                    
                    if o == None:
                        print("Bad info")

                    trigger = False    
                    for _, h1 in andmed["session_objects"].items():
                        if h1 == o.objekti_andmed_võtja:
                            trigger = True

                    if trigger:
                        pass
                    else:
                        pass
                        self.gui.kinematics_window.set_most_recent_object(o)
                        uue_objekti_nimi = self.gui.kinematics_window.approximate_color(o.värv) + " sfäär"
                        while True:
                            for key, _ in andmed["session_objects"].items():
                                if key == uue_objekti_nimi:
                                    try:
                                        uue_objekti_nimi = uue_objekti_nimi[0:-1] + str(int(uue_objekti_nimi[-1])+1)
                                    except ValueError:
                                        uue_objekti_nimi = uue_objekti_nimi + " 1"
                                    continue
                            break
                        andmed["session_objects"][uue_objekti_nimi] = o.objekti_andmed_võtja
                        self.gui.kinematics_window.objekti_menüü.add_options([uue_objekti_nimi])
                    self.ekraan.lisa_objekti(o)

                # Objekti lisamise nupp rippumenüüst
                if sündmus.ui_element == self.gui.kinematics_window.lisa_järjendist:
                    try:
                        self.ekraan.lisa_objekti(self.tegeleja.serialiseerija(andmed["session_objects"][andmed["cur_object"]]))
                    except:
                        pass
                    
                # Lisab kõike järjendist
                if sündmus.ui_element == self.gui.kinematics_window.lisa_kõike:
                    for key, value in andmed["session_objects"].items():
                        try:
                            self.ekraan.lisa_objekti(self.tegeleja.serialiseerija(value))
                        except:
                            pass
                        
                        
                # Kustutab kõike järjendist
                if sündmus.ui_element == self.gui.kinematics_window.kustuta_kõike:
                    for asi in self.gui.kinematics_window.objekti_menüü.options_list:
                        if asi == ('', ''):
                            continue
                        self.gui.kinematics_window.objekti_menüü.remove_options([asi])
                    andmed["session_objects"] = {'': ''}
                    andmed["cur_object"] = ''
                    self.gui.kinematics_window.objekti_menüü.selected_option = ('', '')

                # Vahetab režiimi
                if sündmus.ui_element == self.gui.kinematics_window.režiim:
                    andmed["õhutakistusega"] = not andmed["õhutakistusega"]
                    if andmed["õhutakistusega"]:
                        self.gui.kinematics_window.režiimi_sild.set_text("Õhutakistusega")
                    else:
                        self.gui.kinematics_window.režiimi_sild.set_text("Ilma õhutakistuseta")
            

    def create_object(self) -> object:
        """
        Lisab objekti ekraanile antud andmetega. Saaks ka selle funktsiooni kasutada info kontrollijana.
        """

        # Loeb kõik andmed
        esialgne_kiirus = self.gui_parser.positiivne_number(self.gui.kinematics_window.esialgne_kiirus.get_text())
        nurk = self.gui_parser.nurk(self.gui.kinematics_window.nurk.get_text())
        gravitatsioon = self.gui_parser.number(self.gui.kinematics_window.gravitatsioon.get_text())
        dt = self.gui_parser.number(self.gui.kinematics_window.dt.get_text())
        suurus = self.gui_parser.positiivne_number(self.gui.kinematics_window.suurus.get_text())
        värv = self.gui_parser.värv(self.gui.kinematics_window.värv.get_text())

        üldinfo = [esialgne_kiirus, nurk, gravitatsioon, suurus, värv]

        raskus = self.gui_parser.positiivne_number(self.gui.kinematics_window.raskus.get_text())
        tõmbetegur = self.gui_parser.positiivne_number(self.gui.kinematics_window.tõmbetegur.get_text())
        õhu_tihedus = self.gui_parser.positiivne_number(self.gui.kinematics_window.õhu_tihedus.get_text())

        õhuinfo = [raskus, tõmbetegur, õhu_tihedus]

        # vaikeväärtus
        if dt == None:
            dt = 0.001

        # viga, kui midagi on None
        for asi in üldinfo:
            if asi == None:
                return None

        if not andmed["õhutakistusega"]:
            # Uue objekti on loonud antud andmetega
            o = Sfäär(self.ekraan.ekraan,
                                esialgne_kiirus,
                                nurk, 
                                gravitatsioon=gravitatsioon,
                                dt=dt,
                                suurus=suurus,
                                värv=värv)
            
            return o
        else:
            # viga, kui midagi on None
            for asi in õhuinfo:
                if asi == None:
                    return None
                
            # Uue objekti on loonud antud andmetega
            o = SfäärÕhutakistusega(self.ekraan.ekraan,
                                            esialgne_kiirus,
                                            nurk, 
                                            gravitatsioon=gravitatsioon,
                                            dt=dt,
                                            suurus=suurus,
                                            raskus=raskus,
                                            värv=värv,
                                            tõmbetegur=tõmbetegur,
                                            õhu_tihedus=õhu_tihedus)
            
            return o
            

