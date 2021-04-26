import pygame
from variaveisGlobais import *


class Personagem:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.surf = pygame.Surface((self.largura, self.altura))
        self.spritesIdle = [None, None, None, None]
        self.spritesRun = [None, None, None, None]
        self.sprite = self.spritesIdle[0]
        self.rect = self.surf.get_rect(topleft=(0, 0))
        self.coordant = self.rect.topleft
        self.velocidade = 5
        self.estado = ""
        self.imageIndex = 0

    def move(self):
        pass


class Jogador(Personagem):

    def __init__(self, largura, altura):
        super().__init__(largura, altura)

        self.spritesIdle[0] = pygame.image.load("../Assets/Sprites/jogador/playerIdle0.png")
        self.spritesIdle[1] = pygame.image.load("../Assets/Sprites/jogador/playerIdle1.png")
        self.spritesIdle[2] = pygame.image.load("../Assets/Sprites/jogador/playerIdle2.png")
        self.spritesIdle[3] = pygame.image.load("../Assets/Sprites/jogador/playerIdle3.png")
        self.spritesRun[0] = pygame.image.load("../Assets/Sprites/jogador/playerRun0.png")
        self.spritesRun[1] = pygame.image.load("../Assets/Sprites/jogador/playerRun1.png")
        self.spritesRun[2] = pygame.image.load("../Assets/Sprites/jogador/playerRun2.png")
        self.spritesRun[3] = pygame.image.load("../Assets/Sprites/jogador/playerRun3.png")

        self.sprite = pygame.transform.scale(self.spritesIdle[0], [self.largura, self.altura])
        self.surf.blit(self.sprite, self.coordant)
        self.estado = "parado"
        self.vida = 3
        self.stamina = 100

    def move(self, direcao, direcaoHorizontal, direcaoVertical):
        self.coordant = self.rect.topleft
        if direcaoVertical == "cima":
            if self.rect.top > 0:
                self.rect.move_ip(0, -self.velocidade)
        elif direcaoVertical == "baixo":
            if self.rect.bottom < 600:
                self.rect.move_ip(0, self.velocidade)

        if direcaoHorizontal == "direita":
            if self.rect.right < 800:
                self.rect.move_ip(self.velocidade, 0)
        elif direcaoHorizontal == "esquerda":
            if self.rect.left > 0:
                self.rect.move_ip(-self.velocidade, 0)

        if direcao == "cima" or direcao == "baixo" or direcao == "direita" or direcao == "esquerda":
            self.estado = "andando"
        else:
            self.estado = "parado"
    
    def muda_posicao(self, x, y):
        self.rect = self.surf.get_rect(top_left=(x, y))
    
    def resgata_posicao(self):
        self.rect = self.surf.get_rect(topleft=self.coordant)


class Inimigo(Personagem):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
        self.spritesIdle[0] = pygame.image.load("../Assets/Sprites/monstro/monsterIdle0.png")
        self.sprite = pygame.transform.scale(self.spritesIdle[0], [largura, altura])
        self.surf.blit(self.sprite, self.coordant)
        self.estado = "caminho"
        self.raio_de_visao = 160 #pixels
        self.angulo_de_visao = 60 #graus

    def raio_de_visao_setter(self, raio_de_visao):
        self.raio_de_visao = raio_de_visao

    def angulo_de_visao_setter(self, angulo_de_visao):
        self.angulo_de_visao = angulo_de_visao

    def estado_setter(self, estado):
        self.estado = estado

    def move(self, x, y):
        self.coordant = self.rect.topleft
        self.rect.move_ip(x, y)
        if (self.rect.left < 0) or (self.rect.right > tamanhoTela[0]) or (self.rect.top < 0) or (self.rect.bottom > tamanhoTela[1]):
            self.resgata_posicao()

    def define_posicao(self, ponto):
        self.rect.center = ponto

    def velocidade_setter(self, velocidade):
        self.velocidade = velocidade

    def resgata_posicao(self):
        self.rect.topleft = self.coordant


jogador = Jogador(32, 40)
inimigo = Inimigo(64, 72)
inimigo.define_posicao((100, 250))
