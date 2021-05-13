from prototipo.cenas.cena import Cena
from prototipo.personagens import *
from prototipo.controladorInimigo import *
from prototipo.cenas.colisao import Colisao
from prototipo.cenas.sprites import SpritesCena
from prototipo.cenas.menu_em_jogo import MenuEmJogo


class SpritesSaguao(SpritesCena):  # Classe que armazena os sprites da cena.
    def __init__(self):
        super().__init__()
        self.estatua_sprite = self.load_image("../Assets/Sprites/cenario/estatua.png", True)
        self.vela_sprite = self.load_image("../Assets/Sprites/cenario/vela.png", True)
        self.porao_sprite = self.load_image("../Assets/Sprites/cenario/porta_porao.png")


spritesSaguao = SpritesSaguao()


class ColisaoSaguao(Colisao):  # Classe responsável por construir os objetos do cenário e suas colisões.

    def __init__(self):
        super().__init__()
        self.temMonstro = False

    def construir_cenario(self):

        self.construir_objeto(spritesSaguao.parede_sprite_h, 0, 0, "saguao", 5, adicionalY=-30)  # Parede horizontal superior
        self.construir_objeto(spritesSaguao.parede_sprite_v, 0, 26, "saguao", 10, "vertical")  # Parede esquerda 1
        #self.construir_objeto(spritesSaguao.parede_sprite_v, 0, 280, "saguao", 3, "vertical", identificacao="portaCozinha")  # Porta para a cozinha.
        self.construir_objeto(spritesSaguao.parede_sprite_v, 0, 350, "saguao", 10, "vertical")  # Parede esquerda 2
        self.construir_objeto(spritesSaguao.parede_sprite_v, 774, 26, "saguao", 30, "vertical")  # Parede direita
        self.construir_objeto(spritesSaguao.parede_sprite_vh, 0, 574, "saguao", 35)  # Parede inferior.
        self.construir_objeto(spritesSaguao.estatua_sprite, 350, 250, "saguao")
        self.construir_objeto(spritesSaguao.vela_sprite, 380, 80, "saguao", identificacao="vela")


colisao = ColisaoSaguao()


class Saguao(Cena):
    def __init__(self):  # É executado apenas na instanciação da cena.
        super().__init__()
        self.teclaHorizontal = ""
        self.teclaVertical = ""
        self.cenaJogavel = True
        self.velaVirada = False
        jogador.rect.topleft = (375, 550)
        colisao.construir_cenario()

    def iniciar(self):  # É executado 1 vez sempre que a cena é chamada.
        print("iniciou saguao")
        MenuEmJogo.cena_anterior = "saguao"
        if glob.cenaAtual == "inicio":
            jogador.rect.topleft = (375, 520)
        glob.cenaAtual = "saguao"

        self.delay = 10
        self.iniciou = True

    def eventos(self):  # Captura os eventos do teclado e do cenário.
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, colisao.get_colisao_jogador("saguao"))
        #controlador.movimenta()
        #colisao.colisao_monstro()

        if self.delay > 0:
            self.delay -= 1

        if self.tecla == "p":
            colisao.destruir_objeto("portaCozinha")
            MenuEmJogo.cena_anterior = "saguao"
            return "menuEmJogo"
        elif self.tecla == "i":
            MenuEmJogo.cena_anterior = "saguao"
            return "inventario"
        elif self.tecla == "e":
            # Acionar a vela
            if colisao.distancia(jogador, 380, 100) < 50:
                colisao.destruir_objeto("vela")
                vela_sprite = pygame.transform.rotate(spritesSaguao.vela_sprite, 270)
                colisao.construir_objeto(vela_sprite, 380, 80, "saguao")
                colisao.construir_objeto(spritesSaguao.porao_sprite, 650, 35, "saguao", adicionalY=-30)
                self.velaVirada = True
                glob.vela.play()

            # Entrar no porão
            elif colisao.distancia(jogador, 650, 100) < 50 and self.delay <= 0 and self.velaVirada:
                self.iniciou = False
                glob.passos.play()
                return "porao"
            elif colisao.distancia(jogador, 0, 280) < 50 and self.delay <= 0:
                self.iniciou = False
                glob.porta_som.play()
                return "cozinha"

    def atualizar(self):  # Atualiza os sprites da cena.
        glob.tela.blit(spritesSaguao.fundo, (0, 0))
        colisao.desenhar_objetos("saguao")
        jogadorGroup.draw(glob.tela)
        glob.tela.blit(spritesSaguao.sprite_iluminacao, (jogador.rect.center[0] - 1200, jogador.rect.center[1] - 900))
        jogadorGroup.update()



