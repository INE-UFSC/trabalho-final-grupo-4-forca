import pygame


class Global:

    def __init__(self):
        # Variáveis gerais ---------
        pygame.display.set_caption("Any way out?")
        self.tamanhoTela = (800, 600)
        self.tela = pygame.display.set_mode(self.tamanhoTela)
        self.jogoAberto = True
        self.clock = pygame.time.Clock()
        self.cenaAtual = None
        self.volume = 0.1
        pygame.mixer.init()

        # Cores --------------------
        self.preto = (0, 0, 0)
        self.branco = (255, 255, 255)
        self.verde = (0, 255, 0)
        self.vermelho = (255, 0, 0)


glob = Global()
