import pygame
import itens
from variaveisGlobais import *


class Jogador:

    def __init__(self, x, y):
        self.surf = pygame.Surface((60, 100))
        self.image = pygame.image.load("..\Assets\jogador\jogador.png")
        self.image = pygame.transform.scale(self.image, [60, 100])

        self.rect = self.surf.get_rect(topleft=(x, y))
        self.coordant = self.rect.topleft
        self.surf.blit(self.image, self.coordant)
        self.velocidade = 5
        self.vida = 3
        self.stamina = 100

        self.inventario = [None]*20
        self.inventario[0] = itens.chave
        self.inventario[18] = itens.chave

    def move(self, direcao):
        self.coordant = self.rect.topleft
        if direcao == "cima":
            if self.rect.top > 0:
                self.rect.move_ip(0, -self.velocidade)
        elif direcao == "baixo":
            if self.rect.bottom < 600:
                self.rect.move_ip(0, self.velocidade)
        elif direcao == "direita":
            if self.rect.right < 800:
                self.rect.move_ip(self.velocidade, 0)
        elif direcao == "esquerda":
            if self.rect.left > 0:
                self.rect.move_ip(-self.velocidade, 0)
    
    def muda_posicao(self, x, y):
        self.rect = self.surf.get_rect(top_left=(x, y))
    
    def resgata_posicao(self):
        self.rect = self.surf.get_rect(topleft=self.coordant)

    def aplica_efeito(self, index : int):
        pass

    def remove_item(self, index : int):
        self.inventario[index] = None
    
class Inimigo():
    def __init__(self):
        self.surf = pygame.Surface((20,60))
        self.rect = self.surf.get_rect(topleft = (0,0))
        self.surf.fill((255,0,0))
        self.velocidade = 5
        self.estado = "caminho"
        self.raio_de_visao = 160 #pixels
        self.angulo_de_visao = 60 #graus
        self.coordant = self.rect.topleft
        

    
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

jogador = Jogador(0,0)
inimigo = Inimigo()
inimigo.define_posicao((100, 250))
