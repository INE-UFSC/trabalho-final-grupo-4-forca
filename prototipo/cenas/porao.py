from prototipo.cenas.cena import Cena
from prototipo.variaveisGlobais import glob
from prototipo.cenas.colisao import Colisao
from prototipo.cenas.sprites import SpritesCena
from prototipo.personagens import *
import pygame


class SpritesPorao(SpritesCena):
    def __init__(self):
        super().__init__()


spritesPorao = SpritesPorao()


class Porao(Cena):

    def __init__(self):
        super().__init__()
        self.cenaJogavel = True

    def iniciar(self):
        print("iniciou porao")
        if glob.cenaAtual == "saguao":
            jogador.rect.topleft = (50, 550)
        glob.cenaAtual = "porao"
        colisao.construir_cenario()
        self.delay = 10
        self.iniciou = True

    def eventos(self):
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, colisao.get_colisao_jogador("porao"))

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
            elif colisao.distancia(jogador, 780, 0) < 50 and self.delay <= 0:
                self.iniciou = False
                return "porao2"

    def atualizar(self):
        glob.tela.blit(spritesPorao.fundo, (0, 0))
        colisao.desenhar_objetos("porao")
        jogadorGroup.draw(glob.tela)
        jogadorGroup.update()


class Porao2(Porao):

    def __init__(self):
        super().__init__()

    def iniciar(self):
        print("iniciou porao 2")
        jogador.rect.topleft = (760, 560)
        glob.cenaAtual = "porao2"
        colisao.construir_cenario()
        self.delay = 10
        self.iniciou = True

    def eventos(self):
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, colisao.get_colisao_jogador("porao2"))

        if self.delay > 0:
            self.delay -= 1

        if self.tecla == "p":
            return "menuEmJogo"
        elif self.tecla == "i":
            return "inventario"
        elif self.tecla == "e":
            if colisao.distancia(jogador, 760, 560) < 50 and self.delay <= 0:
                self.iniciou = False
                return "porao"

    def atualizar(self):
        glob.tela.blit(spritesPorao.fundo, (0, 0))
        colisao.desenhar_objetos("porao2")
        jogadorGroup.draw(glob.tela)
        jogadorGroup.update()


class ColisaoPorao(Colisao):

    def __init__(self):
        super().__init__()
        self.temMonstro = False

    def construir_cenario(self):
        self.construir_objeto(spritesPorao.parede_sprite_h, 300, 300, "porao")


colisao = ColisaoPorao()
