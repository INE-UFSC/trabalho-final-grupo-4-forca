from prototipo.personagens import *
from prototipo.controladorInimigo import *


class Colisao:

    def __init__(self):
        self.parede_sprite_h = pygame.image.load("../Assets/Sprites/cenario/parede_horizontal.png")
        self.parede_sprite_v = pygame.image.load("../Assets/Sprites/cenario/parede_vertical.png")
        self.xP = []  # X das paredes.
        self.yP = []  # Y das paredes.

        self.x = []  # X dos objetos.
        self.y = []  # Y dos objetos.
        self.objeto_rect = []
        self.objeto_sprites = []

        self.orientacao = []
        self.parede_rect = []
        self.temMonstro = True
        self.construir_cenario()

    def draw(self):
        pass

    def construir_cenario(self):
        pass

    def construir_parede(self, orientacao, x, y, quantidade):
        for i in range(quantidade):
            self.orientacao.append(orientacao)
            if orientacao == "horizontal":
                self.xP.append(x + (i * 183))
                self.yP.append(y)
                self.parede_rect.append(self.parede_sprite_h.get_rect(topleft=(self.xP[-1], self.yP[-1])))
            elif orientacao == "vertical":
                self.xP.append(x)
                self.yP.append(y + (i * 26))
                self.parede_rect.append(self.parede_sprite_v.get_rect(topleft=(self.xP[-1], self.yP[-1])))

    def desenhar_paredes(self):
        for i, orientacao in enumerate(self.orientacao):
            if orientacao == "horizontal":
                glob.tela.blit(self.parede_sprite_h, (self.xP[i], self.yP[i]))
            elif orientacao == "vertical":
                glob.tela.blit(self.parede_sprite_v, (self.xP[i], self.yP[i]))

    def construir_objeto(self, sprite, x, y):
            self.x.append(x)
            self.y.append(y)
            self.objeto_sprites.append(sprite)
            self.objeto_rect.append(sprite.get_rect(topleft=(self.x[-1], self.y[-1])))

    def desenhar_objetos(self):
        for i, sprite in enumerate(self.objeto_sprites):
            glob.tela.blit(sprite, (self.x[i], self.y[i]))

    def get_colisao_jogador(self):
        colisoes_jogador = self.parede_rect.copy()
        if self.temMonstro:
            colisoes_jogador.append(inimigo.rect)
        return colisoes_jogador + self.objeto_rect

    def get_colisao_monstro(self):
        return self.parede_rect + self.objeto_rect

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
