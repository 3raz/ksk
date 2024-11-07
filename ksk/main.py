import pygame, sys
from objektid.šabloonid.objekt import Objekt
from graafikud.ekraan import Ekraan


ekraan = Ekraan(640, 480)


o = Objekt(150,70,ekraan.ekraani_võtja,25,dt=0.001)
o.alguspunkti_seadja((0, 480))

ekraan.lisa_objekti(o)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            del ekraan
            sys.exit()
    
    ekraan.puhasta()
    ekraan.joonista_objekte()

    