from prototipo.cenas.cena import Cena
from prototipo.variaveisGlobais import glob
from prototipo.cenas.colisao import Colisao
from prototipo.cenas.sprites import SpritesCena
from prototipo.personagens import *
from prototipo.cenas.menu_em_jogo import MenuEmJogo
from prototipo import som
from prototipo.hud import hud
from time import sleep


class SpritesSala(SpritesCena):
    def __init__(self):
        super().__init__()
        self.televisao_sprite = self.load_image("../Assets/Sprites/cenario/television.png", True)
        self.NPFerramenta = self.load_image("../Assets/Sprites/cenario/NPFerramenta.png", True)
        self.porta_corredor = self.load_image("../Assets/Sprites/cenario/porta_metal.png", True)
        self.NPCodigo = self.load_image("../Assets/Sprites/hud/NPCodigo.png", True)


spritesSala = SpritesSala()


class ColisaoSala(Colisao):
    def __init__(self):
        super().__init__()

    def construir_cenario(self):
        self.construir_objeto(spritesSala.parede_sprite_h, 0, 0, "sala", 5, adicionalY=-30) # Parede cima

        self.construir_objeto(spritesSala.parede_sprite_v, 774, 26, "sala", 8, "vertical")  # Parede direita 1.
        self.construir_objeto(spritesSala.parede_sprite_v, 774, 300, "sala", 12, "vertical")  # Parede direita 2.
        self.construir_objeto(spritesSala.parede_sprite_v, 0, 1, "sala", 24, "vertical")  # Parede esquerda.
        self.construir_objeto(spritesSala.parede_sprite_vh, 0, 574, "sala", 7)  # Parede inferior 1.
        self.construir_objeto(spritesSala.parede_sprite_vh, 252, 574, "sala", 21)  # Parede inferior 2.
        self.construir_objeto(spritesSala.televisao_sprite, 250, 75, "sala", 1, identificacao="televisao", adicionalY=-25)
        self.construir_objeto(spritesSala.porta_corredor, 450, 28, "sala", 1, identificacao="porta_metal", adicionalY=-30)


colisao = ColisaoSala()


class Sala(Cena):
    possui_ferramenta_sala = False
    possui_codigo = False

    def __init__(self):
        super().__init__()
        self.teclaHorizontal = ""
        self.teclaVertical = ""
        self.cenaJogavel = True
        colisao.construir_cenario()
        self.puzzle = ["esquerda", "cima", "cima"]

    def iniciar(self):
        print("iniciou sala")
        if glob.cenaAtual == "saguao":
            jogador.rect.topleft = (200, 545)
        elif glob.cenaAtual == "corredor":
            jogador.rect.topleft = (450, 60)
        glob.cenaAtual = "sala"

        self.delay = 10
        self.iniciou = True


    def eventos(self):  # Captura os eventos do teclado e do cenário.
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, colisao.get_colisao_jogador("sala"))
        # controlador.movimenta()
        # colisao.colisao_monstro()

        if self.delay > 0:
            self.delay -= 1

        if self.tecla == "p":
            MenuEmJogo.cena_anterior = "sala"
            return "menuEmJogo"
        if self.tecla == "i":
            MenuEmJogo.cena_anterior = "sala"
            return "inventario"
        elif self.tecla == "e":
            if colisao.distancia(jogador, 220, 585) < 50 and self.delay <= 0:
                self.iniciou = False
                som.porta_som.play()
                return "saguao"

            # interagir televisao
            if colisao.distancia(jogador, 270, 92) < 50 and self.delay <= 0:
                if Sala.possui_ferramenta_sala:
                    pass # inserir fio de cobre no inventario se possuir ferramenta.
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    som.pegar_item.play()
                else:
                    glob.tela.fill((glob.preto))
                    glob.tela.blit(spritesSala.NPFerramenta, spritesSala.NPFerramenta.get_rect(center = glob.tela.get_rect().center))
                    pygame.display.flip()
                    sleep(2)

            # porta corredor
            if colisao.distancia(jogador, 455, 80) < 50 and self.delay <= 0:
                if Sala.possui_codigo:
                    pass # destranca a porta se possuir o codigo.
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    som.puzzle_cozinha.play()
                else:
                    glob.tela.fill((glob.preto))
                    glob.tela.blit(spritesSala.NPCodigo, spritesSala.NPCodigo.get_rect(center = glob.tela.get_rect().center))
                    pygame.display.flip()
                    sleep(2)

    def desenhar_objetos_externos(self):
        jogadorGroup.draw(glob.tela)
        glob.tela.blit(spritesSala.sprite_iluminacao, (jogador.rect.center[0] - 1200, jogador.rect.center[1] - 900))
        hud.desenhar_hud(jogador.stamina, jogador.vida, jogador.rect.center[0] - 30, jogador.rect.top - 30,
                         self.mostrarVida)
        jogadorGroup.update()

    def atualizar(self):  # Atualiza os sprites da cena.
        glob.tela.blit(spritesSala.fundo, (0, 0))
        colisao.desenhar_objetos("sala")
        self.desenhar_objetos_externos()
