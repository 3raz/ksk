import math

class KinemaatikaMudel:
    def __init__(self, esialgne_kiirus: float, nurk: float, gravitatsioon: float = 9.8, dt: float = 0.001) -> None:
        self.esialgne_kiirus = esialgne_kiirus
        self.nurk = math.radians(nurk)
        self.gravitatsioon = gravitatsioon
        self.dt = dt

        self.aeg: float = 0
        self.positsioon_x: float = 0
        self.positsioon_y: float = 0
        self.kiirus_x: float = self.esialgne_kiirus * math.cos(self.nurk)
        self.kiirus_y: float = self.esialgne_kiirus * math.sin(self.nurk)
        
        self.algus_x = 0
        self.algus_y = 0

    def __arvuta_positsiooni__(self) -> None:
        """
        Uuenda objekti asukohta kiiruse ja aja järgi
        """
        if self.algus_y - self.positsioon_y > self.algus_y:
            del self
            return
        self.positsioon_x = self.kiirus_x * self.aeg
        self.positsioon_y = (self.kiirus_y * self.aeg) - (0.5 * self.gravitatsioon * self.aeg ** 2)

    def __arvuta_kiiruse__(self) -> None:
        """
        Uuenda objekti y-kiirust gravitatsiooni alusel
        """
        self.kiirus_y -= self.gravitatsioon * self.dt

    def uuenda(self) -> None:
        """
        Uuenda objekti kõiki aspekte
        """
        self.__arvuta_positsiooni__()
        self.__arvuta_kiiruse__()
        self.aeg += self.dt

    
    def lähtesta_seadja(self, esialgne_kiirus: float, nurk: float) -> None:
        """
        Lähtesta
        """
        self.esialgne_kiirus = esialgne_kiirus
        self.nurk = math.radians(nurk)
        self.aeg = 0
        self.positsioon_x = 0
        self.positsioon_y = 0
        self.kiirus_x = self.esialgne_kiirus * math.cos(self.nurk)
        self.kiirus_y = self.esialgne_kiirus * math.sin(self.nurk)

    def alguspunkti_seadja(self, punkt: tuple) -> None:
        self.algus_x = punkt[0]
        self.algus_y = punkt[1]

    @property
    def objekti_andmed_võtja(self) -> dict:
        """
        Tagastab objekti andmed. Seda kutsutakse simulatsiooni 
        lõpus, et näidata kasutajale kulunud aega ja läbitud vahemaad.
        """
        return {
            "positsioon": (self.positsioon_x, self.positsioon_y),
            "kiirus": (self.kiirus_x, self.kiirus_y),
            "aeg": self.aeg
        }