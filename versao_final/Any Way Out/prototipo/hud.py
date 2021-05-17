from prototipo.cenas.sprites import SpritesCena
from prototipo.variaveisGlobais import glob


class HUD(SpritesCena):

    def __init__(self):
        super().__init__()
        self.barraStamina = [self.load_image("Assets/Sprites/hud/stamina0.png", True), self.load_image("Assets/Sprites/hud/stamina1.png", True),
                             self.load_image("Assets/Sprites/hud/stamina2.png", True), self.load_image("Assets/Sprites/hud/stamina3.png", True),
                             self.load_image("Assets/Sprites/hud/stamina4.png", True), self.load_image("Assets/Sprites/hud/staminaCheia.png", True)]
        self.barraVida = [self.load_image("Assets/Sprites/hud/vida0.png", True), self.load_image("Assets/Sprites/hud/vida1.png", True),
                          self.load_image("Assets/Sprites/hud/vida2.png", True), self.load_image("Assets/Sprites/hud/vidaCheia.png", True)]
        self.delay_vida = 0

    def desenhar_hud(self, stamina: int, vida: int, vida_x: float, vida_y: float, mostrar_vida: bool):
        # Verificar o sprite atual da barra de stamina.
        if stamina < 20:
            stamina_id = 0
        elif stamina < 40:
            stamina_id = 1
        elif stamina < 60:
            stamina_id = 2
        elif stamina < 80:
            stamina_id = 3
        elif stamina < 100:
            stamina_id = 4
        else:
            stamina_id = 5

        # Verificar o estado atual da barra de vida.
        if vida < 1:
            vida_id = 0
        elif vida < 2:
            vida_id = 1
        elif vida < 3:
            vida_id = 2
        else:
            vida_id = 3

        # Fazer a barra de vida aparecer e piscar apenas quando for mudada.
        if mostrar_vida:
            self.delay_vida = 100
        else:
            if (self.delay_vida > 65 or self.delay_vida < 35) and self.delay_vida > 0:
                glob.tela.blit(self.barraVida[vida_id], (vida_x, vida_y))
            if self.delay_vida > 0:
                self.delay_vida -= 1
        glob.tela.blit(self.barraStamina[stamina_id], (20, 20))  # Desenhar a barra de stamina.


hud = HUD()

