import pygame
from prototipo.personagens import jogador

class item:
    def __init__(self, nome: str, imgpath: str, usable: bool):
        self.nome = nome
        self.image = pygame.image.load(imgpath)
        self.usable = usable
        self.hp_change = 0
        self.stamina_change = 0

    def aplica_efeito(self):
        if jogador.vida < 3:
            jogador.vida = jogador.vida + self.hp_change
        if jogador.stamina<80:
            jogador.stamina = jogador.stamina + self.stamina_change

chave = item("Chave", "..\Assets\Sprites\menuPrincipal\seta.png", False)
pocao_vida = item("Poção de Vida",  "..\Assets\Sprites\menuPrincipal\seta.png", True)
pocao_vida.hp_change = 1
pocao_stamina = item("Poção de Stamina",  "..\Assets\Sprites\menuPrincipal\seta.png", True)
pocao_stamina.stamina_change = 20
cobre = item("Pedaço de Cobre",  "..\Assets\Sprites\menuPrincipal\seta.png", True)