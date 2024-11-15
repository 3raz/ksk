################################################
# Programmeerimine I
# 2024/2025 sügissemester
#
# Projekt
# Teema: Kinemaatika Simulaator
#
#
# Autorid: Zachary A. Davis
#
# Lisakommentaar (nt käivitusjuhend): 
# 1) Käsureaga käivitage käsku pip install -r requirements.txt 
# 2) Käivitage faili main.py (see sama fail)
#
##################################################

from juhatajad.Juhataja import Juhataja
from mudlid.Sfäär import Sfäär

class Main:
    def __init__(self):
        self.juhataja = Juhataja()
    
    def jookse(self):
        self.juhataja.programm()

if __name__ == "__main__":
    """
    PÕHIPROGRAMM KUS OBJEKTID JA VÄRKI SAAKS LISADA
    """
    main = Main()

    # Loob palju objekte ja käskib neid läbi õhu lendama
    for x in range(5):
        for j in range(100, 500, 10):
            for i in range(0,124, 5):
                o = Sfäär(main.juhataja.ekraan.ekraani_võtja,j,i, suurus=5, värv=(0,255-2*i,2*i))
                o.alguspunkti_seadja((0, 480))
                main.juhataja.ekraan.lisa_objekti(o)

    main.jookse()