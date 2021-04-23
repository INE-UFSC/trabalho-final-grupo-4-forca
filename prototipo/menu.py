from variaveisGlobais import *
#   Código principal do Menu.


class MenuBotao:

    def __init__(self):
        self.posicaoX = 120
        self.posicaoY = 50
        self.sprite = pygame.image.load("../Assets/menuPrincipal/titulo.png")


class MenuTitulo(MenuBotao):

    def __init__(self):
        super().__init__()


class MenuOpcao(MenuBotao):

    def __init__(self, sprite, x, y):
        super().__init__()
        self.posicaoX = x
        self.posicaoY = y
        self.sprite = pygame.image.load(sprite)

menuTitulo = MenuTitulo()
menuContinuar = MenuOpcao("../Assets/menuPrincipal/continuar.png", 280, 200)
menuContinuar2 = MenuOpcao("../Assets/menuPrincipal/continuar_apagado.png", 280, 200)
menuNovoJogo = MenuOpcao("../Assets/menuPrincipal/novoJogo.png", 280, 280)
menuConfiguracoes = MenuOpcao("../Assets/menuPrincipal/configuracoes.png", 280, 360)
menuControls = MenuOpcao("../Assets/menuPrincipal/controles.png", 280, 280)
menuVolume = MenuOpcao("../Assets/menuPrincipal/volume.png", 280, 200)
menuVoltar = MenuOpcao("../Assets/menuPrincipal/voltar.png", 280, 360)
controls_info = MenuOpcao("../Assets/menuPrincipal/controles_info.png", 150, 150)
menuVoltar2 = MenuOpcao("../Assets/menuPrincipal/voltar.png", 280, 440)
menuSair = MenuOpcao("../Assets/menuPrincipal/sair.png", 280, 440)
menuSeta = MenuOpcao("../Assets/menuPrincipal/seta.png", 210, 200)
bkg_img = pygame.image.load("../Assets/menuPrincipal/fundo2.jpg")
bkg = pygame.transform.scale(bkg_img, (largura, altura))


