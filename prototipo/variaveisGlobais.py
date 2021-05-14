import pygame
import configparser
config = configparser.ConfigParser()


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
        config.read('config.ini')

        try:
            self.volume_efeitos = config.getfloat('volume', 'volume_efeitos')
            self.volume_musica = config.getfloat('volume', 'volume_musica')
        except:
            self.volume_efeitos = 0.1
            self.volume_musica = 0.1


glob = Global()
