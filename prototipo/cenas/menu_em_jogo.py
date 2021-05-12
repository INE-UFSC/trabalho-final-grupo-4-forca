from prototipo.cenas.cena import Cena
from prototipo.cenas.menu_principal import MenuPrincipal
from prototipo.menu import *
from prototipo.personagens import *


class MenuEmJogo(Cena):

    def __init__(self):
        super().__init__()
        self.opcaoAtual = "continuar"
        self.fundo = bkg
        self.fundo2 = bkg2

    def iniciar(self):
        if MenuPrincipal.in_game == 1:
            glob.tela.blit(self.fundo2, (0, 0))
        else:
            glob.tela.blit(self.fundo, (0, 0))
        glob.tela.blit(menuTituloPausa.sprite, (menuTituloPausa.posicaoX, menuTituloPausa.posicaoY))
        glob.tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        glob.tela.blit(menuContinuar_em_jogo.sprite, (menuContinuar_em_jogo.posicaoX, menuContinuar_em_jogo.posicaoY))
        glob.tela.blit(menuConfiguracoesEmJogo.sprite, (menuConfiguracoesEmJogo.posicaoX, menuConfiguracoesEmJogo.posicaoY))
        glob.tela.blit(menuSairEmJogo.sprite, (menuSairEmJogo.posicaoX, menuSairEmJogo.posicaoY))

    def eventos(self):

        if self.tecla == "baixo":
            if self.opcaoAtual == "continuar":    self.opcaoAtual = "configuracoes"
            elif self.opcaoAtual == "configuracoes":   self.opcaoAtual = "sair"
            elif self.opcaoAtual == "sair":  self.opcaoAtual = "continuar"
            return None
        elif self.tecla == "cima":
            if self.opcaoAtual == "continuar":    self.opcaoAtual = "sair"
            elif self.opcaoAtual == "configuracoes":  self.opcaoAtual = "continuar"
            elif self.opcaoAtual == "sair":   self.opcaoAtual = "configuracoes"
            return None

        if self.tecla == "enter" and self.opcaoAtual == "continuar":
            return MenuEmJogo.cena_anterior
        elif self.tecla == "enter" and self.opcaoAtual == "configuracoes":
            return "menuConfig"
        elif self.tecla == "enter" and self.opcaoAtual == "sair":
            return "menuSair0"
        elif self.tecla == "esc":
            return MenuEmJogo.cena_anterior

    def atualizar(self):
        if self.opcaoAtual == "continuar" and menuSeta.posicaoY != 200:
            menuSeta.posicaoX = 200
            menuSeta.posicaoY = 200
        elif self.opcaoAtual == "configuracoes" and menuSeta.posicaoY != 280:
            menuSeta.posicaoX = 200
            menuSeta.posicaoY = 280
        elif self.opcaoAtual == "sair" and menuSeta.posicaoY != 361:
            menuSeta.posicaoX = 200
            menuSeta.posicaoY = 361


class MenuTutorial1(Cena):  # ----------------------------------------------
    def __init__(self):
        super().__init__()
        self.fundo3 = bkg3
        self.opcaoAtual = "continuar"

    def iniciar(self):
        glob.tela.blit(self.fundo3, (0, 0))
        glob.tela.blit(tutorial_titulo.sprite, (tutorial_titulo.posicaoX, tutorial_titulo.posicaoY))
        glob.tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        glob.tela.blit(tutorial1.sprite, (tutorial1.posicaoX, tutorial1.posicaoY))
        glob.tela.blit(menuContinuar3.sprite, (menuContinuar3.posicaoX, menuContinuar3.posicaoY))

    def eventos(self):
        if self.tecla == "enter" and self.opcaoAtual == "continuar":
            return "tutorial2"

    def atualizar(self):
        if self.opcaoAtual == "continuar" and menuSeta.posicaoY != 520:
            menuSeta.posicaoY = 520


class MenuTutorial2(Cena):  # ----------------------------------------------
    def __init__(self):
        super().__init__()
        self.fundo3 = bkg3
        self.opcaoAtual = "continuar"

    def iniciar(self):
        glob.tela.blit(self.fundo3, (0, 0))
        glob.tela.blit(tutorial_titulo.sprite, (tutorial_titulo.posicaoX, tutorial_titulo.posicaoY))
        glob.tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        glob.tela.blit(tutorial2.sprite, (tutorial2.posicaoX, tutorial2.posicaoY))
        glob.tela.blit(menuContinuar3.sprite, (menuContinuar3.posicaoX, menuContinuar3.posicaoY))

    def eventos(self):
        if self.tecla == "enter" and self.opcaoAtual == "continuar":
            return "inicio"

    def atualizar(self):
        if self.opcaoAtual == "continuar" and menuSeta.posicaoY != 520:
            menuSeta.posicaoY = 520



class MenuInventario(Cena):  # ----------------------------------------------
    def __init__(self):
        super().__init__()
        self.fundo = ibkg
        self.container = pygame.Surface((100, 100))
        self.container.fill((127, 127, 127))
        self.selectedBox = pygame.Surface((100, 100))
        self.selectedBox.fill((191, 191, 191))
        self.box_x = 150
        self.box_y = 100
        self.itemindex = 0
        self.jaMudou = False

    def iniciar(self):
        self.iniciou = True

    def eventos(self):
        if not self.jaMudou:
            if self.tecla == "esc":
                return MenuEmJogo.cena_anterior
            if self.tecla == "cima" and self.box_y > 100:
                self.box_y = self.box_y-100
                self.itemindex = self.itemindex - 5
            if self.tecla == "baixo" and self.box_y < 400:
                self.box_y = self.box_y + 100
                self.itemindex = self.itemindex + 5
            if self.tecla == "esquerda" and self.box_x > 150:
                self.box_x = self.box_x - 100
                self.itemindex = self.itemindex - 1
            if self.tecla == "direita" and self.box_x < 550:
                self.box_x = self.box_x + 100
                self.itemindex = self.itemindex + 1
            if self.tecla == "enter" and jogador.inventario[self.itemindex]!= None:
                if jogador.inventario[self.itemindex].usable == True:
                    jogador.aplica_efeito(self.itemindex)                               # não entendo por que não
                    jogador.remove_item(self.itemindex)                                 # funciona na mesma linha

        if self.tecla != "cima" and self.tecla != "baixo" and self.tecla != "direita" and self.tecla != "esquerda":
            self.jaMudou = False
        else:
            self.jaMudou = True

    def atualizar(self):
        glob.tela.blit(self.fundo, (100, 50))
        for i in range(0, 4):
            for j in range(0, 5):
                glob.tela.blit(self.container, (((j * 100) + 150), ((i * 100) + 100)))
        glob.tela.blit(self.selectedBox, (self.box_x, self.box_y))
        for i in range(0, 4):
            for j in range(0, 5):
                if jogador.inventario[(i * 5) + j] != None:
                    glob.tela.blit(jogador.inventario[(i * 5) + j].image, (((j * 100) + 150), ((i * 100) + 100)))


