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

class SpritesOficina(SpritesCena):
    def __init__(self):
        super().__init__()
        self.sprite_caixa = self.load_image("Assets/Sprites/cenario/caixas.png", True)
        self.sprite_machado = self.load_image("Assets/Sprites/cenario/machado.png", True)
        self.sprite_martelo = self.load_image("Assets/Sprites/cenario/martelo.png", True)
        self.sprite_mesa_grande = self.load_image("Assets/Sprites/cenario/mesa_grande.png", True)
        self.sprite_parede_vh = self.load_image("Assets/Sprites/cenario/parede_verticalh.png")
        self.sprite_bau = self.load_image("Assets/Sprites/cenario/bau.png", True)
        self.sprite_boneco = self.load_image("Assets/Sprites/cenario/boneco.png", True)
        self.pegou_ferramenta2 = self.load_image("Assets/Sprites/hud/pegou_ferramenta2.png", True)
        self.sprite_bau_si = self.load_image("Assets/Sprites/cenario/bau_sem_item.png", True)

spritesOficina = SpritesOficina()

class ColisaoOficina(Colisao):
    def __init__(self):
        super().__init__()
    
    def construir_cenario(self):
        self.construir_objeto(spritesOficina.parede_sprite_h, 0, 0, "oficina", 5)
        self.construir_objeto(spritesOficina.parede_sprite_v, 0, 26, "oficina", 10, "vertical")  # Parede esquerda 1
        self.construir_objeto(spritesOficina.parede_sprite_v, 0, 350, "oficina", 10, "vertical")  # Parede esquerda 2
        self.construir_objeto(spritesOficina.parede_sprite_v, 774, 1, "oficina", 24, orientacao = "vertical")
        self.construir_objeto(spritesOficina.sprite_caixa, 620, 120, "oficina")
        self.construir_objeto(spritesOficina.sprite_caixa, 550, 200, "oficina")
        self.construir_objeto(spritesOficina.sprite_caixa, 680, 240, "oficina")
        self.construir_objeto(spritesOficina.sprite_caixa, 450, 120, "oficina")
        self.construir_objeto(spritesOficina.sprite_parede_vh, 384, 400, "oficina", 15)
        self.construir_objeto(spritesOficina.sprite_bau_si, 600, 426, "oficina", adicionalY=-28)
        if not item.possui_ferramenta_cozinha:
            self.construir_objeto(spritesOficina.sprite_bau, 600, 426, "oficina", adicionalY=-28, identificacao="bau")
        self.construir_objeto(spritesOficina.sprite_mesa_grande, 120, 200, "oficina")
        self.construir_objeto(spritesOficina.sprite_machado, 140, 220, "oficina")
        self.construir_objeto(spritesOficina.sprite_martelo, 180, 220, "oficina")
        self.construir_objeto(spritesOficina.sprite_boneco, 100, 120, "oficina", 3)
        self.construir_objeto(spritesOficina.parede_sprite_vh, 0, 574, "oficina", 35)
        

colisao = ColisaoOficina()

class Oficina(Cena):
    def __init__(self):
        super().__init__()
        self.cenaJogavel = True
        colisao.construir_cenario()

    def iniciar(self):  # É executado 1 vez sempre que a cena é chamada.
        print("iniciou oficina")
        if glob.cenaAtual == "sala":
            jogador.rect.topleft = (10, 290)
        glob.cenaAtual = "oficina"
        colisao.construir_cenario()
        self.delay = 10
        self.iniciou = True

    def eventos(self):  # Captura os eventos do teclado e do cenário.
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, colisao.get_colisao_jogador("oficina"))

        if self.delay > 0:
            self.delay -= 1

        if self.tecla == "p":
            MenuEmJogo.cena_anterior = "oficina"
            return "menuEmJogo"
        elif self.tecla == "i":
            MenuEmJogo.cena_anterior = "oficina"
            return "inventario"
        elif self.tecla == "e":
            if colisao.distancia(jogador, 0, 280) < 50 and self.delay <= 0:
                self.iniciou = False
                som.porta_som.play()
                return "sala"
            if colisao.distancia(jogador, 625, 453) < 30 and self.delay <= 0 and not item.possui_ferramenta_cozinha:
                item.possui_ferramenta_cozinha = True
                jogador.adiciona_item(itens.ferramenta2)
                colisao.destruir_objeto("bau")
                som.pegar_item.play()
                glob.tela.fill((glob.preto))
                glob.tela.blit(spritesOficina.pegou_ferramenta2, spritesOficina.pegou_ferramenta2.get_rect(center=glob.tela.get_rect().center))
                pygame.display.flip()
                sleep(2)
        
    def desenhar_objetos_externos(self):
        jogadorGroup.draw(glob.tela)
        glob.tela.blit(spritesOficina.sprite_iluminacao, (jogador.rect.center[0] - 1200, jogador.rect.center[1] - 900))
        hud.desenhar_hud(jogador.stamina, jogador.vida, jogador.rect.center[0] - 30, jogador.rect.top - 30, self.mostrarVida)
        jogadorGroup.update()


    def atualizar(self):  # Atualiza os sprites da cena.
        glob.tela.blit(spritesOficina.fundo, (0, 0))
        colisao.desenhar_objetos("oficina")
        self.desenhar_objetos_externos()
