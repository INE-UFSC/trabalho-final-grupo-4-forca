from prototipo.personagens import *
from prototipo.controladorInimigo import *


class Colisao:

    def __init__(self):
        self.parede_sprite_h = pygame.image.load("../Assets/Sprites/cenario/parede_horizontal.png")
        self.parede_sprite_v = pygame.image.load("../Assets/Sprites/cenario/parede_vertical.png")
        self.x = []
        self.y = []
        self.orientacao = []
        self.parede_rect = []

    def draw(self):
        pass

    def construir_cenario(self):
        pass

    def construir_parede_horizontal(self, x, y, quantidade):
        pass

    def construir_parede_vertical(self, x, y, quantidade):
        pass

    def desenhar_paredes(self):
        pass

    def get_colisao_jogador(self):
        pass

    def get_colisao_monstro(self):
        pass

    def colisao_monstro(self):
        for retangulo in self.parede_rect:
            if inimigo.rect.colliderect(retangulo):
                inimigo.resgata_posicao()

        if inimigo.movimento_falhou:
            controlador.movimenta_x()
            for retangulo in self.parede_rect:
                if inimigo.rect.colliderect(retangulo):
                    inimigo.resgata_posicao()
        if inimigo.movimento_falhou:
            controlador.movimenta_y()
            for retangulo in self.parede_rect:
                if inimigo.rect.colliderect(retangulo):
                    inimigo.resgata_posicao()

        if inimigo.rect.colliderect(jogador.rect):
            inimigo.resgata_posicao()
