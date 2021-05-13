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

        # Cores --------------------
        self.preto = (0, 0, 0)
        self.branco = (255, 255, 255)
        self.verde = (0, 255, 0)
        self.vermelho = (255, 0, 0)

        # Sons ---------------------
        pygame.mixer.init()
        self.volume = 0.1
        self.porta_som = pygame.mixer.Sound("../Assets/sons/porta.mp3")
        self.porta_som.set_volume(self.volume)
        self.passos = pygame.mixer.Sound("../Assets/sons/passos.wav")
        self.passos.set_volume(self.volume)
        self.monstro1 = pygame.mixer.Sound("../Assets/sons/monstro.mp3")
        self.monstro1.set_volume(self.volume)
        self.monstro2 = pygame.mixer.Sound("../Assets/sons/rugido.mp3")
        self.monstro2.set_volume(self.volume)
        self.vela = pygame.mixer.Sound("../Assets/sons/vela.wav")
        self.vela.set_volume(self.volume)
        self.pegar_item = pygame.mixer.Sound("../Assets/sons/pegar_item.wav")
        self.pegar_item.set_volume(self.volume)


glob = Global()
