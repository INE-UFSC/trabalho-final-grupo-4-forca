from prototipo.personagens import *
from prototipo.controladorInimigo import controlador


class Colisao:

    def __init__(self):
        self.parede_sprite = ""
        self.x = []
        self.y = []
        self.parede_rect = []

    def draw(self):
        pass

    def construir_cenario(self):
        pass

    def construir_parede_horizontal(self, x, y, quantidade):
        pass

    def desenhar_parede_horizontal(self):
        pass

    def get_colisao_jogador(self):
        pass

    def get_colisao_monstro(self):
        pass

    def colisao_monstro(self):
        pass
