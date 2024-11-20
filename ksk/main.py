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

class Main:
    def __init__(self):
        self.juhataja = Juhataja()
    
    def jookse(self):
        self.juhataja.programm()

if __name__ == "__main__":
    """
    Põhiprogramm
    """
    main = Main()
    main.jookse()