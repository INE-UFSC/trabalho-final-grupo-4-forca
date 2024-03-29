import pygame


class SpritesCena:
    def __init__(self):
        self.fundo = self.load_image("Assets/Sprites/cenario/chaoGrande.png")
        self.fundo_inicio = self.load_image("Assets/Sprites/cenario/inicio.png")
        self.parede_sprite_h = self.load_image("Assets/Sprites/cenario/parede_horizontal.png")
        self.parede_sprite_v = self.load_image("Assets/Sprites/cenario/parede_vertical.png")
        self.parede_sprite_vh = self.load_image("Assets/Sprites/cenario/parede_verticalh.png")
        self.sprite_mesa = self.load_image("Assets/Sprites/cenario/mesa.png", True)
        self.sprite_iluminacao = self.load_image("Assets/Sprites/cenario/efeitodeluzjogogrande.png", True)

    # Se o sprite tiver transparência, "transparente" precisa ser True.
    def load_image(self, imagem: str, transparente=False):
        if not transparente:
            return pygame.image.load(imagem).convert()
        else:
            return pygame.image.load(imagem).convert_alpha()


spritesCena = SpritesCena()
