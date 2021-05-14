from prototipo.cenas.cena import Cena
from prototipo.personagens import *
from prototipo.controladorInimigo import *
from prototipo.cenas.colisao import Colisao
from prototipo.cenas.sprites import SpritesCena
from prototipo.cenas.menu_em_jogo import MenuEmJogo
from prototipo import som


class SpritesInicio(SpritesCena):  # Classe que armazena os sprites da cena.
    def __init__(self):
        super().__init__()
        self.parede_invisivel = pygame.image.load("../Assets/Sprites/cenario/parede_invisivel.png")

spritesInicio = SpritesInicio()

class ColisaoInicio(Colisao):  # Classe responsável por construir os objetos do cenário e suas colisões.

    def __init__(self):
        super().__init__()
        self.temMonstro = False

    def construir_cenario(self):
        self.construir_objeto(spritesInicio.parede_invisivel, 320, 400, "inicio", 9, "vertical", 26, "ini0")
        self.construir_objeto(spritesInicio.parede_invisivel, 456, 400, "inicio", 9, "vertical", 26, "ini1")
        self.construir_objeto(spritesInicio.parede_invisivel, 428, 375, "inicio", 2, "horizontal", 26, "ini2")
        self.construir_objeto(spritesInicio.parede_invisivel, 319, 375, "inicio", 2, "horizontal", 26, "ini3")
        self.construir_objeto(spritesInicio.parede_invisivel, 350, 350, "inicio", 4, "horizontal", 26, "ini4")


colisao = ColisaoInicio()


class Inicio(Cena):  # Primeira cena do jogo.
    def __init__(self):  # É executado apenas na instanciação da cena.
        super().__init__()
        self.cenaJogavel = True
        jogador.rect.topleft = (375, 550)
        colisao.construir_cenario()

    def iniciar(self):  # É executado 1 vez sempre que a cena é chamada.
        glob.cenaAtual = "inicio"

        self.delay = 10
        self.iniciou = True

    def eventos(self):  # Captura os eventos do teclado e do cenário.
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, colisao.get_colisao_jogador("inicio"))

        if self.delay > 0:
            self.delay -= 1

        if self.tecla == "p":
            MenuEmJogo.cena_anterior = "inicio"
            return "menuEmJogo"
        elif self.tecla == "i":
            MenuEmJogo.cena_anterior = "inicio"
            return "inventario"
        elif self.tecla == "e":
            # Entrar na casa
            if colisao.distancia(jogador, 410, 400) < 50 and self.delay <= 0:
                self.iniciou = False
                som.porta_som.play()
                return "saguao"

    def atualizar(self):  # Atualiza os sprites da cena.
        glob.tela.blit(spritesInicio.fundo_inicio, (0, 0))
        colisao.desenhar_objetos("inicio")
        jogadorGroup.draw(glob.tela)
        jogadorGroup.update()



