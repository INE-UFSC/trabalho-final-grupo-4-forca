import pygame

class item:
    cobre1 = False
    cobre2 = False
    cobre3 = False
    possui_ferramenta_sala = False
    possui_ferramenta_cozinha = False
    possui_chave_cozinha = False
    possui_codigo = False

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


ferramenta1 = item("Ferramenta 1", "..\Assets\Sprites\itens\\ferramenta1.png", False)
chave = item("Chave", "..\Assets\Sprites\itens\chave.png", False)
pocao_vida = item("Poção de Vida",  "..\Assets\Sprites\itens\pocaovida.png", True)
pocao_vida.hp_change = 1
pocao_stamina = item("Poção de Stamina",  "..\Assets\Sprites\itens\pocaostamina.png", True)
pocao_stamina.stamina_change = 20
cobre = item("Pedaço de Cobre",  "..\Assets\Sprites\itens\cobre.png", False)
ferramenta2 = item("Ferramenta 2",  "..\Assets\Sprites\itens\\ferramenta2.png", False)
codigo = item("Código",  "..\Assets\Sprites\itens\codigo.png", False)
