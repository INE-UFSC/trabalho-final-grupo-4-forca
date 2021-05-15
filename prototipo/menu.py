from variaveisGlobais import glob
import pygame

# Código principal do Menu.


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
menuTituloPausa = MenuOpcao("../Assets/Sprites/menuPrincipal/titulo_pausa.png", 120, 50)
menuTituloConfigs = MenuOpcao("../Assets/Sprites/menuPrincipal/titulo_configs.png", 120, 50)
menuTituloControles = MenuOpcao("../Assets/Sprites/menuPrincipal/titulo_controles.png", 120, 50)
menuTituloSair = MenuOpcao("../Assets/Sprites/menuPrincipal/titulo_sair.png", 120, 50)
menuSim = MenuOpcao("../Assets/Sprites/menuPrincipal/sim.png", 440, 360)
menuNao = MenuOpcao("../Assets/Sprites/menuPrincipal/nao.png", 180, 360)
menuContinuar = MenuOpcao("../Assets/Sprites/menuPrincipal/continuar.png", 280, 200)
menuContinuar2 = MenuOpcao("../Assets/Sprites/menuPrincipal/continuar_apagado.png", 280, 200)
menuContinuar3 = MenuOpcao("../Assets/Sprites/menuPrincipal/continuar.png", 280, 520)
menuContinuar_em_jogo = MenuOpcao("../Assets/Sprites/menuPrincipal/continuar.png", 280, 200)
menuNovoJogo = MenuOpcao("../Assets/Sprites/menuPrincipal/novoJogo.png", 280, 280)
menuConfiguracoes = MenuOpcao("../Assets/Sprites/menuPrincipal/configuracoes.png", 280, 360)
menuConfiguracoesEmJogo = MenuOpcao("../Assets/Sprites/menuPrincipal/configuracoes.png", 280, 280)
menuControls = MenuOpcao("../Assets/Sprites/menuPrincipal/controles.png", 280, 280)
menuVolume = MenuOpcao("../Assets/Sprites/menuPrincipal/volume.png", 280, 200)
menuVoltar = MenuOpcao("../Assets/Sprites/menuPrincipal/voltar.png", 280, 360)
controls_info = MenuOpcao("../Assets/Sprites/menuPrincipal/controles_info.png", 210, 150)
tutorial1 = MenuOpcao("../Assets/Sprites/menuPrincipal/tutorial1.png", 90, 150)
tutorial2 = MenuOpcao("../Assets/Sprites/menuPrincipal/tutorial2.png", 90, 150)
tutorial_titulo = MenuOpcao("../Assets/Sprites/menuPrincipal/tutorial_titulo.png", 120, 50)
atencao_info = MenuOpcao("../Assets/Sprites/menuPrincipal/atencao.png", 200, 160)
menuVoltar2 = MenuOpcao("../Assets/Sprites/menuPrincipal/voltar.png", 280, 520)
menuSair = MenuOpcao("../Assets/Sprites/menuPrincipal/sair.png", 280, 440)
menuSairEmJogo = MenuOpcao("../Assets/Sprites/menuPrincipal/sair.png", 280, 361)
menuSeta = MenuOpcao("../Assets/Sprites/menuPrincipal/seta.png", 210, 200)
menuTituloVolume = MenuOpcao("../Assets/Sprites/menuPrincipal/titulo_volume.png", 120, 50)
volume_efeitos = MenuOpcao("../Assets/Sprites/menuPrincipal/volume_efeitos.png", 80, 200)
volume_musica = MenuOpcao("../Assets/Sprites/menuPrincipal/volume_musica.png", 80, 280)
barra_efeitos = MenuOpcao("../Assets/Sprites/menuPrincipal/barra_volume.png", 290, 200)
barra_musica = MenuOpcao("../Assets/Sprites/menuPrincipal/barra_volume.png", 290, 280)
slider = MenuOpcao("../Assets/Sprites/menuPrincipal/slider.png", 292, 202)
slider2 = MenuOpcao("../Assets/Sprites/menuPrincipal/slider.png", 292, 282)
menuTituloFim = MenuOpcao("../Assets/Sprites/menuPrincipal/titulo_fim.png", 120, 50)
menuFim = MenuOpcao("../Assets/Sprites/menuPrincipal/fim.png", 120, 150)
fimMorte = MenuOpcao("../Assets/Sprites/menuPrincipal/fimMorte.png", 120, 150)

bkg_img = pygame.image.load("../Assets/Sprites/menuPrincipal/fundo2.jpg")
bkg2_img = pygame.image.load("../Assets/Sprites/menuPrincipal/fundo3.jpg")
bkg3_img = pygame.image.load("../Assets/Sprites/menuPrincipal/fundo_inicio.png")
ibkg_img = pygame.image.load("../Assets/Sprites/menuPrincipal/inventorybackground.png")
bkg = pygame.transform.scale(bkg_img, (glob.tamanhoTela[0], glob.tamanhoTela[1]))
bkg2 = pygame.transform.scale(bkg2_img, (glob.tamanhoTela[0], glob.tamanhoTela[1]))
bkg3 = pygame.transform.scale(bkg3_img, (glob.tamanhoTela[0], glob.tamanhoTela[1]))
ibkg = pygame.transform.scale(ibkg_img, (600, 520))

