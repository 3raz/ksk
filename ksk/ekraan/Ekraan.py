import pygame

class EkraanMeta(type):
    """
    Üheainsa eksemplari muster ekraani jaoks.
    """
    _eksemplarid = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._eksemplarid:
            cls._eksemplarid[cls] = super(EkraanMeta, cls).__call__(*args, **kwargs)
        return cls._eksemplarid[cls]

class Ekraan(metaclass=EkraanMeta):
    def __init__(self, suurus_x, suurus_y, kaptsioon="Ekraan", tapeedi_värv=(0,0,0)):
        pygame.init()
        self.suurus_x = suurus_x
        self.suurus_y = suurus_y
        self.ekraan = pygame.display.set_mode((self.suurus_x, self.suurus_y), pygame.RESIZABLE)
        
        pygame.display.set_caption(kaptsioon)
        self.tapeedi_värv = tapeedi_värv
        self.objektid = []

    def joonista_objekte(self):
        """
        Joonistab kõike objekte, mis asuvad objekti järjendis.
        """
        for o in self.objektid:
            o.protsess()
        pygame.display.flip()
    
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
        self.objektid.append(objekt)
    
    @property
    def ekraani_võtja(self):
        return self.ekraan
    
    def __del__(self):
        """
        Lõpeta käivitamist korralikult.
        """
        pygame.quit()
    