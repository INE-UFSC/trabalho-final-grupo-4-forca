from prototipo.personagens import *
from prototipo.controladorInimigo import *
import math


class Colisao:

    def __init__(self):
        self.parede_sprite_h = pygame.image.load("../Assets/Sprites/cenario/parede_horizontal.png")
        self.parede_sprite_v = pygame.image.load("../Assets/Sprites/cenario/parede_vertical.png")

        self.x = []  # X dos objetos.
        self.y = []  # Y dos objetos.
        self.objeto_rect = []  # Hitbox dos objetos.
        self.objeto_sprites = []  # Sprites dos objetos.
        self.orientacao = []  # Orientação dos objetos.
        self.ids = []  # Identificações dos objetos.

        self.temMonstro = True
        self.construir_cenario()

    def draw(self):
        pass

    def construir_cenario(self):
        pass

    def construir_objeto(self, sprite, x, y, quantidade=1, orientacao="horizontal", distancia=0, identificacao=""):
        if distancia == 0:
            if orientacao == "horizontal":
                distancia = sprite.get_width()
            elif orientacao == "vertical":
                distancia = sprite.get_height()
        if orientacao == "horizontal":
            for i in range(quantidade):
                self.orientacao.append(orientacao)
                self.objeto_sprites.append(sprite)
                self.ids.append(identificacao)
                self.x.append(x + (i * distancia))
                self.y.append(y)
                self.objeto_rect.append(sprite.get_rect(topleft=(self.x[-1], self.y[-1])))
        elif orientacao == "vertical":
            for i in range(quantidade):
                self.orientacao.append(orientacao)
                self.objeto_sprites.append(sprite)
                self.ids.append(identificacao)
                self.x.append(x)
                self.y.append(y + (i * distancia))
                self.objeto_rect.append(sprite.get_rect(topleft=(self.x[-1], self.y[-1])))

    def destruir_objeto(self, identificacao: str):
        for i, identidade in enumerate(self.ids):
            if identidade == identificacao:
                self.x.pop(i)
                self.y.pop(i)
                self.objeto_rect.pop(i)
                self.objeto_sprites.pop(i)
                self.orientacao.pop(i)
                self.ids.pop(i)
                self.destruir_objeto(identificacao)

    def desenhar_objetos(self):
        for i, sprite in enumerate(self.objeto_sprites):
            glob.tela.blit(sprite, (self.x[i], self.y[i]))

    def distancia(self, obj, x, y):
        return math.hypot(x - obj.rect.x, y - obj.rect.y)

    def get_colisao_jogador(self):
        colisoes_jogador = self.objeto_rect.copy()
        if self.temMonstro:
            colisoes_jogador.append(inimigo.rect)
        return colisoes_jogador

    def get_colisao_monstro(self):
        return self.objeto_rect

    def colisao_monstro(self):
        for retangulo in self.objeto_rect:
            if inimigo.rect.colliderect(retangulo):
                inimigo.resgata_posicao()

        if inimigo.movimento_falhou:
            controlador.movimenta_x()
            for retangulo in self.objeto_rect:
                if inimigo.rect.colliderect(retangulo):
                    inimigo.resgata_posicao()
        if inimigo.movimento_falhou:
            controlador.movimenta_y()
            for retangulo in self.objeto_rect:
                if inimigo.rect.colliderect(retangulo):
                    inimigo.resgata_posicao()

        if inimigo.rect.colliderect(jogador.rect):
            inimigo.resgata_posicao()
