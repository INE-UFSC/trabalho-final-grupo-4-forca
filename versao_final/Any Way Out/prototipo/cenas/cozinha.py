from prototipo.cenas.cena import Cena
from prototipo.variaveisGlobais import glob
from prototipo.cenas.colisao import Colisao
from prototipo.cenas.sprites import SpritesCena
from prototipo.personagens import *
from prototipo.cenas.menu_em_jogo import MenuEmJogo
from prototipo import som
from prototipo.hud import hud
from prototipo.cenas.saguao import Saguao
from time import sleep


class SpritesCozinha(SpritesCena):
    def __init__(self):
        super().__init__()
        self.sprite_cadeira_direita = self.load_image("Assets/Sprites/cenario/cadeiradireita.png", True)
        self.sprite_cadeira_esquerda = self.load_image("Assets/Sprites/cenario/cadeiraesquerda.png", True)
        self.sprite_cadeira_cima = self.load_image("Assets/Sprites/cenario/cadeiracima.png", True)
        self.sprite_cadeira_baixo = self.load_image("Assets/Sprites/cenario/cadeirabaixo.png", True)
        self.sprite_forno = self.load_image("Assets/Sprites/cenario/forno.png", True)
        self.sprite_geladeira = self.load_image("Assets/Sprites/cenario/geladeira.png", True)
        self.sprite_pia = self.load_image("Assets/Sprites/cenario/pia.png", True)
        self.sprite_prato = self.load_image("Assets/Sprites/cenario/prato.png", True)
        self.sprite_garrafa = self.load_image("Assets/Sprites/cenario/garrafavinho.png", True)
        self.NPFerramenta = self.load_image("Assets/Sprites/hud/NPFerramenta2.png", True)
        self.pegou_cobre = self.load_image("Assets/Sprites/hud/pegou_cobre.png", True)
        self.pegou_codigo = self.load_image("Assets/Sprites/hud/pegou_codigo.png", True)


spritesCozinha = SpritesCozinha()


class ColisaoCozinha(Colisao):
    def __init__(self):
        super().__init__()
    
    def construir_cenario(self):
        self.construir_objeto(spritesCozinha.parede_sprite_h, 0, 0, "cozinha", 5, adicionalY=-30)

        self.construir_objeto(spritesCozinha.parede_sprite_v, 774, 26, "cozinha", 10, "vertical")  # Parede direita 1.
        #self.construir_objeto(spritesCozinha.parede_sprite_v, 774, 280, "cozinha", 3, "vertical", identificacao="portaSaguao")  # Porta para o saguão.
        self.construir_objeto(spritesCozinha.parede_sprite_v, 774, 350, "cozinha", 10, "vertical")  # Parede direita 2.

        self.construir_objeto(spritesCozinha.parede_sprite_v, 0, 1, "cozinha", 24, "vertical")  # Parede esquerda.

        self.construir_objeto(spritesCozinha.parede_sprite_vh, 0, 574, "cozinha", 14)  # Parede inferior 1.
        #self.construir_objeto(spritesCozinha.parede_sprite_vh, 364, 574, "cozinha", 3, identificacao="portaArmazem")
        self.construir_objeto(spritesCozinha.parede_sprite_vh, 442, 574, "cozinha", 14)  # Parede inferior 2.

        self.construir_objeto(spritesCozinha.sprite_cadeira_cima, 360, 205, "cozinha", 1, identificacao = "cadeiracima")
        self.construir_objeto(spritesCozinha.sprite_cadeira_esquerda, 280, 250, "cozinha", 1, identificacao = "cadeiraesquerda")
        self.construir_objeto(spritesCozinha.sprite_cadeira_cima, 440, 250, "cozinha", 1, identificacao = "cadeiradireita")
        self.construir_objeto(spritesCozinha.sprite_mesa, 320, 250, "cozinha", 1, identificacao = "mesa")
        self.construir_objeto(spritesCozinha.sprite_geladeira, 60,40, "cozinha", 1, identificacao = "geladeira", adicionalY=-28)
        self.construir_objeto(spritesCozinha.sprite_forno, 250, 100, "cozinha", 3, identificacao = "forno", adicionalY=-20)
        self.construir_objeto(spritesCozinha.sprite_pia, 495, 100, "cozinha", identificacao = "pia", adicionalY=-20)
        self.construir_objeto(spritesCozinha.sprite_prato, 510, 105, "cozinha")
        self.construir_objeto(spritesCozinha.sprite_prato, 615, 300, "cozinha")
        self.construir_objeto(spritesCozinha.sprite_prato, 550, 450, "cozinha")
        self.construir_objeto(spritesCozinha.sprite_prato, 730, 530, "cozinha")
        self.construir_objeto(spritesCozinha.sprite_garrafa, 100, 250, "cozinha")
        self.construir_objeto(spritesCozinha.sprite_garrafa, 250, 400, "cozinha")
        self.construir_objeto(spritesCozinha.sprite_garrafa, 50, 500, "cozinha")


