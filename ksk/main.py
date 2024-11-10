import pygame, sys
from objektid.Sfäär import Sfäär
from objektid.Ruut import Ruut
from graafikud.Ekraan import Ekraan


ekraan = Ekraan(640, 480)




r = Sfäär(ekraan.ekraani_võtja,150,69, suurus=5, värv=(255,0,0))
r.alguspunkti_seadja((0, 480))

p = Sfäär(ekraan.ekraani_võtja,150,70,gravitatsioon=8.87, suurus=10, värv=(255,255,255))
p.alguspunkti_seadja((0, 480))

q = Ruut(ekraan.ekraani_võtja,100,70, suurus=30, värv=(255,255,255))
q.alguspunkti_seadja((0, 480))

for i in range(15,85):
    o = Sfäär(ekraan.ekraani_võtja,150,i, suurus=10, värv=(i,255,255))
    o.alguspunkti_seadja((0, 480))
    ekraan.lisa_objekti(o)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            del ekraan
            sys.exit()
    
    ekraan.puhasta()
    ekraan.joonista_objekte()

    