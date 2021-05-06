from prototipo.cenas.cena import Cena
from prototipo.variaveisGlobais import glob
from prototipo.cenas.colisao import Colisao
from prototipo.personagens import *
import pygame


class SpritesPorao:
    def __init__(self):
        self.fundo = pygame.image.load("../Assets/Sprites/cenario/chaoGrande.png")


spritesPorao = SpritesPorao()


class Porao(Cena):

    def __init__(self):
        super().__init__()
        self.cenaJogavel = True

    def iniciar(self):
        print("iniciou")
        jogador.rect.topleft = (50, 550)
        self.delay = 10
        self.iniciou = True

    def eventos(self):
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, colisao.get_colisao_jogador())

        if self.delay > 0:
            self.delay -= 1

        if self.tecla == "p":
            return "menuEmJogo"
        elif self.tecla == "i":
            return "inventario"
        elif self.tecla == "e":
            if colisao.distancia(jogador, 50, 550) < 50 and self.delay <= 0:
                self.iniciou = False
                return "saguao"

    def atualizar(self):
        glob.tela.blit(spritesPorao.fundo, (0, 0))
        colisao.desenhar_objetos()
        jogadorGroup.draw(glob.tela)
        jogadorGroup.update()


class ColisaoPorao(Colisao):

    def __init__(self):
        super().__init__()
        self.temMonstro = False

    def construir_cenario(self):
        pass


colisao = ColisaoPorao()
