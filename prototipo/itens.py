import pygame

class item:
    def __init__(self, nome: str, imgpath: str, usable: bool):
        self.nome = nome
        self.image = pygame.image.load(imgpath)
        self.usable = usable
        self.hp_change = 0
        self.stamina_change = 0

    def aplica_efeito(self, jogador):
        if jogador.vida < 3:
            jogador.vida = jogador.vida + self.hp_change
        if jogador.stamina<80:
            jogador.stamina = jogador.stamina + self.stamina_change

chave = item("Chave", "..\Assets\Sprites\itens\chave.png", False)
pocao_vida = item("Poção de Vida",  "..\Assets\Sprites\itens\pocaovida.png", True)
pocao_vida.hp_change = 1
pocao_stamina = item("Poção de Stamina",  "..\Assets\Sprites\itens\pocaostamina.png", True)
pocao_stamina.stamina_change = 20
cobre = item("Pedaço de Cobre",  "..\Assets\Sprites\itens\cobre.png", False)