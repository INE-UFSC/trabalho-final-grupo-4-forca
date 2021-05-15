from prototipo.personagens import *
from prototipo.controladorInimigo import *
import math


class Colisao:

    def __init__(self):
        self.x = []  # X dos objetos.
        self.y = []  # Y dos objetos.
        self.objeto_rect = []  # Hitbox dos objetos.
        self.objeto_sprites = []  # Sprites dos objetos.
        self.orientacao = []  # Orientação dos objetos.
        self.ids = []  # Identificações dos objetos.
        self.cenas = []  # Cena na qual o objeto será construido.

        self.temMonstro = True
        self.construir_cenario()

    def draw(self):
        pass

    def construir_cenario(self):
        pass

    def construir_objeto(self, sprite, x, y, cena, quantidade=1, orientacao="horizontal", distancia=0, identificacao="", adicionalY=0):
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
                self.cenas.append(cena)
                self.x.append(x + (i * distancia))
                self.y.append(y)
                self.objeto_rect.append(sprite.get_rect(topleft=(self.x[-1], self.y[-1] + adicionalY)))
        elif orientacao == "vertical":
            for i in range(quantidade):
                self.orientacao.append(orientacao)
                self.objeto_sprites.append(sprite)
                self.ids.append(identificacao)
                self.cenas.append(cena)
                self.x.append(x)
                self.y.append(y + (i * distancia))
                self.objeto_rect.append(sprite.get_rect(topleft=(self.x[-1], self.y[-1] + adicionalY)))

    def destruir_objeto(self, identificacao: str):
        for i, identidade in enumerate(self.ids):
            if identidade == identificacao:
                self.x.pop(i)
                self.y.pop(i)
                self.objeto_rect.pop(i)
                self.objeto_sprites.pop(i)
                self.orientacao.pop(i)
                self.cenas.pop(i)
                self.ids.pop(i)
                self.destruir_objeto(identificacao)

    def desenhar_objetos(self, cena):
        for i, cenaAtual in enumerate(self.cenas):
            if cenaAtual == cena:
                glob.tela.blit(self.objeto_sprites[i], (self.x[i], self.y[i]))

    def distancia(self, obj, x, y):
        return math.hypot(x - obj.rect.x, y - obj.rect.y)

    def get_colisao_jogador(self, cena):
        colisoes_jogador = []
        for i, cenaAtual in enumerate(self.cenas):
            if cenaAtual == cena:
                colisoes_jogador.append(self.objeto_rect[i])
        if self.temMonstro:
            colisoes_jogador.append(inimigo.rect)
        return colisoes_jogador

    def get_colisao_monstro(self, cena):
        colisoes_monstro = []
        for i, cenaAtual in enumerate(self.cenas):
            if cenaAtual == cena:
                colisoes_monstro.append(self.objeto_rect[i])
        return colisoes_monstro

    def colisao_monstro(self):
        controlador.movimenta()
        for retangulo in self.objeto_rect:
            if inimigo.rect.colliderect(retangulo):
                inimigo.resgata_posicao()
        controlador.movimenta()
        for retangulo in self.objeto_rect:
            if inimigo.rect.colliderect(retangulo):
                inimigo.resgata_posicao()

        if inimigo.rect.colliderect(jogador.rect):
            inimigo.resgata_posicao()
