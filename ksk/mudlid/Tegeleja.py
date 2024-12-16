from mudlid.Sfäär import Sfäär
from mudlid.Ruut import Ruut
from mudlid.SfäärÕhutakistusega import SfäärÕhutakistusega
from mudlid.Kuul import Kuul

class Tegeleja:
    """
    vajalik lisa klass, muidu ei saaks funktsioon serialiseerija jadaga erinevates kohtades.
    """
    def __init__(self, ekraan):
        self.ekraan = ekraan

    def serialiseerija(self, sõnastik: dict) -> object:
        try:
            tüüp = sõnastik["tüüp"]
        except TypeError:
            return None

        if tüüp == "Sfäär":
            return Sfäär(self.ekraan.ekraan, sõnastik["esialgne_kiirus"], sõnastik["nurk"], gravitatsioon=sõnastik["gravitatsioon"], dt=sõnastik["dt"], suurus=sõnastik["suurus"], värv=sõnastik["värv"])
        elif tüüp == "Ruut":
            return Ruut(self.ekraan.ekraan, sõnastik["esialgne_kiirus"], sõnastik["nurk"], gravitatsioon=sõnastik["gravitatsioon"], dt=sõnastik["dt"], suurus=sõnastik["suurus"], värv=sõnastik["värv"])
        elif tüüp == "Sfäär Õhutakistusega":
            return SfäärÕhutakistusega(self.ekraan.ekraan, sõnastik["esialgne_kiirus"], sõnastik["nurk"], gravitatsioon=sõnastik["gravitatsioon"], dt=sõnastik["dt"], suurus=sõnastik["suurus"], värv=sõnastik["värv"], raskus=sõnastik["raskus"], tõmbekoefitsient=sõnastik["tõmbekoefitsient"], õhu_tihedus=sõnastik["õhu_tihedus"])
        elif tüüp == "Kuul":
            return Kuul(self.ekraan.ekraan, sõnastik["esialgne_kiirus"], sõnastik["nurk"], gravitatsioon=sõnastik["gravitatsioon"], dt=sõnastik["dt"], suurus=sõnastik["suurus"], värv=sõnastik["värv"], raskus=sõnastik["raskus"], tõmbekoefitsient=sõnastik["tõmbekoefitsient"], õhu_tihedus=sõnastik["õhu_tihedus"])
        else:
            return Sfäär(self.ekraan.ekraan, sõnastik["esialgne_kiirus"], sõnastik["nurk"], gravitatsioon=sõnastik["gravitatsioon"], dt=sõnastik["dt"], suurus=sõnastik["suurus"], värv=sõnastik["värv"])