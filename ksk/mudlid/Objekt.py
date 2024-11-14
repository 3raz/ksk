from mudlid.KinemaatikaMudel import KinemaatikaMudel

from abc import abstractmethod

class Objekt(KinemaatikaMudel):
    def __init__(self, ekraan, esialgne_kiirus, nurk, gravitatsioon=9.8, dt=0.001, suurus=10, värv=(255,0,0)) -> None:
        super().__init__(esialgne_kiirus, nurk, gravitatsioon=gravitatsioon, dt=dt)
        self.suurus = suurus
        self.ekraan = ekraan
        self.värv = värv
        
    @abstractmethod
    def _joonista_(self) -> None:
        """
        Kaitstud funktsioon joonistab objekti ekraanile. Lapse klass peab määrama.
        """
        pass
    
    def __uuenda__(self) -> None:
        """
        Privaatfunktsioon uuenda objektiandmeid lapsevanema klassi kaudu.
        """
        super().uuenda()
    
    def protsess(self) -> None:
        self._joonista_()
        self.__uuenda__()