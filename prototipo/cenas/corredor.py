from prototipo.cenas.cena import Cena
from prototipo.personagens import *
from prototipo.controladorInimigo import *
from prototipo.cenas.colisao import Colisao
from prototipo.cenas.sprites import SpritesCena
from prototipo.cenas.menu_em_jogo import MenuEmJogo
from prototipo import itens
from prototipo import som
from prototipo.hud import hud


class SpritesCorredor(SpritesCena):  # Classe que armazena os sprites da cena.
    def __init__(self):
        super().__init__()
        self.porta_corredor = self.load_image("../Assets/Sprites/cenario/porta_metal.png", True)

spritesCorredor = SpritesCorredor()


class ColisaoCorredor(Colisao):  # Classe responsável por construir os objetos do cenário e suas colisões.

    def __init__(self):
        super().__init__()
        self.temMonstro = False

    def construir_cenario(self):
        self.construir_objeto(spritesCorredor.parede_sprite_h, 0, 0, "corredor", 5, adicionalY=-30)  # Parede horizontal superior
        self.construir_objeto(spritesCorredor.parede_sprite_v, 300, 26, "corredor", 30, "vertical")  # Parede esquerda 1
        self.construir_objeto(spritesCorredor.parede_sprite_v, 500, 26, "corredor", 30, "vertical")  # Parede direita
        self.construir_objeto(spritesCorredor.parede_sprite_vh, 0, 574, "corredor", 35)  # Parede inferior.
        self.construir_objeto(spritesCorredor.porta_corredor, 380, 28, "corredor", 1, identificacao="porta_final", adicionalY=-30)


colisao = ColisaoCorredor()


class Corredor(Cena):
    porta_sala = False

    def __init__(self):  # É executado apenas na instanciação da cena.
        super().__init__()
        self.teclaHorizontal = ""
        self.teclaVertical = ""
        self.cenaJogavel = True
        self.velaVirada = False
        jogador.rect.topleft = (400, 530)
        colisao.construir_cenario()

    def iniciar(self):  # É executado 1 vez sempre que a cena é chamada.
        print("iniciou corredor")
        MenuEmJogo.cena_anterior = "corredor"
        if glob.cenaAtual == "sala":
            jogador.rect.topleft = (400, 530)
        glob.cenaAtual = "corredor"

        self.delay = 10
        self.iniciou = True

    def eventos(self):  # Captura os eventos do teclado e do cenário.
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, colisao.get_colisao_jogador("corredor"))
        #controlador.movimenta()
        #colisao.colisao_monstro()

        if self.delay > 0:
            self.delay -= 1

        if self.tecla == "p":
            colisao.destruir_objeto("portaCozinha")
            MenuEmJogo.cena_anterior = "corredor"
            return "menuEmJogo"
        elif self.tecla == "i":
            MenuEmJogo.cena_anterior = "corredor"
            return "inventario"
        elif self.tecla == "e":
            # Entrar na sala
            if colisao.distancia(jogador, 400, 570) < 50 and self.delay <= 0:
                self.iniciou = False
                som.porta_som.play()
                return "sala"

        if self.tecla == "e" and self.delay <= 0:
            self.mostrarVida = True
        else:
            self.mostrarVida = False

    def desenhar_objetos_externos(self):
        jogadorGroup.draw(glob.tela)
        glob.tela.blit(spritesCorredor.sprite_iluminacao, (jogador.rect.center[0] - 1200, jogador.rect.center[1] - 900))
        hud.desenhar_hud(jogador.stamina, jogador.vida, jogador.rect.center[0] - 30, jogador.rect.top - 30,
                         self.mostrarVida)
        jogadorGroup.update()

    def atualizar(self):  # Atualiza os sprites da cena.
        glob.tela.blit(spritesCorredor.fundo, (0, 0))
        colisao.desenhar_objetos("corredor")
        self.desenhar_objetos_externos()
