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


class SpritesPorao(SpritesCena):  # Classe que armazena os sprites da cena.
    def __init__(self):
        super().__init__()
        self.sprite_mesa = pygame.transform.scale(self.sprite_mesa, (90, 70))
        self.sprite_bau = self.load_image("Assets/Sprites/cenario/bau.png", True)
        self.sprite_bau_si = self.load_image("Assets/Sprites/cenario/bau_sem_item.png", True)
        self.sprite_chave = self.load_image("Assets/Sprites/cenario/chave.png", True)
        self.pegou_chave = self.load_image("Assets/Sprites/hud/pegou_chave.png", True)
        self.pegou_cobre = self.load_image("Assets/Sprites/hud/pegou_cobre.png", True)

spritesPorao = SpritesPorao()


class ColisaoPorao(Colisao):  # Classe responsável por construir os objetos do cenário e suas colisões.

    def __init__(self):
        super().__init__()
        self.temMonstro = False

    def construir_cenario(self):
        self.construir_objeto(spritesPorao.parede_sprite_v, 150, 0, "porao", 4, "vertical", 26, "paredecobre1")
        self.construir_objeto(spritesPorao.parede_sprite_v, 250, 0, "porao", 4, "vertical", 26, "paredecobre2")
        self.construir_objeto(spritesPorao.parede_sprite_vh, 0, 160, "porao", 13, "horizontal", 26, "lab1")
        self.construir_objeto(spritesPorao.parede_sprite_v, 338, 56, "porao", 5, "vertical", 26, "lab2")
        self.construir_objeto(spritesPorao.parede_sprite_vh, 364, 56, "porao", 6, "horizontal", 26, "lab3")
        self.construir_objeto(spritesPorao.parede_sprite_v, 494, 82, "porao", 7, "vertical", 26, "lab4")
        self.construir_objeto(spritesPorao.parede_sprite_v, 572, 82, "porao", 10, "vertical", 26, "lab5")
        self.construir_objeto(spritesPorao.parede_sprite_vh, 572, 56, "porao", 6, "horizontal", 26, "lab6")
        self.construir_objeto(spritesPorao.parede_sprite_vh, 0, 316, "porao", 22, "horizontal", 26, "lab7")
        self.construir_objeto(spritesPorao.parede_sprite_vh, 78, 238, "porao", 16, "horizontal", 26, "lab8")
        self.construir_objeto(spritesPorao.parede_sprite_vh, 650, 160, "porao", 6, "horizontal", 26, "lab9")
        self.construir_objeto(spritesPorao.parede_sprite_v, 650, 186, "porao", 6, "vertical", 26, "lab10")
        self.construir_objeto(spritesPorao.parede_sprite_vh, 0, 394, "porao", 28, "horizontal", 26, "lab11")
        self.construir_objeto(spritesPorao.parede_sprite_v, 728, 394, "porao", 4, "vertical", 26, "lab12")
        self.construir_objeto(spritesPorao.parede_sprite_vh, 208, 472, "porao", 20, "horizontal", 26, "lab13")
        self.construir_objeto(spritesPorao.sprite_mesa, 30, 425, "porao", adicionalY=-40)
        self.construir_objeto(spritesPorao.sprite_bau_si, 403, 92, "porao", adicionalY=-28)
        if not item.cobre1:
            self.construir_objeto(spritesPorao.sprite_bau, 403, 92, "porao", adicionalY=-28, identificacao="bau")
        if not item.possui_chave_cozinha:
            self.construir_objeto(spritesPorao.sprite_chave, 65, 429, "porao", identificacao="chave")
        self.construir_objeto(spritesPorao.parede_sprite_vh, 104, 574, "porao", 30)


colisao = ColisaoPorao()


class Porao(Cena):  # Primeira parte do porão.

    def __init__(self):  # É executado apenas na instanciação da cena.
        super().__init__()
        self.cenaJogavel = True

    def iniciar(self):  # É executado 1 vez sempre que a cena é chamada.
        print("iniciou porao")
        jogador.rect.topleft = (50, 550)
        colisao.construir_cenario()
        self.delay = 10
        self.iniciou = True

    def eventos(self):  # Captura os eventos do teclado e do cenário.
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, colisao.get_colisao_jogador("porao"))

        if self.delay > 0:
            self.delay -= 1

        if self.tecla == "p":
            MenuEmJogo.cena_anterior = "porao"
            return "menuEmJogo"
        elif self.tecla == "i":
            MenuEmJogo.cena_anterior = "porao"
            return "inventario"
        elif self.tecla == "e":
            if colisao.distancia(jogador, 50, 550) < 50 and self.delay <= 0:
                self.iniciou = False
                som.passos.play()
                return "saguao"
            if colisao.distancia(jogador, 80, 454) < 50 and self.delay <= 0 and not item.possui_chave_cozinha:
                item.possui_chave_cozinha = True
                jogador.adiciona_item(itens.chave)
                colisao.destruir_objeto("chave")
                som.pegar_item.play()
                glob.tela.fill((glob.preto))
                glob.tela.blit(spritesPorao.pegou_chave, spritesPorao.pegou_chave.get_rect(center=glob.tela.get_rect().center))
                pygame.display.flip()
                sleep(2)
            if colisao.distancia(jogador, 430, 103) < 30 and self.delay <= 0 and not item.cobre1:
                item.cobre1 = True
                jogador.adiciona_item(itens.cobre)
                colisao.destruir_objeto("bau")
                som.pegar_item.play()
                glob.tela.fill((glob.preto))
                glob.tela.blit(spritesPorao.pegou_cobre, spritesPorao.pegou_cobre.get_rect(center=glob.tela.get_rect().center))
                pygame.display.flip()
                sleep(2)

    def desenhar_objetos_externos(self):
        jogadorGroup.draw(glob.tela)
        glob.tela.blit(spritesPorao.sprite_iluminacao, (jogador.rect.center[0] - 1200, jogador.rect.center[1] - 900))
        hud.desenhar_hud(jogador.stamina, jogador.vida, jogador.rect.center[0] - 30, jogador.rect.top - 30,
                         self.mostrarVida)
        jogadorGroup.update()

    def atualizar(self):  # Atualiza os sprites da cena.
        glob.tela.blit(spritesPorao.fundo, (0, 0))
        colisao.desenhar_objetos("porao")
        self.desenhar_objetos_externos()
