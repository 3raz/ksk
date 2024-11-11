from juhatajad.Juhataja import Juhataja
from mudlid.Sfäär import Sfäär

class Main:
    def __init__(self):
        self.juhataja = Juhataja()
    
    def jookse(self):
        self.juhataja.programm()

if __name__ == "__main__":
    main = Main()

    for j in range(100, 500, 10):
        for i in range(0,124, 5):
            o = Sfäär(main.juhataja.ekraan.ekraani_võtja,j,i, dt=main.juhataja.dt, suurus=5, värv=(0,255-2*i,2*i))
            o.alguspunkti_seadja((0, 480))
            main.juhataja.ekraan.lisa_objekti(o)

    main.jookse()