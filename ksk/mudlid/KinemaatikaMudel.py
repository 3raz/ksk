import math
import pygame
from andmed.Andmed import Andmed

andmed = Andmed().andmed

class KinemaatikaMudel:
    def __init__(self, esialgne_kiirus: float, nurk: float, gravitatsioon: float, dt: float) -> None:
        self.esialgne_kiirus = esialgne_kiirus
        self.nurk = math.radians(nurk)
        self.gravitatsioon = gravitatsioon
        self.dt = dt

        # Esialgne vorm
        self.aeg: float = 0
        self.positsioon_x: float = 0
        self.positsioon_y: float = 0
        self.kiirus_x: float = self.esialgne_kiirus * math.cos(self.nurk)
        self.kiirus_y: float = self.esialgne_kiirus * math.sin(self.nurk)
        
        self.algus_x = 0
        self.algus_y = 0

        self.maal = False

    def __arvuta_positsiooni__(self) -> None:
        """
        Uuenda objekti asukohta kiiruse ja aja järgi
        """
        if self.algus_y - self.positsioon_y > self.algus_y:
            self.maal = True
            return
        self.positsioon_x += self.kiirus_x * self.dt / andmed["scale"]
        self.positsioon_y += self.kiirus_y * self.dt / andmed["scale"]

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
        self.joonista_riivsai()
        if not self.maal:
            self.aeg += self.dt

    
    def lähtesta_seadja(self) -> None:
        """
        Lähtesta
        """
        self.aeg = 0
        self.positsioon_x = 0
        self.positsioon_y = 0
        self.kiirus_x = self.esialgne_kiirus * math.cos(self.nurk)
        self.kiirus_y = self.esialgne_kiirus * math.sin(self.nurk)
        self.maal = False

    def alguspunkti_seadja(self, punkt: tuple) -> None:
        """
        Joonistab objekti offset'iga erineva koordinatsüsteemi töötlemiseks.
        """
        self.algus_x = punkt[0]
        self.algus_y = punkt[1]

    def joonista_riivsai(self, värv=(255,255,255)):
        if andmed["gui_andmed"]["riivsaiaga"]:
            andmed["riivsai"].append((self.positsioon_x, self.positsioon_y, self.algus_y))