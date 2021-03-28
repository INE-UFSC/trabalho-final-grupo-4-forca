import pygame

#   Código principal do Menu.


class Menu:

    def __init__(self):
        self.posicaoX = 120
        self.posicaoY = 50
        self.sprite = pygame.image.load("../Assets/titulo.png")
        self.elementosMostrados = False


class MenuContinuar(Menu):

    def __init__(self):
        super().__init__()
        self.posicaoX = 280
        self.posicaoY = 200
        self.sprite = pygame.image.load("../Assets/opcao.png")


class MenuNovoJogo(Menu):

    def __init__(self):
        super().__init__()
        self.posicaoX = 280
        self.posicaoY = 280
        self.sprite = pygame.image.load("../Assets/opcao.png")


class MenuConfiguracoes(Menu):

    def __init__(self):
        super().__init__()
        self.posicaoX = 280
        self.posicaoY = 360
        self.sprite = pygame.image.load("../Assets/opcao.png")


class MenuSair(Menu):

    def __init__(self):
        super().__init__()
        self.posicaoX = 280
        self.posicaoY = 440
        self.sprite = pygame.image.load("../Assets/opcao.png")


menu = Menu()
menuContinuar = MenuContinuar()
menuNovoJogo = MenuNovoJogo()
menuConfiguracoes = MenuConfiguracoes()
menuSair = MenuSair()
