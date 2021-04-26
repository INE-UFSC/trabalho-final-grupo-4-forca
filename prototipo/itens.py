import pygame

class item:
    def __init__(self, nome: str, imgpath: str, usable: bool):
        self.nome = nome
        self.image = pygame.image.load(imgpath)
        self.usable = usable

chave = item("Chave", "..\Assets\Sprites\menuPrincipal\seta.png", True)