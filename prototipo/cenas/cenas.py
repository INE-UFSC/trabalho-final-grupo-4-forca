from prototipo.cenas.menu_principal import MenuPrincipal, MenuConfig, MenuControles, MenuSair0, MenuVolume
from prototipo.cenas.saguao import Saguao
from prototipo.cenas.inicio import Inicio
from prototipo.cenas.porao import Porao
from prototipo.cenas.menu_em_jogo import MenuEmJogo, MenuInventario, MenuTutorial1, MenuTutorial2
from prototipo.cenas.cozinha import Cozinha


class Cenas:
    def __init__(self):
        self.menuPrincipal = MenuPrincipal()
        self.tutorial1 = MenuTutorial1()
        self.tutorial2 = MenuTutorial2()
        self.inicio = Inicio()
        self.saguao = Saguao()
        self.porao = Porao()
        self.menuConfig = MenuConfig()
        self.menuControles = MenuControles()
        self.menuEmJogo = MenuEmJogo()
        self.menuInventario = MenuInventario()
        self.menuSair0 = MenuSair0()
        self.cozinha = Cozinha()
        self.menuVolume = MenuVolume()

        self.cenas = [self.menuPrincipal, self.tutorial1, self.tutorial2, self.inicio, self.saguao, self.porao,
                      self.menuConfig, self.menuControles, self.menuEmJogo, self.menuInventario, self.menuSair0,
                      self.cozinha, self.menuVolume]
        self.nomes = ["menuPrincipal", "tutorial1", "tutorial2", "inicio", "saguao", "porao",
                      "menuConfig", "menuControles", "menuEmJogo", "inventario", "menuSair0",
                      "cozinha", "menuVolume"]


cenas = Cenas()
