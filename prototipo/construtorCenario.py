import pygame
from variaveisGlobais import *

class ConstrutorCenario:
    def __init__(self):
        self.chao = []
        self.chaoGroup = pygame.sprite.Group()
        self.chaoPadrao = pygame.image.load("../Assets/Sprites/cenario/chao.png")

    def construirChao(self, x: float, y: float, size: int, sprite, larg=32, alt=32):
        for i in range(size):
            for ii in range(size):
                self.chao.append(Parede(x+(ii*larg), y+(i*alt), sprite, larg, alt, self.chaoGroup))

    def drawGroups(self):
        self.chaoGroup.draw(tela)

    def updateGroups(self):
        self.chaoGroup.update()


class Parede(pygame.sprite.Sprite):

    def __init__(self, x: float, y: float, sprite, larg=32, alt=32, *groups):
        super().__init__(*groups)
        self.largura = larg
        self.altura = alt
        self.surf = pygame.Surface((self.largura, self.altura))
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.image = pygame.transform.scale(sprite, [self.largura, self.altura])


construtorCenario = ConstrutorCenario()


