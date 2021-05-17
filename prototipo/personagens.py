import pygame
import itens
from itens import item
from variaveisGlobais import glob


class Personagem(pygame.sprite.Sprite):

    def __init__(self, largura, altura, *groups):
        super().__init__(*groups)
        self.largura = largura
        self.altura = altura
        self.surf = pygame.Surface((self.largura, self.altura))
        self.imagesIdle = [None, None, None, None, None]
        self.imagesRun = [None, None, None, None, None]
        self.image = self.imagesIdle[0]
        self.rect = self.surf.get_rect(topleft=(0, 0))
        self.coordant = self.rect.topleft
        self.velocidade = 1.5
        self.estado = ""
        self.imageIndex = 0
        self.ultimaDirecaoH = "direita"

    def move(self):
        pass


class Jogador(Personagem):

    def __init__(self, largura, altura, *groups):
        super().__init__(largura, altura, *groups)

        self.imagesIdle[0] = pygame.image.load("../Assets/Sprites/jogador/playerIdle0.png")
        self.imagesIdle[1] = pygame.image.load("../Assets/Sprites/jogador/playerIdle1.png")
        self.imagesIdle[2] = pygame.image.load("../Assets/Sprites/jogador/playerIdle2.png")
        self.imagesIdle[3] = pygame.image.load("../Assets/Sprites/jogador/playerIdle3.png")
        self.imagesIdle[4] = pygame.image.load("../Assets/Sprites/jogador/playerIdle0.png")
        self.imagesRun[0] = pygame.image.load("../Assets/Sprites/jogador/playerRun0.png")
        self.imagesRun[1] = pygame.image.load("../Assets/Sprites/jogador/playerRun1.png")
        self.imagesRun[2] = pygame.image.load("../Assets/Sprites/jogador/playerRun2.png")
        self.imagesRun[3] = pygame.image.load("../Assets/Sprites/jogador/playerRun3.png")
        self.imagesRun[4] = pygame.image.load("../Assets/Sprites/jogador/playerRun2.png")

        self.image = pygame.transform.scale(self.imagesIdle[self.imageIndex], [self.largura, self.altura])
        self.surf.blit(self.image, self.coordant)
        self.estado = "parado"
        self.velocidade = 3
        self.vida = 3
        self.stamina = 100
        self.inventario = [None] * 20
        self.inventario[19] = itens.pocao_vida #adiciona pocaovida no inventario
        self.inventario[20] = itens.pocao_stamina  # adiciona pocaovida no inventario


    def move(self, direcao, direcaoHorizontal, direcaoVertical, colisoes):

        for retangulo in colisoes:
            if jogador.rect.colliderect(retangulo):
                jogador.resgata_posicao(colisoes)

        self.coordant = self.rect.topleft

        if direcaoVertical == "cima":
            if self.rect.top > 0:
                self.rect.move_ip(0, -self.velocidade)
        elif direcaoVertical == "baixo":
            if self.rect.bottom < 600:
                self.rect.move_ip(0, self.velocidade)

        if direcaoHorizontal == "direita":
            if self.rect.right < 800:
                self.rect.move_ip(self.velocidade, 0)
            self.ultimaDirecaoH = "direita"
        elif direcaoHorizontal == "esquerda":
            if self.rect.left > 0:
                self.rect.move_ip(-self.velocidade, 0)
            self.ultimaDirecaoH = "esquerda"

        # Correr
        if direcao == "shift" and self.stamina > 0:
            self.velocidade = 5
            self.stamina -= 1
        else:
            self.velocidade = 3
            if self.stamina < 100:
                self.stamina += 1

        if direcao == "cima" or direcao == "baixo" or direcao == "direita" or direcao == "esquerda":
            self.estado = "andando"
        else:
            self.estado = "parado"

        # Ajustar os sprites do jogador conforme a situação.
        if self.ultimaDirecaoH == "direita":
            if self.estado == "andando":
                self.image = pygame.transform.scale(self.imagesRun[int(self.imageIndex)], [self.largura, self.altura])
            elif self.estado == "parado":
                self.image = pygame.transform.scale(self.imagesIdle[int(self.imageIndex)], [self.largura, self.altura])
        elif self.ultimaDirecaoH == "esquerda":
            if self.estado == "andando":
                self.image = pygame.transform.scale(self.imagesRun[int(self.imageIndex)], [self.largura, self.altura])
                self.image = pygame.transform.flip(self.image, True, False)
            elif self.estado == "parado":
                self.image = pygame.transform.scale(self.imagesIdle[int(self.imageIndex)], [self.largura, self.altura])
                self.image = pygame.transform.flip(self.image, True, False)

        # Fazer o índice do sprite atual atualizar para realizar a animação.
        if self.imageIndex < 4:
            self.imageIndex += 0.15
        else:
            self.imageIndex = 0

    def muda_posicao(self, x, y):
        self.rect = self.surf.get_rect(top_left=(x, y))
    
    def resgata_posicao(self, colisoes):
        self.rect = self.surf.get_rect(topleft=self.coordant)

    def adiciona_item(self, item: item):
        control = 0
        for inventory_index in range(0, 20):
            if (self.inventario[inventory_index] == None) and (control == 0):
                self.inventario[inventory_index] = item
                control = 1

    def remove_item(self, index: int):
        self.inventario[index] = None


