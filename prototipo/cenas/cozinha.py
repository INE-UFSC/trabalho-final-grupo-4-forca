from prototipo.cenas.cena import Cena
from prototipo.variaveisGlobais import glob
from prototipo.cenas.colisao import Colisao
from prototipo.cenas.sprites import SpritesCena
from prototipo.personagens import *
import pygame


class SpritesCozinha(SpritesCena):
    def __init__(self):
        super().__init__()
        self.sprite_mesa = pygame.image.load("../Assets/Sprites/cenario/mesa.png") 
        self.sprite_cadeira_direita = pygame.image.load("../Assets/Sprites/cenario/cadeiradireita.png")
        self.sprite_cadeira_esquerda = pygame.image.load("../Assets/Sprites/cenario/cadeiraesquerda.png")
        self.sprite_cadeira_cima = pygame.image.load("../Assets/Sprites/cenario/cadeiracima.png")
        self.sprite_cadeira_baixo = pygame.image.load("../Assets/Sprites/cenario/cadeirabaixo.png")
cozinhasprites = SpritesCozinha()

class ColisaoCozinha(Colisao):
    def __init__(self):
        super().__init__()
    
    def construir_cenario(self):
        self.construir_objeto(cozinhasprites.sprite_cadeira_cima, 380, 205, "cozinha", 1, identificacao = "cadeiracima")
        self.construir_objeto(cozinhasprites.sprite_cadeira_esquerda, 300, 250, "cozinha", 1, identificacao = "cadeiraesquerda")
        self.construir_objeto(cozinhasprites.sprite_cadeira_cima, 460, 250, "cozinha", 1, identificacao = "cadeiradireita")
        self.construir_objeto(cozinhasprites.sprite_mesa, 340, 250, "cozinha", 1, identificacao = "mesa")

colisao = ColisaoCozinha()
class Cozinha(Cena):

    def __init__(self):
        super().__init__()
        self.teclaHorizontal = ""
        self.teclaVertical = ""
        self.cenaJogavel = True
        colisao.construir_cenario()
        self.puzzle = ["esquerda", "cima", "cima"]
    def iniciar(self):
        glob.cenaAtual = "cozinha"
        if glob.cenaAtual == "cozinha":
            jogador.rect.topleft = (40, 40)

        self.delay = 10
        self.iniciou = True
    
    def muda_puzzle(self, cadeira):
        if cadeira == "esquerda":
            self.puzzle[0] = self.acha_posicao(self.puzzle[0])
            colisao.destruir_objeto("cadeiraesquerda")
            colisao.destruir_objeto("mesa")
            self.constroi_objeto("esquerda")
            colisao.construir_objeto(cozinhasprites.sprite_mesa, 340, 250, "cozinha", 1, identificacao = "mesa")
        elif cadeira == "cima":
            self.puzzle[1] = self.acha_posicao(self.puzzle[1])
            colisao.destruir_objeto("cadeiracima")
            colisao.destruir_objeto("mesa")
            self.constroi_objeto("cima")
            colisao.construir_objeto(cozinhasprites.sprite_mesa, 340, 250, "cozinha", 1, identificacao = "mesa")
        elif cadeira == "direita":
            self.puzzle[2] = self.acha_posicao(self.puzzle[2])
            colisao.destruir_objeto("cadeiradireita")
            colisao.destruir_objeto("mesa")
            self.constroi_objeto("direita")
            colisao.construir_objeto(cozinhasprites.sprite_mesa, 340, 250, "cozinha", 1, identificacao = "mesa")
            
    
    def constroi_objeto(self, cadeira):
        if cadeira == "esquerda":
            if self.puzzle[0] == "esquerda":
                colisao.construir_objeto(cozinhasprites.sprite_cadeira_esquerda, 300, 250, "cozinha", 1, identificacao = "cadeiraesquerda")
            elif self.puzzle[0] == "cima":
                colisao.construir_objeto(cozinhasprites.sprite_cadeira_cima, 300, 250, "cozinha", 1, identificacao = "cadeiraesquerda")
            elif self.puzzle[0] == "direita":
                colisao.construir_objeto(cozinhasprites.sprite_cadeira_direita, 300, 250, "cozinha", 1, identificacao = "cadeiraesquerda")
            elif self.puzzle[0] == "baixo":
                colisao.construir_objeto(cozinhasprites.sprite_cadeira_baixo, 300, 250, "cozinha", 1, identificacao = "cadeiraesquerda")
        
        elif cadeira == "cima":
            if self.puzzle[1] == "esquerda":
                colisao.construir_objeto(cozinhasprites.sprite_cadeira_esquerda, 380, 205, "cozinha", 1, identificacao = "cadeiracima")
            elif self.puzzle[1] == "cima":
                colisao.construir_objeto(cozinhasprites.sprite_cadeira_cima, 380, 205, "cozinha", 1, identificacao = "cadeiracima")
            elif self.puzzle[1] == "direita":
                colisao.construir_objeto(cozinhasprites.sprite_cadeira_direita, 380, 205, "cozinha", 1, identificacao = "cadeiracima")
            elif self.puzzle[1] == "baixo":
                colisao.construir_objeto(cozinhasprites.sprite_cadeira_baixo, 380, 205, "cozinha", 1, identificacao = "cadeiracima")
        elif cadeira == "direita":
            if self.puzzle[2] == "esquerda":
                colisao.construir_objeto(cozinhasprites.sprite_cadeira_esquerda, 460, 250, "cozinha", 1, identificacao = "cadeiradireita")
            elif self.puzzle[2] == "cima":
                colisao.construir_objeto(cozinhasprites.sprite_cadeira_cima, 460, 250, "cozinha", 1, identificacao = "cadeiradireita")
            elif self.puzzle[2] == "direita":
                colisao.construir_objeto(cozinhasprites.sprite_cadeira_direita, 460, 250, "cozinha", 1, identificacao = "cadeiradireita")
            elif self.puzzle[2] == "baixo":
                colisao.construir_objeto(cozinhasprites.sprite_cadeira_baixo, 460, 250, "cozinha", 1, identificacao = "cadeiradireita")
    
    def acha_posicao(self, posicao):
        if posicao == "esquerda":
            return "cima"
        elif posicao == "cima":
            return "direita"
        elif posicao == "direita":
            return "baixo"
        elif posicao == "baixo":
            return "esquerda"


    def eventos(self):  # Captura os eventos do teclado e do cenário.
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, colisao.get_colisao_jogador("cozinha"))
        #controlador.movimenta()
        #colisao.colisao_monstro()

        if self.delay > 0:
            self.delay -= 1

        if self.tecla == "i":
            return "inventario"
        elif self.tecla == "e":
            if colisao.distancia(jogador, 400, 190) < 40 and self.delay <= 0:
                self.muda_puzzle("cima")
                self.delay = 20
            elif colisao.distancia(jogador, 300, 260) < 40 and self.delay <= 0:
                self.muda_puzzle("esquerda")
                self.delay = 20
            elif colisao.distancia(jogador, 500, 260) < 40 and self.delay <= 0:
                self.delay = 20
                self.muda_puzzle("direita")
            
            
    def atualizar(self):  # Atualiza os sprites da cena.
        glob.tela.blit(cozinhasprites.fundo, (0, 0))
        colisao.desenhar_objetos("cozinha")
        jogadorGroup.draw(glob.tela)
        jogadorGroup.update()
