from prototipo.cenas.cena import Cena
from prototipo.personagens import *
from prototipo.controladorInimigo import *
from prototipo.cenas.colisao import Colisao


class SpritesSaguao:
    def __init__(self):
        self.fundo = pygame.image.load("../Assets/Sprites/cenario/chaoGrande.png")
        self.estatua_sprite = pygame.image.load("../Assets/Sprites/cenario/estatua.png")
        self.vela_sprite = pygame.image.load("../Assets/Sprites/cenario/vela.png")
        self.porao_sprite = pygame.image.load("../Assets/Sprites/cenario/porta_porao.png")


spritesSaguao = SpritesSaguao()


class Saguao(Cena):
    def __init__(self):
        super().__init__()
        self.teclaHorizontal = ""
        self.teclaVertical = ""
        self.cenaJogavel = True
        self.velaVirada = False
        jogador.rect.topleft = (375, 550)

    def iniciar(self):
        print("iniciou")
        self.delay = 10
        self.iniciou = True

    def eventos(self):
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, colisao.get_colisao_jogador())
        #controlador.movimenta()
        #colisao.colisao_monstro()

        if self.delay > 0:
            self.delay -= 1

        if self.tecla == "p":
            colisao.destruir_objeto("portaCozinha")
            return "menuEmJogo"
        elif self.tecla == "i":
            return "inventario"
        elif self.tecla == "e":
            # Acionar a vela
            if colisao.distancia(jogador, 380, 100) < 50:
                colisao.destruir_objeto("vela")
                vela_sprite = pygame.transform.rotate(spritesSaguao.vela_sprite, 270)
                colisao.construir_objeto(vela_sprite, 380, 100)
                colisao.construir_objeto(spritesSaguao.porao_sprite, 650, 35)

            # Entrar no porão
            elif colisao.distancia(jogador, 650, 100) < 50 and self.delay <= 0:
                self.iniciou = False
                return "porao"

    def atualizar(self):
        glob.tela.blit(spritesSaguao.fundo, (0, 0))
        colisao.desenhar_objetos()
        jogadorGroup.draw(glob.tela)
        jogadorGroup.update()


class ColisaoSaguao(Colisao):

    def __init__(self):
        super().__init__()
        self.temMonstro = False

    def construir_cenario(self):

        self.construir_objeto(self.parede_sprite_h, 0, 0, 5)  # Parede horizontal superior
        self.construir_objeto(self.parede_sprite_v, 0, 26, 10, "vertical")  # Parede esquerda 1
        self.construir_objeto(self.parede_sprite_v, 0, 280, 3, "vertical", identificacao="portaCozinha")  # Porta cozinha
        self.construir_objeto(self.parede_sprite_v, 0, 350, 10, "vertical")  # Parede esquerda 2
        self.construir_objeto(self.parede_sprite_v, 774, 26, 30, "vertical")  # Parede direita
        self.construir_objeto(spritesSaguao.estatua_sprite, 350, 250)
        self.construir_objeto(spritesSaguao.vela_sprite, 380, 100, identificacao="vela")


colisao = ColisaoSaguao()
