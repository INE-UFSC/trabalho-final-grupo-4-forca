import pygame


class SpritesCena:
    def __init__(self):
        self.fundo = pygame.image.load("../Assets/Sprites/cenario/chaoGrande.png")
        self.fundo_inicio = pygame.image.load("../Assets/Sprites/cenario/inicio.png")
        self.parede_sprite_h = pygame.image.load("../Assets/Sprites/cenario/parede_horizontal.png")
        self.parede_sprite_v = pygame.image.load("../Assets/Sprites/cenario/parede_vertical.png")