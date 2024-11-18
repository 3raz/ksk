import pygame
from gui.Gui import GUI

class Ekraan:
    _eksemplar = None

    def __new__(cls, *args, **kwargs):
        if cls._eksemplar is None:
            cls._eksemplar = super(Ekraan, cls).__new__(cls)
            cls._eksemplar._initialized = False
        return cls._eksemplar

    def __init__(self, suurus_x, suurus_y, kaptsioon="Ekraan", tapeedi_värv=(0, 0, 0)):
        if not self._initialized:
            pygame.init()
            self.suurus_x = suurus_x
            self.suurus_y = suurus_y
            self.tapeedi_värv = tapeedi_värv
            self.ekraan = pygame.display.set_mode((self.suurus_x, self.suurus_y), pygame.RESIZABLE)
            pygame.display.set_caption(kaptsioon)
            self.objektid = []
            self._initialized = True

    def joonista_objekte(self):
        """
        Joonistab kõike objekte, mis asuvad objekti järjendis.
        """
        for o in self.objektid:
            o.protsess()
        pygame.display.update()
    
    def puhasta(self):
        """
        Täitab tapeedi värviga.
        """
        self.ekraan.fill(self.tapeedi_värv)
    
    def värvi_seadja(self, värv):
        self.tapeedi_värv = värv
        
    def lisa_objekti(self, objekt):
        """
        Lisa objekti järjendisse. Funktsioon joonista_objekte selles klassis siis joonistab kõike, mis on järjendis.
        """
        objekt.alguspunkti_seadja((self.suurus_x, self.suurus_y))
        self.objektid.append(objekt)
    
    @property
    def ekraani_võtja(self):
        return self.ekraan
    
    def __del__(self):
        """
        Lõpeta käivitamist korralikult.
        """
        pygame.quit()