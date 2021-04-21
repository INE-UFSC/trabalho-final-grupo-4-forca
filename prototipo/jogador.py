import pygame


class Jogador:

    def __init__(self, x, y):
        self.surf = pygame.Surface((60, 100))
        self.image = pygame.image.load("..\Assets\jogador\jogador.png")
        self.image = pygame.transform.scale(self.image, [60, 100])

        self.rect = self.surf.get_rect(topleft=(x, y))
        self.coordant = self.rect.topleft
        self.surf.blit(self.image, self.coordant)
        self.velocidade = 5
        self.vida = 3
        self.stamina = 100

    def move(self, direcao):
        self.coordant = self.rect.topleft
        if direcao == "cima":
            if self.rect.top > 0:
                self.rect.move_ip(0, -self.velocidade)
        elif direcao == "baixo":
            if self.rect.bottom < 600:
                self.rect.move_ip(0, self.velocidade)
        elif direcao == "direita":
            if self.rect.right < 800:
                self.rect.move_ip(self.velocidade, 0)
        elif direcao == "esquerda":
            if self.rect.left > 0:
                self.rect.move_ip(-self.velocidade, 0)
    
    def muda_posicao(self, x, y):
        self.rect = self.surf.get_rect(top_left=(x, y))
    
    def resgata_posicao(self):
        self.rect = self.surf.get_rect(topleft=self.coordant)

jogador = Jogador(0,0)
