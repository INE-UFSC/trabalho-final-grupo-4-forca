from prototipo.cenas.cena import Cena
from prototipo.personagens import *
from prototipo.controladorInimigo import *


class Saguao(Cena):
    def __init__(self):
        super().__init__()
        self.teclaHorizontal = ""
        self.teclaVertical = ""
        self.fundo = pygame.image.load("../Assets/Sprites/cenario/chaoGrande.png")  # pygame.Surface((self.largura, self.altura))
        # self.parede = pygame.Surface((204, 147))
        # self.parede.blit(pygame.image.load("../Assets/Sprites/cenario/parede.png"), (0, 0))#fill(vermelho)
        self.parede = pygame.image.load("../Assets/Sprites/cenario/parede.png")
        self.parede0rect = self.parede.get_rect(topleft=(100, 40))
        self.parede1rect = self.parede.get_rect(topleft=(100, 375))
        self.parede2rect = self.parede.get_rect(topleft=(500, 500))
        self.lista_parederect = [self.parede0rect, self.parede1rect, self.parede2rect]

    def iniciar(self):
        # drawGroups()
        # construtorCenario.construirChao(0, 0, 60, construtorCenario.chaoPadrao)
        print("iniciou")
        self.iniciou = True

    def eventos(self):
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical)

        for retangulo in self.lista_parederect:
            if jogador.rect.colliderect(retangulo):
                jogador.resgata_posicao()

        if jogador.rect.colliderect(inimigo.rect):
            jogador.resgata_posicao()
        controlador.movimenta()

        for retangulo in self.lista_parederect:
            if inimigo.rect.colliderect(retangulo):
                inimigo.resgata_posicao()

        if inimigo.movimento_falhou:
            controlador.movimenta_x()
            for retangulo in self.lista_parederect:
                if inimigo.rect.colliderect(retangulo):
                    inimigo.resgata_posicao()
        if inimigo.movimento_falhou:
            controlador.movimenta_y()
            for retangulo in self.lista_parederect:
                if inimigo.rect.colliderect(retangulo):
                    inimigo.resgata_posicao()

        if inimigo.rect.colliderect(jogador.rect):
            inimigo.resgata_posicao()

        if self.tecla == "p":
            return "menuEmJogo"
        if self.tecla == "e":
            return "inventario"

    def atualizar(self):
        glob.tela.blit(self.fundo, (0, 0))
        # construtorCenario.drawGroups()
        # construtorCenario.updateGroups()
        glob.tela.blit(self.parede, (100, 40))
        glob.tela.blit(self.parede, (100, 375))
        glob.tela.blit(self.parede, (500, 500))
        draw_groups()
        update_groups()
