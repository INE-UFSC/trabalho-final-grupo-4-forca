import pygame

#   Código principal do Menu.


class Menu:

    def __init__(self):
        self.posicaoX = 120
        self.posicaoY = 50
        self.sprite = pygame.image.load("../Assets/menuPrincipal/titulo.png")


class MenuContinuar(Menu):

    def __init__(self, sprite, x, y):
        super().__init__()
        self.posicaoX = x
        self.posicaoY = y
        self.sprite = pygame.image.load(sprite)


class MenuNovoJogo(Menu):

    def __init__(self, sprite, x, y):
        super().__init__()
        self.posicaoX = x
        self.posicaoY = y
        self.sprite = pygame.image.load(sprite)


class MenuConfiguracoes(Menu):

    def __init__(self, sprite, x, y):
        super().__init__()
        self.posicaoX = x
        self.posicaoY = y
        self.sprite = pygame.image.load(sprite)


class MenuSair(Menu):

    def __init__(self, sprite, x, y):
        super().__init__()
        self.posicaoX = x
        self.posicaoY = y
        self.sprite = pygame.image.load(sprite)


class MenuSeta(Menu):

    def __init__(self, sprite, x, y):
        super().__init__()
        self.posicaoX = x
        self.posicaoY = y
        self.sprite = pygame.image.load(sprite)


menu = Menu()
menuContinuar = MenuContinuar("../Assets/menuPrincipal/continuar.png", 280, 200)
menuNovoJogo = MenuNovoJogo("../Assets/menuPrincipal/novoJogo.png", 280, 280)
menuConfiguracoes = MenuConfiguracoes("../Assets/menuPrincipal/configuracoes.png", 280, 360)
menuSair = MenuSair("../Assets/menuPrincipal/sair.png", 280, 440)
menuSeta = MenuSeta("../Assets/menuPrincipal/seta.png", 210, 200)
