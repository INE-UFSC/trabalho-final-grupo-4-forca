from prototipo.cenas.cena import Cena
from prototipo.variaveisGlobais import glob
from prototipo.cenas.colisao import Colisao
from prototipo.cenas.sprites import SpritesCena
from prototipo.personagens import *
from prototipo.cenas.menu_em_jogo import MenuEmJogo
from prototipo import som
import pygame
from prototipo.hud import hud
from time import sleep


class SpritesArmazem(SpritesCena):
    def __init__(self):
        super().__init__()
        self.sprite_caixa = self.load_image("../Assets/Sprites/cenario/caixas.png", True)
        self.sprite_machado = self.load_image("../Assets/Sprites/cenario/machado.png", True)
        self.sprite_martelo = self.load_image("../Assets/Sprites/cenario/martelo.png", True)
        self.sprite_vassoura = self.load_image("../Assets/Sprites/cenario/vassoura.png", True)
        self.sprite_barril = self.load_image("../Assets/Sprites/cenario/barril.png", True)
        self.sprite_mesa = self.load_image("../Assets/Sprites/cenario/mesa_trabalho.png", True)
        self.sprite_parede_vh = self.load_image("../Assets/Sprites/cenario/parede_verticalh.png")
        self.sprite_bau = self.load_image("../Assets/Sprites/cenario/bau.png", True)
        self.sprite_porta = self.load_image("../Assets/Sprites/cenario/porta_sala.png", True)
        self.pegou_ferramenta1 = self.load_image("../Assets/Sprites/hud/pegou_ferramenta1.png", True)
        self.sprite_bau_si = self.load_image("../Assets/Sprites/cenario/bau_sem_item.png", True)

spritesArmazem = SpritesArmazem()

class ColisaoArmazem(Colisao):
    def __init__(self):
        super().__init__()
    
    def construir_cenario(self):
        self.construir_objeto(spritesArmazem.sprite_mesa, 26, 220, "armazem", adicionalY=-28)
        self.construir_objeto(spritesArmazem.parede_sprite_h, 0, 0, "armazem", 5, adicionalY=-30)
        self.construir_objeto(spritesArmazem.parede_sprite_v, 0, 1, "armazem", 24, orientacao = "vertical")
        self.construir_objeto(spritesArmazem.parede_sprite_v, 774, 1, "armazem", 24, orientacao = "vertical")
        self.construir_objeto(spritesArmazem.sprite_caixa, 620, 120, "armazem")
        self.construir_objeto(spritesArmazem.sprite_caixa, 550, 200, "armazem")
        self.construir_objeto(spritesArmazem.sprite_caixa, 680, 240, "armazem")
        self.construir_objeto(spritesArmazem.sprite_caixa, 450, 120, "armazem")
        self.construir_objeto(spritesArmazem.sprite_machado, 30, 250, "armazem")
        self.construir_objeto(spritesArmazem.sprite_martelo, 30, 290, "armazem")
        self.construir_objeto(spritesArmazem.sprite_vassoura, 60, 20, "armazem", 3)
        self.construir_objeto(spritesArmazem.sprite_barril, 100, 140, "armazem", 3, adicionalY=-28)
        self.construir_objeto(spritesArmazem.sprite_barril, 100, 176, "armazem", 3, adicionalY=-28)
        self.construir_objeto(spritesArmazem.sprite_parede_vh, 384, 400, "armazem", 15)
        self.construir_objeto(spritesArmazem.sprite_bau_si, 600, 426, "armazem", adicionalY=-28)
        if not item.possui_ferramenta_sala:
            self.construir_objeto(spritesArmazem.sprite_bau, 600, 426, "armazem", adicionalY=-28, identificacao="bau")
        self.construir_objeto(spritesArmazem.parede_sprite_vh, 0, 574, "armazem", 35)
        self.construir_objeto(spritesArmazem.sprite_porta, 375, 28, "armazem", 1, identificacao="porta_armazem", adicionalY=-30)
        

colisao = ColisaoArmazem()

class Armazem(Cena):
    def __init__(self):
        super().__init__()
        self.cenaJogavel = True

    def iniciar(self): 
        print("iniciou armazem")
        if glob.cenaAtual == "cozinha":
            jogador.rect.topleft = (385, 110)
        glob.cenaAtual = "armazem"
        colisao.construir_cenario()
        self.delay = 10
        self.iniciou = True

    def eventos(self):  
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, colisao.get_colisao_jogador("armazem"))

        if self.delay > 0:
            self.delay -= 1

        if self.tecla == "p":
            MenuEmJogo.cena_anterior = "armazem"
            return "menuEmJogo"
        elif self.tecla == "i":
            MenuEmJogo.cena_anterior = "armazem"
            return "inventario"
        elif self.tecla == "e":
            if colisao.distancia(jogador, 400, 115) < 50 and self.delay <= 0:
                self.iniciou = False
                som.porta_som.play()
                return "cozinha"
            if colisao.distancia(jogador, 625, 453) < 30 and self.delay <= 0 and not item.possui_ferramenta_sala:
                item.possui_ferramenta_sala = True
                jogador.adiciona_item(itens.ferramenta1)
                colisao.destruir_objeto("bau")
                som.pegar_item.play()
                glob.tela.fill((glob.preto))
                glob.tela.blit(spritesArmazem.pegou_ferramenta1, spritesArmazem.pegou_ferramenta1.get_rect(center=glob.tela.get_rect().center))
                pygame.display.flip()
                sleep(2)

    def desenhar_objetos_externos(self):
        jogadorGroup.draw(glob.tela)
        glob.tela.blit(spritesArmazem.sprite_iluminacao, (jogador.rect.center[0] - 1200, jogador.rect.center[1] - 900))
        hud.desenhar_hud(jogador.stamina, jogador.vida, jogador.rect.center[0] - 30, jogador.rect.top - 30,
                         self.mostrarVida)
        jogadorGroup.update()

    def atualizar(self):
        glob.tela.blit(spritesArmazem.fundo, (0, 0))
        colisao.desenhar_objetos("armazem")
        self.desenhar_objetos_externos()
