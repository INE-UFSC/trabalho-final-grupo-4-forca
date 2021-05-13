from prototipo.variaveisGlobais import glob
from prototipo.personagens import *
from prototipo.hud import hud
from prototipo.cenas.sprites import spritesCena


class Cena:

    def __init__(self):
        self.largura = glob.tamanhoTela[0]
        self.altura = glob.tamanhoTela[1]
        self.fundo = ""
        self.tecla = ""
        self.cenaJogavel = False
        self.proximaCena = "nenhuma"
        self.iniciou = False
        self.delay = 10
        self.mostrarVida = False

    def iniciar(self):
        pass

    def eventos(self):
        pass

    def atualizar(self):
        pass

    def desenhar_objetos_externos(self):
        jogadorGroup.draw(glob.tela)
        glob.tela.blit(spritesCena.sprite_iluminacao, (jogador.rect.center[0] - 1200, jogador.rect.center[1] - 900))
        hud.desenhar_hud(jogador.stamina, jogador.vida, jogador.rect.center[0] - 30, jogador.rect.top - 30,
                         self.mostrarVida)
        jogadorGroup.update()


