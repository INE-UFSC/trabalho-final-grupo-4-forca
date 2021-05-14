from prototipo.cenas.cena import Cena
from prototipo.variaveisGlobais import glob
from prototipo.cenas.colisao import Colisao
from prototipo.cenas.sprites import SpritesCena
from prototipo.personagens import *
from prototipo.cenas.menu_em_jogo import MenuEmJogo


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
spritesArmazem = SpritesArmazem()

class ColisaoArmazem(Colisao):
    def __init__(self):
        super().__init__()
    
    def construir_cenario(self):
        self.construir_objeto(spritesArmazem.sprite_mesa, 26, 220, "armazem")
        self.construir_objeto(spritesArmazem.parede_sprite_h, 0, 0, "armazem", 5)
        self.construir_objeto(spritesArmazem.parede_sprite_v, 0, 1, "armazem", 24, orientacao = "vertical")
        self.construir_objeto(spritesArmazem.parede_sprite_v, 774, 1, "armazem", 24, orientacao = "vertical")
        self.construir_objeto(spritesArmazem.sprite_caixa, 620, 120, "armazem")
        self.construir_objeto(spritesArmazem.sprite_caixa, 550, 200, "armazem")
        self.construir_objeto(spritesArmazem.sprite_caixa, 680, 240, "armazem")
        self.construir_objeto(spritesArmazem.sprite_caixa, 450, 120, "armazem")
        self.construir_objeto(spritesArmazem.sprite_machado, 30, 250, "armazem")
        self.construir_objeto(spritesArmazem.sprite_martelo, 30, 290, "armazem")
        self.construir_objeto(spritesArmazem.sprite_vassoura, 60, 20, "armazem", 3)
        self.construir_objeto(spritesArmazem.sprite_barril, 100, 140, "armazem", 3)
        self.construir_objeto(spritesArmazem.sprite_barril, 100, 176, "armazem", 3)
        self.construir_objeto(spritesArmazem.sprite_parede_vh, 384, 400, "armazem", 15)
        self.construir_objeto(spritesArmazem.sprite_bau, 600, 426, "armazem")
        

colisao = ColisaoArmazem()

class Armazem(Cena):
    def __init__(self):
        super().__init__()
        self.cenaJogavel = True

    def iniciar(self): 
        print("iniciou porao")
        if glob.cenaAtual == "armazem":
            jogador.rect.topleft = (500, 550)
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
        

    def atualizar(self):
        glob.tela.blit(spritesArmazem.fundo, (0, 0))
        colisao.desenhar_objetos("armazem")
        jogadorGroup.draw(glob.tela)
        jogadorGroup.update()
