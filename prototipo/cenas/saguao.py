from prototipo.cenas.cena import Cena
from prototipo.personagens import *
from prototipo.controladorInimigo import *
from prototipo.cenas.colisao import Colisao


class Saguao(Cena):
    def __init__(self):
        super().__init__()
        self.teclaHorizontal = ""
        self.teclaVertical = ""
        self.fundo = pygame.image.load("../Assets/Sprites/cenario/chaoGrande.png")
        self.cenaJogavel = True
        self.lista_colisoes_monstro = colisao.get_colisao_monstro()
        self.lista_colisoes_jogador = colisao.get_colisao_jogador()

    def iniciar(self):
        print("iniciou")
        jogador.rect.topleft = (375, 550)
        #inimigo.rect.right = 300
        self.iniciou = True

    def eventos(self):
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, self.lista_colisoes_jogador)
        #controlador.movimenta()
        #colisao.colisao_monstro()

        if self.tecla == "p":
            return "menuEmJogo"
        elif self.tecla == "e":
            return "inventario"

    def atualizar(self):
        glob.tela.blit(self.fundo, (0, 0))
        colisao.desenhar_paredes()
        colisao.desenhar_objetos()
        jogadorGroup.draw(glob.tela)
        jogadorGroup.update()


class ColisaoSaguao(Colisao):

    def __init__(self):
        super().__init__()
        self.temMonstro = False

    def construir_cenario(self):
        estatua_sprite = pygame.image.load("../Assets/Sprites/cenario/estatua.png")
        self.construir_parede("horizontal", 0, 0, 5)
        self.construir_parede("vertical", 0, 26, 30)
        self.construir_parede("vertical", 774, 26, 30)
        self.construir_objeto(estatua_sprite, 350, 250)


colisao = ColisaoSaguao()
