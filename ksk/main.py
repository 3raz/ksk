import pygame, sys
from objektid.Sfäär import Sfäär
from objektid.Ruut import Ruut
from graafikud.Ekraan import Ekraan


ekraan = Ekraan(640, 480)


o = Sfäär(ekraan.ekraani_võtja,150,70, dt=0.001, suurus=10, värv=(255,255,255))
o.alguspunkti_seadja((0, 480))

p = Sfäär(ekraan.ekraani_võtja,150,70,gravitatsioon=8.87, dt=0.001, suurus=10, värv=(255,255,255))
p.alguspunkti_seadja((0, 480))

q = Ruut(ekraan.ekraani_võtja,100,70, dt=0.001, suurus=30, värv=(255,255,255))
q.alguspunkti_seadja((0, 480))

ekraan.lisa_objekti(o)
ekraan.lisa_objekti(p)
ekraan.lisa_objekti(q)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            del ekraan
            sys.exit()
    
    ekraan.puhasta()
    ekraan.joonista_objekte()

    