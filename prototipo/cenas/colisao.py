from prototipo.personagens import *
from prototipo.controladorInimigo import *


class Colisao:

    def __init__(self):
        self.parede_sprite_h = pygame.image.load("../Assets/Sprites/cenario/parede_horizontal.png")
        self.parede_sprite_v = pygame.image.load("../Assets/Sprites/cenario/parede_vertical.png")
        self.x = []  # X dos objetos.
        self.y = []  # Y dos objetos.
        self.objeto_rect = []
        self.objeto_sprites = []

        self.orientacao = []
        self.temMonstro = True
        self.construir_cenario()

    def draw(self):
        pass

    def construir_cenario(self):
        pass

    def construir_objeto(self, sprite, x, y, quantidade=1, orientacao="horizontal", distancia=0):
        if distancia == 0:
            if orientacao == "horizontal":
                distancia = sprite.get_width()
            elif orientacao == "vertical":
                distancia = sprite.get_height()
        if orientacao == "horizontal":
            for i in range(quantidade):
                self.orientacao.append(orientacao)
                self.objeto_sprites.append(sprite)
                self.x.append(x + (i * distancia))
                self.y.append(y)
                self.objeto_rect.append(sprite.get_rect(topleft=(self.x[-1], self.y[-1])))
        elif orientacao == "vertical":
            for i in range(quantidade):
                self.orientacao.append(orientacao)
                self.objeto_sprites.append(sprite)
                self.x.append(x)
                self.y.append(y + (i * distancia))
                self.objeto_rect.append(sprite.get_rect(topleft=(self.x[-1], self.y[-1])))

    def desenhar_objetos(self):
        for i, sprite in enumerate(self.objeto_sprites):
            glob.tela.blit(sprite, (self.x[i], self.y[i]))

    def get_colisao_jogador(self):
        colisoes_jogador = self.objeto_rect.copy()
        if self.temMonstro:
            colisoes_jogador.append(inimigo.rect)
        return colisoes_jogador

    def get_colisao_monstro(self):
        return self.objeto_rect

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
