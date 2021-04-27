import pygame

#   Variáveis gerais ---------
largura = 800
altura = 600
tamanhoTela = (largura, altura)
tela = pygame.display.set_mode(tamanhoTela)
pygame.display.set_caption("Any way out?")
jogoAberto = True
clock = pygame.time.Clock()
faseAtual = None


#   Cores --------------------
preto = (0, 0, 0)
branco = (255, 255, 255)
verde = (0, 255, 0)
vermelho = (255, 0, 0)
