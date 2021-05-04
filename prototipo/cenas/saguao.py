from prototipo.cenas.cena import Cena
from prototipo.personagens import *
from prototipo.controladorInimigo import *
from prototipo.cenas.colisao import Colisao


class Saguao(Cena):
    def __init__(self):
        super().__init__()
        self.teclaHorizontal = ""
        self.teclaVertical = ""
        self.fundo = pygame.image.load("../Assets/Sprites/cenario/chaoGrande.png")
        self.cenaJogavel = True
        self.lista_colisoes_monstro = colisao.get_colisao_monstro()
        self.lista_colisoes_jogador = colisao.get_colisao_jogador()

    def iniciar(self):
        print("iniciou")
        self.iniciou = True

    def eventos(self):
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, self.lista_colisoes_jogador)
        controlador.movimenta()
        colisao.colisao_monstro()

        if self.tecla == "p":
            return "menuEmJogo"
        elif self.tecla == "e":
            return "inventario"

    def atualizar(self):
        glob.tela.blit(self.fundo, (0, 0))
        colisao.draw()
        draw_groups()
        update_groups()


class ColisaoSaguao(Colisao):

    def __init__(self):
        self.parede_sprite = pygame.image.load("../Assets/Sprites/cenario/parede.png")
        self.x = [100, 100, 500]
        self.y = [40, 375, 500]
        self.parede_rect = [self.parede_sprite.get_rect(topleft=(self.x[0], self.y[0])),
                            self.parede_sprite.get_rect(topleft=(self.x[1], self.y[1])),
                            self.parede_sprite.get_rect(topleft=(self.x[2], self.y[2]))]

    def draw(self):
        glob.tela.blit(self.parede_sprite, (self.x[0], self.y[0]))
        glob.tela.blit(self.parede_sprite, (self.x[1], self.y[1]))
        glob.tela.blit(self.parede_sprite, (self.x[2], self.y[2]))

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


colisao = ColisaoSaguao()
