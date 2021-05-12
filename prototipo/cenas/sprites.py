import pygame


class SpritesCena:
    def __init__(self):
        self.fundo = self.load_image("../Assets/Sprites/cenario/chaoGrande.png")
        self.fundo_inicio = self.load_image("../Assets/Sprites/cenario/inicio.png")
        self.parede_sprite_h = self.load_image("../Assets/Sprites/cenario/parede_horizontal.png")
        self.parede_sprite_v = self.load_image("../Assets/Sprites/cenario/parede_vertical.png")
        self.mesa_sprite = self.load_image("../Assets/Sprites/cenario/mesa.png")

    def load_image(self, imagem: str, transparente=False):
        if not transparente:
            return pygame.image.load(imagem).convert()
        else:
            return pygame.image.load(imagem).convert_alpha()
