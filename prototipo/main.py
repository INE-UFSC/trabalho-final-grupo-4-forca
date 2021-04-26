from prototipo.cenas import *
import pygame


class Main:

    def __init__(self):
        self.cenaAtual = menuPrincipal
        self.jogoAberto = True

#   Loop que mantém o jogo aberto.
    def runGame(self):
        while self.jogoAberto:
            self.cenaAtual.tecla = "outra"
            self.cenaAtual.teclaHorizontal = "outra"
            self.cenaAtual.teclaVertical = "outra"

        #   Verificação constante de eventos.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogoAberto = False
                elif self.cenaAtual == menuPrincipal and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.cenaAtual.tecla = "baixo"
                    elif event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.cenaAtual.tecla = "cima"
                    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.cenaAtual.tecla = "esquerda"
                    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.cenaAtual.tecla = "direita"
                    elif event.key == pygame.K_RETURN:
                        self.cenaAtual.tecla = "enter"

            if self.cenaAtual == cenarioTeste:
                pressed = pygame.key.get_pressed()
                if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
                    self.cenaAtual.tecla = "baixo"
                    self.cenaAtual.teclaVertical = "baixo"
                elif pressed[pygame.K_w] or pressed[pygame.K_UP]:
                    self.cenaAtual.tecla = "cima"
                    self.cenaAtual.teclaVertical = "cima"

                if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
                    self.cenaAtual.tecla = "esquerda"
                    self.cenaAtual.teclaHorizontal = "esquerda"
                elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
                    self.cenaAtual.tecla = "direita"
                    self.cenaAtual.teclaHorizontal = "direita"
                elif pressed[pygame.K_RETURN]:
                    self.cenaAtual.tecla = "enter"

            self.cenaAtual.proximaCena = self.cenaAtual.eventos()

            self.cenaAtual.iniciar()
            self.cenaAtual.atualizar()

        #   Atualizar os elementos na tela.
            pygame.display.flip()

        #   Verificar se a cena atual desencadeou algum evento.
            if self.cenaAtual.proximaCena == "cenarioTeste":
                self.cenaAtual = cenarioTeste
            elif self.cenaAtual.proximaCena == "fecharJogo":
                self.jogoAberto = False

        #   Limitar o FPS do jogo.
            clock.tick(60)


jogo = Main()
jogo.runGame()
