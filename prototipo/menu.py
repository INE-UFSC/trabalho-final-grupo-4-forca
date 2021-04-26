from variaveisGlobais import *
#   Código principal do Menu.


class MenuBotao:

    def __init__(self):
        self.posicaoX = 120
        self.posicaoY = 50
        self.sprite = pygame.image.load("../Assets/Sprites/menuPrincipal/titulo.png")


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
menuContinuar = MenuOpcao("../Assets/Sprites/menuPrincipal/continuar.png", 280, 200)
menuContinuar2 = MenuOpcao("../Assets/Sprites/menuPrincipal/continuar_apagado.png", 280, 200)
menuNovoJogo = MenuOpcao("../Assets/Sprites/menuPrincipal/novoJogo.png", 280, 280)
menuConfiguracoes = MenuOpcao("../Assets/Sprites/menuPrincipal/configuracoes.png", 280, 360)
menuControls = MenuOpcao("../Assets/Sprites/menuPrincipal/controles.png", 280, 280)
menuVolume = MenuOpcao("../Assets/Sprites/menuPrincipal/volume.png", 280, 200)
menuVoltar = MenuOpcao("../Assets/Sprites/menuPrincipal/voltar.png", 280, 360)
controls_info = MenuOpcao("../Assets/Sprites/menuPrincipal/controles_info.png", 150, 150)
menuVoltar2 = MenuOpcao("../Assets/Sprites/menuPrincipal/voltar.png", 280, 440)
menuSair = MenuOpcao("../Assets/Sprites/menuPrincipal/sair.png", 280, 440)
menuSeta = MenuOpcao("../Assets/Sprites/menuPrincipal/seta.png", 210, 200)
bkg_img = pygame.image.load("../Assets/Sprites/menuPrincipal/fundo2.jpg")
bkg = pygame.transform.scale(bkg_img, (largura, altura))


#menuTitulo = MenuTitulo()
#menuContinuar = MenuContinuar("../Assets/Sprites/menuPrincipal/continuar.png", 280, 200)
#menuNovoJogo = MenuNovoJogo("../Assets/Sprites/menuPrincipal/novoJogo.png", 280, 280)
#menuConfiguracoes = MenuConfiguracoes("../Assets/Sprites/menuPrincipal/configuracoes.png", 280, 360)
#menuSair = MenuSair("../Assets/Sprites/menuPrincipal/sair.png", 280, 440)
#menuSeta = MenuSeta("../Assets/Sprites/menuPrincipal/seta.png", 210, 200)

