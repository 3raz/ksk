import pygame
from andmed.Andmed import Andmed
from mudlid.Objekt import Objekt

andmed = Andmed().andmed

class Ekraan:
    """
    See klass rakendab ainus eksemplari disainimustrit, selle pärast on ainult võimalik üks ekraan olla.
    """
    _eksemplar = None

    def __new__(cls, *args, **kwargs):
        """
        Ainus eksemplari disainimustri abifunktsioon.
        """
        if cls._eksemplar is None:
            cls._eksemplar = super(Ekraan, cls).__new__(cls)
            cls._eksemplar._initialized = False
        return cls._eksemplar

    def __init__(self, kaptsioon="Ekraan", tapeedi_värv=(0, 0, 0)):
        if not self._initialized:
            pygame.init()
            self.suurus_x, self.suurus_y = andmed["resolution"]
            self.tapeedi_värv = tapeedi_värv
            self.ekraan = pygame.display.set_mode((self.suurus_x, self.suurus_y), pygame.RESIZABLE)
            pygame.display.set_caption(kaptsioon)
            self.objektid = []
            self._initialized = True

    def värskenda_resolution(self) -> None:
        """
        Lisafunktsioon, et resolution kindlasti värskendaks.
        """
        self.suurus_x, self.suurus_y = andmed["resolution"]

    def joonista_objekte(self) -> None:
        """
        Joonistab kõike objekte, mis asuvad objekti järjendis.
        """
        for o in self.objektid:
            o.protsess()
        pygame.display.update()
        
    def puhasta(self) -> None:
        """
        Täitab tapeedi värviga.
        """
        self.ekraan.fill(self.tapeedi_värv)
    
    def kustuta_objekte(self) -> None:
        """
        Kustutab kõike objekte
        """
        self.objektid = []
    
    def värvi_seadja(self, värv: tuple) -> None:
        """
        Muutub tapeedi värvi.
        """
        self.tapeedi_värv = värv
        
    def lisa_objekti(self, objekt: Objekt) -> None:
        """
        Lisa objekti järjendisse. Funktsioon joonista_objekte selles klassis siis joonistab kõike, mis on järjendis.
        """
        objekt.alguspunkti_seadja((self.suurus_x, self.suurus_y-self.suurus_y/andmed["gui_pikkus"]))
        self.objektid.append(objekt)
    
    @property
    def ekraani_võtja(self) -> pygame.Surface:
        """
        Annab ekraani pygame'i osa tagasi, millega saaks uusi pygame'i ja ksk programmi objekte luua.
        Returns:
            pygame.Surface
        """
        return self.ekraan
    
    def __del__(self):
        """
        Lõpeta käivitamist korralikult.
        """
        pygame.quit()