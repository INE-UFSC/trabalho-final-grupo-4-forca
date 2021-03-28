import pygame
from menu import *
from variaveisGlobais import *


class Cena:

    def __init__(self):
        self.largura = 800
        self.altura = 600
        self.fundo = ""
        self.tecla = ""

    def iniciar(self):
        pass

    def atualizar(self):
        pass


class MenuPrincipal(Cena):

    def __init__(self):
        super().__init__()
        self.fundo = pygame.image.load("../Assets/menuPrincipal/fundo.jpg")
        self.opcaoAtual = "continuar"


    def iniciar(self):
#   Evitar que os elementos sejam desenhados mais que uma vez.
        tela.blit(self.fundo, (0, 0))
        tela.blit(menuTitulo.sprite, (menuTitulo.posicaoX, menuTitulo.posicaoY))
        tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        tela.blit(menuContinuar.sprite, (menuContinuar.posicaoX, menuContinuar.posicaoY))
        tela.blit(menuNovoJogo.sprite, (menuNovoJogo.posicaoX, menuNovoJogo.posicaoY))
        tela.blit(menuConfiguracoes.sprite, (menuConfiguracoes.posicaoX, menuConfiguracoes.posicaoY))
        tela.blit(menuSair.sprite, (menuSair.posicaoX, menuSair.posicaoY))

    def eventos(self):
        if self.tecla == "baixo":
            if self.opcaoAtual == "continuar":    self.opcaoAtual = "novoJogo"
            elif self.opcaoAtual == "novoJogo":   self.opcaoAtual = "configuracoes"
            elif self.opcaoAtual == "configuracoes":  self.opcaoAtual = "sair"
            elif self.opcaoAtual == "sair":   self.opcaoAtual = "continuar"
        elif self.tecla == "cima":
            if self.opcaoAtual == "continuar":    self.opcaoAtual = "sair"
            elif self.opcaoAtual == "novoJogo":   self.opcaoAtual = "continuar"
            elif self.opcaoAtual == "configuracoes":  self.opcaoAtual = "novoJogo"
            elif self.opcaoAtual == "sair":   self.opcaoAtual = "configuracoes"

    def atualizar(self):
        if self.opcaoAtual == "continuar" and menuSeta.posicaoY != 200:
            menuSeta.posicaoY = 200
        elif self.opcaoAtual == "novoJogo" and menuSeta.posicaoY != 280:
            menuSeta.posicaoY = 280
        elif self.opcaoAtual == "configuracoes" and menuSeta.posicaoY != 360:
            menuSeta.posicaoY = 360
        elif self.opcaoAtual == "sair" and menuSeta.posicaoY != 440:
            menuSeta.posicaoY = 440


class Saguao(Cena):

    def __init__(self, largura, altura):
        super().__init__()
        self.largura = largura
        self.altura = altura


cena = Cena()
menuPrincipal = MenuPrincipal()
