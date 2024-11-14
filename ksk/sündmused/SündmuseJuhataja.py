import pygame
import sys

class SündmuseJuhataja:
    def __init__(self, ekraan):
        self.ekraan = ekraan

    def töötle_sündmustega(self):
        """Töötle pygame'i sündmustega"""
        for sündmus in pygame.event.get():
            if sündmus.type == pygame.QUIT:
                del self.ekraan
                sys.exit()

            if sündmus.type == pygame.VIDEORESIZE:
                vana_ekraan = self.ekraan.ekraan
                self.ekraan.ekraan = pygame.display.set_mode((sündmus.w, sündmus.h), pygame.RESIZABLE)
                self.ekraan.ekraan.blit(vana_ekraan, (0,0))
                del vana_ekraan
                
                for objekt in self.ekraan.objektid:
                    objekt.alguspunkti_seadja((sündmus.w, sündmus.h))