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
        self.adicionalX = 0
        self.adicionalY = 0
        self.parede0rect = self.parede.get_rect(topleft=(100+self.adicionalX, 40+self.adicionalY))
        self.parede1rect = self.parede.get_rect(topleft=(100+self.adicionalX, 375+self.adicionalY))
        self.parede2rect = self.parede.get_rect(topleft=(500+self.adicionalX, 500+self.adicionalY))
        self.lista_colisoes_monstro = [self.parede0rect, self.parede1rect, self.parede2rect]
        self.lista_colisoes_jogador = [self.parede0rect, self.parede1rect, self.parede2rect, inimigo.rect]

    def iniciar(self):
        print("iniciou")
        self.iniciou = True

    def eventos(self):
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, self.lista_colisoes_jogador)
        controlador.movimenta()

        if glob.cameraDirecaoV == 1:
            self.adicionalY += jogador.velocidade
        elif glob.cameraDirecaoV == -1:
            self.adicionalY -= jogador.velocidade

        if glob.cameraDirecaoH == 1:
            self.adicionalX -= jogador.velocidade
        elif glob.cameraDirecaoH == -1:
            self.adicionalX += jogador.velocidade

        self.parede0rect = self.parede.get_rect(topleft=(100+self.adicionalX, 40+self.adicionalY))
        self.parede1rect = self.parede.get_rect(topleft=(100+self.adicionalX, 375+self.adicionalY))
        self.parede2rect = self.parede.get_rect(topleft=(500+self.adicionalX, 500+self.adicionalY))
        self.lista_colisoes_jogador = [self.parede0rect, self.parede1rect, self.parede2rect, inimigo.rect]


        for retangulo in self.lista_colisoes_monstro:
            if inimigo.rect.colliderect(retangulo):
                inimigo.resgata_posicao()

        if inimigo.movimento_falhou:
            controlador.movimenta_x()
            for retangulo in self.lista_colisoes_monstro:
                if inimigo.rect.colliderect(retangulo):
                    inimigo.resgata_posicao()
        if inimigo.movimento_falhou:
            controlador.movimenta_y()
            for retangulo in self.lista_colisoes_monstro:
                if inimigo.rect.colliderect(retangulo):
                    inimigo.resgata_posicao()

        if inimigo.rect.colliderect(jogador.rect):
            inimigo.resgata_posicao()


        if self.tecla == "p":
            return "menuEmJogo"
        if self.tecla == "e":
            return "inventario"

    def atualizar(self):
        glob.tela.blit(self.fundo, (0+self.adicionalX, 0+self.adicionalY))
        glob.tela.blit(self.parede, (100+self.adicionalX, 40+self.adicionalY))
        glob.tela.blit(self.parede, (100+self.adicionalX, 375+self.adicionalY))
        glob.tela.blit(self.parede, (500+self.adicionalX, 500+self.adicionalY))
        draw_groups()
        update_groups()
