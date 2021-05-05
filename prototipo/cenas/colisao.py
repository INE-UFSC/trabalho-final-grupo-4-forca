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
        self.construir_cenario()

    def draw(self):
        pass

    def construir_cenario(self):
        pass

    def construir_parede(self, orientacao, x, y, quantidade):
        for i in range(quantidade):
            self.orientacao.append(orientacao)
            if orientacao == "horizontal":
                self.x.append(x + (i * 183))
                self.y.append(y)
                self.parede_rect.append(self.parede_sprite_h.get_rect(topleft=(self.x[-1], self.y[-1])))
            elif orientacao == "vertical":
                self.x.append(x)
                self.y.append(y + (i * 26))
                self.parede_rect.append(self.parede_sprite_v.get_rect(topleft=(self.x[-1], self.y[-1])))

    def desenhar_paredes(self):
        for i, orientacao in enumerate(self.orientacao):
            if orientacao == "horizontal":
                glob.tela.blit(self.parede_sprite_h, (self.x[i], self.y[i]))
            elif orientacao == "vertical":
                glob.tela.blit(self.parede_sprite_v, (self.x[i], self.y[i]))

    def get_colisao_jogador(self):
        colisoes_jogador = self.parede_rect.copy()
        colisoes_jogador.append(inimigo.rect)
        return colisoes_jogador

    def get_colisao_monstro(self):
        return self.parede_rect

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
