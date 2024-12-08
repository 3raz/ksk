from mudlid.Sfäär import Sfäär
from mudlid.Ruut import Ruut

class Tegeleja:
    def __init__(self, ekraan):
        self.ekraan = ekraan

    def serialiseerija(self, andmed: dict) -> object:
        tüüp = andmed["tüüp"]

        if tüüp == "Sfäär":
            return Sfäär(self.ekraan.ekraan, andmed["esialgne_kiirus"], andmed["nurk"], gravitatsioon=andmed["gravitatsioon"], dt=andmed["dt"], suurus=andmed["suurus"], värv=andmed["värv"])

        elif tüüp == "Ruut":
            return Ruut(self.ekraan.ekraan, andmed["esialgne_kiirus"], andmed["nurk"], gravitatsioon=andmed["gravitatsioon"], dt=andmed["dt"], suurus=andmed["suurus"], värv=andmed["värv"])
        
        else:
            return Sfäär(self.ekraan.ekraan, andmed["esialgne_kiirus"], andmed["nurk"], gravitatsioon=andmed["gravitatsioon"], dt=andmed["dt"], suurus=andmed["suurus"], värv=andmed["värv"])