colisao = ColisaoCozinha()


class Cozinha(Cena):

    def __init__(self):
        super().__init__()
        self.temMonstro = False
        self.cenaJogavel = True
        colisao.construir_cenario()
        self.puzzle = ["esquerda", "cima", "cima"]


    def iniciar(self):
        print("iniciou cozinha")
        if glob.cenaAtual == "saguao":
            jogador.rect.topleft = (770, 300)
        elif glob.cenaAtual == "armazem":
            jogador.rect.topleft = (375, 570)
        glob.cenaAtual = "cozinha"

        self.delay = 10
        self.iniciou = True
    
    def muda_puzzle(self, cadeira):
        if cadeira == "esquerda":
            self.puzzle[0] = self.acha_posicao(self.puzzle[0])
            colisao.destruir_objeto("cadeiraesquerda")
            colisao.destruir_objeto("mesa")
            self.constroi_objeto("esquerda")
            colisao.construir_objeto(spritesCozinha.sprite_mesa, 320, 250, "cozinha", 1, identificacao = "mesa")
        elif cadeira == "cima":
            self.puzzle[1] = self.acha_posicao(self.puzzle[1])
            colisao.destruir_objeto("cadeiracima")
            colisao.destruir_objeto("mesa")
            self.constroi_objeto("cima")
            colisao.construir_objeto(spritesCozinha.sprite_mesa, 320, 250, "cozinha", 1, identificacao = "mesa")
        elif cadeira == "direita":
            self.puzzle[2] = self.acha_posicao(self.puzzle[2])
            colisao.destruir_objeto("cadeiradireita")
            colisao.destruir_objeto("mesa")
            self.constroi_objeto("direita")
            colisao.construir_objeto(spritesCozinha.sprite_mesa, 320, 250, "cozinha", 1, identificacao = "mesa")

    def constroi_objeto(self, cadeira):
        if cadeira == "esquerda":
            if self.puzzle[0] == "esquerda":
                colisao.construir_objeto(spritesCozinha.sprite_cadeira_esquerda, 280, 250, "cozinha", 1, identificacao = "cadeiraesquerda")
            elif self.puzzle[0] == "cima":
                colisao.construir_objeto(spritesCozinha.sprite_cadeira_cima, 280, 250, "cozinha", 1, identificacao = "cadeiraesquerda")
            elif self.puzzle[0] == "direita":
                colisao.construir_objeto(spritesCozinha.sprite_cadeira_direita, 280, 250, "cozinha", 1, identificacao = "cadeiraesquerda")
            elif self.puzzle[0] == "baixo":
                colisao.construir_objeto(spritesCozinha.sprite_cadeira_baixo, 280, 250, "cozinha", 1, identificacao = "cadeiraesquerda")
        
        elif cadeira == "cima":
            if self.puzzle[1] == "esquerda":
                colisao.construir_objeto(spritesCozinha.sprite_cadeira_esquerda, 360, 205, "cozinha", 1, identificacao = "cadeiracima")
            elif self.puzzle[1] == "cima":
                colisao.construir_objeto(spritesCozinha.sprite_cadeira_cima, 360, 205, "cozinha", 1, identificacao = "cadeiracima")
            elif self.puzzle[1] == "direita":
                colisao.construir_objeto(spritesCozinha.sprite_cadeira_direita, 360, 205, "cozinha", 1, identificacao = "cadeiracima")
            elif self.puzzle[1] == "baixo":
                colisao.construir_objeto(spritesCozinha.sprite_cadeira_baixo, 360, 205, "cozinha", 1, identificacao = "cadeiracima")
        elif cadeira == "direita":
            if self.puzzle[2] == "esquerda":
                colisao.construir_objeto(spritesCozinha.sprite_cadeira_esquerda, 440, 250, "cozinha", 1, identificacao = "cadeiradireita")
            elif self.puzzle[2] == "cima":
                colisao.construir_objeto(spritesCozinha.sprite_cadeira_cima, 440, 250, "cozinha", 1, identificacao = "cadeiradireita")
            elif self.puzzle[2] == "direita":
                colisao.construir_objeto(spritesCozinha.sprite_cadeira_direita, 440, 250, "cozinha", 1, identificacao = "cadeiradireita")
            elif self.puzzle[2] == "baixo":
                colisao.construir_objeto(spritesCozinha.sprite_cadeira_baixo, 440, 250, "cozinha", 1, identificacao = "cadeiradireita")
    
    def acha_posicao(self, posicao):
        if posicao == "esquerda":
            return "cima"
        elif posicao == "cima":
            return "direita"
        elif posicao == "direita":
            return "baixo"
        elif posicao == "baixo":
            return "esquerda"

    def eventos(self):  # Captura os eventos do teclado e do cenário.
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, colisao.get_colisao_jogador("cozinha"))
        #controlador.movimenta()
        #colisao.colisao_monstro()

        if self.delay > 0:
            self.delay -= 1

        if self.tecla == "p":
            MenuEmJogo.cena_anterior = "cozinha"
            return "menuEmJogo"
        if self.tecla == "i":
            MenuEmJogo.cena_anterior = "cozinha"
            return "inventario"
        elif self.tecla == "e":
            if colisao.distancia(jogador, 380, 190) < 40 and self.delay <= 0:
                self.muda_puzzle("cima")
                self.delay = 20
                if self.puzzle == ['direita', 'baixo', 'esquerda']:
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    som.puzzle_cozinha.play()
                    Saguao.porta_sala = True
            elif colisao.distancia(jogador, 280, 260) < 40 and self.delay <= 0:
                self.muda_puzzle("esquerda")
                self.delay = 20
                if self.puzzle == ['direita', 'baixo', 'esquerda']:
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    som.puzzle_cozinha.play()
                    Saguao.porta_sala = True
            elif colisao.distancia(jogador, 480, 260) < 40 and self.delay <= 0:
                self.delay = 20
                self.muda_puzzle("direita")
                if self.puzzle == ['direita', 'baixo', 'esquerda']:
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    som.puzzle_cozinha.play()
                    Saguao.porta_sala = True
            elif colisao.distancia(jogador, 800, 280) < 50 and self.delay <= 0:
                self.iniciou = False
                som.porta_som.play()
                return "saguao"
            elif colisao.distancia(jogador, 375, 600) < 50 and self.delay <= 0:
                self.iniciou = False
                som.porta_som.play()
                return "armazem"

            if colisao.distancia(jogador, 95, 145) < 35 and self.delay <= 0 and not item.cobre2:
                if item.possui_ferramenta_cozinha:
                    item.cobre2 = True
                    item.possui_codigo = True
                    jogador.adiciona_item(itens.cobre)
                    jogador.adiciona_item(itens.codigo)
                    som.pegar_item.play()
                    glob.tela.fill((glob.preto))
                    glob.tela.blit(spritesCozinha.pegou_cobre, spritesCozinha.pegou_cobre.get_rect(center=glob.tela.get_rect().center))
                    pygame.display.flip()
                    sleep(2)
                    som.pegar_item.play()
                    glob.tela.fill((glob.preto))
                    glob.tela.blit(spritesCozinha.pegou_codigo, spritesCozinha.pegou_codigo.get_rect(center=glob.tela.get_rect().center))
                    pygame.display.flip()
                    sleep(4)
                else:
                    glob.tela.fill((glob.preto))
                    glob.tela.blit(spritesCozinha.NPFerramenta, spritesCozinha.NPFerramenta.get_rect(center = glob.tela.get_rect().center))
                    pygame.display.flip()
                    sleep(2)

    def desenhar_objetos_externos(self):
        jogadorGroup.draw(glob.tela)
        glob.tela.blit(spritesCozinha.sprite_iluminacao, (jogador.rect.center[0] - 1200, jogador.rect.center[1] - 900))
        hud.desenhar_hud(jogador.stamina, jogador.vida, jogador.rect.center[0] - 30, jogador.rect.top - 30,
                         self.mostrarVida)
        jogadorGroup.update()

    def atualizar(self):  # Atualiza os sprites da cena.
        glob.tela.blit(spritesCozinha.fundo, (0, 0))
        colisao.desenhar_objetos("cozinha")
        self.desenhar_objetos_externos()
