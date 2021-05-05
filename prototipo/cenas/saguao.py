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
        jogador.rect.topleft = (500, 500)
        inimigo.rect.right = 300
        self.iniciou = True

    def eventos(self):
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical, self.lista_colisoes_jogador)
        controlador.movimenta()
        colisao.colisao_monstro()

        if self.tecla == "p":
            return "menuEmJogo"
        elif self.tecla == "e":
            return "inventario"

    def atualizar(self):
        glob.tela.blit(self.fundo, (0, 0))
        colisao.desenhar_paredes()
        draw_groups()
        update_groups()


class ColisaoSaguao(Colisao):

    def __init__(self):
        self.parede_sprite_h = pygame.image.load("../Assets/Sprites/cenario/parede_horizontal.png")
        self.parede_sprite_v = pygame.image.load("../Assets/Sprites/cenario/parede_vertical.png")
        self.x = []
        self.y = []
        self.orientacao = []
        self.parede_rect = []
        self.construir_cenario()

    def draw(self):
        pass

    def construir_cenario(self):
        self.construir_parede_horizontal(0, 0, 5)
        self.construir_parede_vertical(0, 26, 30)
        self.construir_parede_vertical(774, 26, 30)

    def construir_parede_horizontal(self, x, y, quantidade):
        for i in range(quantidade):
            self.x.append(x + (i*183))
            self.y.append(y)
            self.orientacao.append("horizontal")
            self.parede_rect.append(self.parede_sprite_h.get_rect(topleft=(self.x[-1], self.y[-1])))

    def construir_parede_vertical(self, x, y, quantidade):
        for i in range(quantidade):
            self.x.append(x)
            self.y.append(y + (i*26))
            self.orientacao.append("vertical")
            self.parede_rect.append(self.parede_sprite_v.get_rect(topleft=(self.x[-1], self.y[-1])))

    def desenhar_paredes(self):
        for i, orientacao in enumerate(self.orientacao):
            if orientacao == "horizontal":
                glob.tela.blit(self.parede_sprite_h, (self.x[i], self.y[i]))
            elif orientacao == "vertical":
                glob.tela.blit(self.parede_sprite_v, (self.x[i], self.y[i]))

    def get_colisao_jogador(self):
        colisoes_jogador = self.parede_rect.copy()
        colisoes_jogador.append(inimigo.rect)
        return colisoes_jogador

    def get_colisao_monstro(self):
        return self.parede_rect

    def colisao_monstro(self):
        for retangulo in self.parede_rect:
            if inimigo.rect.colliderect(retangulo):
                inimigo.resgata_posicao()

        if inimigo.movimento_falhou:
            controlador.movimenta_x()
            for retangulo in self.parede_rect:
                if inimigo.rect.colliderect(retangulo):
                    inimigo.resgata_posicao()
        if inimigo.movimento_falhou:
            controlador.movimenta_y()
            for retangulo in self.parede_rect:
                if inimigo.rect.colliderect(retangulo):
                    inimigo.resgata_posicao()

        if inimigo.rect.colliderect(jogador.rect):
            inimigo.resgata_posicao()


colisao = ColisaoSaguao()
