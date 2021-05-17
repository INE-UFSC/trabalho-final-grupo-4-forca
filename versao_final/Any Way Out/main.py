from prototipo.cenas.cenas import cenas
import pygame
from prototipo.variaveisGlobais import glob
from prototipo.controladorInimigo import ControladorInimigo
from configparser import ConfigParser
config = ConfigParser()


class Main:

    def __init__(self):
        self.cenaAtual = cenas.menuPrincipal
        self.jogoAberto = True
        self.clock = pygame.time.Clock()
        pygame.mixer.music.load("Assets/musicas/menu.mp3")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(glob.volume_musica)

#   Loop que mantém o jogo aberto.
    def run_game(self):

        while self.jogoAberto:

            self.cenaAtual.tecla = "outra"
            self.cenaAtual.teclaHorizontal = "outra"
            self.cenaAtual.teclaVertical = "outra"

            # Verificação constante de eventos.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.jogoAberto = False
                # Verificar se as teclas especificadas foram pressionadas 1 vez.
                elif event.type == pygame.KEYDOWN and not self.cenaAtual.cenaJogavel:
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

                    if self.cenaAtual == cenas.menuPrincipal or self.cenaAtual == cenas.menuConfig or self.cenaAtual == cenas.menuControles:
                        if event.key == pygame.K_RETURN:
                            self.cenaAtual.tecla = "enter"
                    elif self.cenaAtual == cenas.menuInventario or self.cenaAtual == cenas.menuEmJogo:
                        if event.key == pygame.K_RETURN:
                            self.cenaAtual.tecla = "enter"
                        elif event.key == pygame.K_ESCAPE:
                            self.cenaAtual.tecla = "esc"

            # Verificar se as teclas especificadas estão sendo pressionadas constantemente.
            if self.cenaAtual.cenaJogavel:
                pressed = pygame.key.get_pressed()
                # Movimentação vertical
                if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
                    self.cenaAtual.tecla = "baixo"
                    self.cenaAtual.teclaVertical = "baixo"
                elif pressed[pygame.K_w] or pressed[pygame.K_UP]:
                    self.cenaAtual.tecla = "cima"
                    self.cenaAtual.teclaVertical = "cima"
                # Movimentação horizontal
                if pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
                    self.cenaAtual.tecla = "esquerda"
                    self.cenaAtual.teclaHorizontal = "esquerda"
                elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
                    self.cenaAtual.tecla = "direita"
                    self.cenaAtual.teclaHorizontal = "direita"

                # Teclas utilitárias
                if pressed[pygame.K_LSHIFT]:
                    self.cenaAtual.tecla = "shift"
                elif pressed[pygame.K_e]:
                    self.cenaAtual.tecla = "e"
                elif pressed[pygame.K_i]:
                    self.cenaAtual.tecla = "i"
                elif pressed[pygame.K_p]:
                    self.cenaAtual.tecla = "p"
                elif pressed[pygame.K_RETURN]:
                    self.cenaAtual.tecla = "enter"

            if not self.cenaAtual.iniciou:
                self.cenaAtual.iniciar()
            self.cenaAtual.proximaCena = self.cenaAtual.eventos()
            self.cenaAtual.atualizar()

        #   Atualizar os elementos na tela.
            pygame.display.flip()

        #   Verificar se a cena atual desencadeou algum evento de mudança.
            if self.cenaAtual.proximaCena in cenas.nomes:
                self.cenaAtual = cenas.cenas[cenas.nomes.index(self.cenaAtual.proximaCena)]
            if self.cenaAtual.proximaCena == "fecharJogo":
                self.jogoAberto = False

        #   Limitar o FPS do jogo.
            self.clock.tick(60)
            #print(self.clock)
            #print(glob.cenaAtual)


jogo = Main()
jogo.run_game()
