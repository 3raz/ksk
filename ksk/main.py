import pygame, sys
from mudlid.Sfäär import Sfäär
from mudlid.Ruut import Ruut
from ekraan.Ekraan import Ekraan


ekraan = Ekraan(640, 480)

clock = pygame.time.Clock()

dt = clock.tick(60)

for j in range(100, 500, 10):
    for i in range(0,124, 5):
        o = Sfäär(ekraan.ekraani_võtja,j,i, dt=dt, suurus=1, värv=(0,255-2*i,2*i))
        o.alguspunkti_seadja((0, 480))
        ekraan.lisa_objekti(o)
    
        

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            del ekraan
            sys.exit()
    
    for i in range(len(ekraan.objektid)):
        ekraan.objektid[i].dt = dt/250   
        ekraan.objektid[i].suurus += 0.1     
    
    dt = clock.tick(60)
    ekraan.puhasta()
    ekraan.joonista_objekte()

    