class Inimigo(Personagem):
    def __init__(self, largura, altura, *groups):
        super().__init__(largura, altura, *groups)

        self.imagesRun[0] = pygame.image.load("../Assets/Sprites/monstro/monsterRun0.png")
        self.imagesRun[1] = pygame.image.load("../Assets/Sprites/monstro/monsterRun1.png")
        self.imagesRun[2] = pygame.image.load("../Assets/Sprites/monstro/monsterRun2.png")
        self.imagesRun[3] = pygame.image.load("../Assets/Sprites/monstro/monsterRun3.png")
        self.imagesRun[4] = pygame.image.load("../Assets/Sprites/monstro/monsterRun0.png")

        self.image = pygame.transform.scale(self.imagesRun[self.imageIndex], [largura, altura])
        self.surf.blit(self.image, self.coordant)

        self.estado = "caminho"
        self.raio_de_visao = 160  # pixels
        self.angulo_de_visao = 60  # graus
        self.movimento_falhou = False
        self.velocidade = 2

    def raio_de_visao_setter(self, raio_de_visao):
        self.raio_de_visao = raio_de_visao

    def angulo_de_visao_setter(self, angulo_de_visao):
        self.angulo_de_visao = angulo_de_visao

    def estado_setter(self, estado):
        self.estado = estado

    def move(self, x, y):
        self.movimento_falhou = False
        self.coordant = self.rect.topleft
        self.rect.move_ip(x, y)
        if (self.rect.left < 0) or (self.rect.right > glob.tamanhoTela[0]) or (self.rect.top < 0) or (self.rect.bottom > glob.tamanhoTela[1]):
            self.resgata_posicao()

        # Verificar qual direção o monstro está caminhando.
        if self.rect.topleft[0] > self.coordant[0]:
            self.ultimaDirecaoH = "direita"
        elif self.rect.topleft[0] < self.coordant[0]:
            self.ultimaDirecaoH = "esquerda"

        # Ajustar os sprites do jogador conforme a situação.
        if self.ultimaDirecaoH == "direita":
            self.image = pygame.transform.scale(self.imagesRun[int(self.imageIndex)], [self.largura, self.altura])
        elif self.ultimaDirecaoH == "esquerda":
            self.image = pygame.transform.scale(self.imagesRun[int(self.imageIndex)], [self.largura, self.altura])
            self.image = pygame.transform.flip(self.image, True, False)

        # Fazer o índice do sprite atual atualizar para realizar a animação.
        if self.imageIndex < 4:
            self.imageIndex += 0.15
        else:
            self.imageIndex = 0

    def velocidade_setter(self, velocidade):
        self.velocidade = velocidade

    def resgata_posicao(self):
        self.rect.topleft = self.coordant
        self.movimento_falhou = True

    def define_posicao(self, ponto):
        self.rect.center = ponto


def update_groups():
    jogadorGroup.update()
    monstroGroup.update()


def draw_groups():
    jogadorGroup.draw(glob.tela)
    monstroGroup.draw(glob.tela)


jogadorGroup = pygame.sprite.Group()
monstroGroup = pygame.sprite.Group()
jogador = Jogador(32, 40, jogadorGroup)
inimigo = Inimigo(64, 72, monstroGroup)
inimigo.define_posicao((100, 250))
