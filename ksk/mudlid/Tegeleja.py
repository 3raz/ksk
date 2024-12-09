from mudlid.Sfäär import Sfäär
from mudlid.Ruut import Ruut

class Tegeleja:
    """
    vajalik lisa klass, muidu ei saaks funktsioon serialiseerija jadaga erinevates kohtades.
    """
    def __init__(self, ekraan):
        self.ekraan = ekraan

    def serialiseerija(self, andmed: dict) -> object:
        try:
            tüüp = andmed["tüüp"]
        except TypeError:
            return None

        if tüüp == "Sfäär":
            return Sfäär(self.ekraan.ekraan, andmed["esialgne_kiirus"], andmed["nurk"], gravitatsioon=andmed["gravitatsioon"], dt=andmed["dt"], suurus=andmed["suurus"], värv=andmed["värv"])

        elif tüüp == "Ruut":
            return Ruut(self.ekraan.ekraan, andmed["esialgne_kiirus"], andmed["nurk"], gravitatsioon=andmed["gravitatsioon"], dt=andmed["dt"], suurus=andmed["suurus"], värv=andmed["värv"])
        
        else:
            return Sfäär(self.ekraan.ekraan, andmed["esialgne_kiirus"], andmed["nurk"], gravitatsioon=andmed["gravitatsioon"], dt=andmed["dt"], suurus=andmed["suurus"], värv=andmed["värv"])