from menu import *
from variaveisGlobais import *
from personagens import *
from controladorInimigo import *
from pathlib import Path
from construtorCenario import construtorCenario

class Cena:

    def __init__(self):
        self.largura = largura
        self.altura = altura
        self.fundo = ""
        self.tecla = ""
        self.proximaCena = "nenhuma"
        self.iniciou = False

    def iniciar(self):
        pass

    def atualizar(self):
        atualizarGroups()


class MenuPrincipal(Cena):

    in_game = 0
    def __init__(self):
        self.config = 0
        save = Path("saves/save.txt")
        exist = 0
        if save.is_file():
            exist = 1
        super().__init__()
        self.opcaoAtual = "continuar"
        self.fundo = bkg
        if exist == 1:
            self.opcaoAtual = "continuar"
        else:
            self.opcaoAtual = "novoJogo"

#   Evitar que os elementos sejam desenhados mais que uma vez.
    def iniciar(self):
        save = Path("saves/save.txt")
        exist = 0
        if save.is_file():
            exist = 1
        tela.blit(self.fundo, (0, 0))
        tela.blit(menuTitulo.sprite, (menuTitulo.posicaoX, menuTitulo.posicaoY))
        tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        tela.blit(menuNovoJogo.sprite, (menuNovoJogo.posicaoX, menuNovoJogo.posicaoY))
        tela.blit(menuConfiguracoes.sprite, (menuConfiguracoes.posicaoX, menuConfiguracoes.posicaoY))
        tela.blit(menuSair.sprite, (menuSair.posicaoX, menuSair.posicaoY))
        if exist == 1:
            tela.blit(menuContinuar.sprite, (menuContinuar.posicaoX, menuContinuar.posicaoY))
        else:
            tela.blit(menuContinuar2.sprite, (menuContinuar2.posicaoX, menuContinuar2.posicaoY))

    def eventos(self):
        save = Path("saves/save.txt")
        exist = 0
        if save.is_file():
            exist = 1

        if exist == 1:
            if self.tecla == "baixo":
                if self.opcaoAtual == "continuar":    self.opcaoAtual = "novoJogo"
                elif self.opcaoAtual == "novoJogo":   self.opcaoAtual = "configuracoes"
                elif self.opcaoAtual == "configuracoes":  self.opcaoAtual = "sair"
                elif self.opcaoAtual == "sair":   self.opcaoAtual = "continuar"
                return None
            elif self.tecla == "cima":
                if self.opcaoAtual == "continuar":    self.opcaoAtual = "sair"
                elif self.opcaoAtual == "novoJogo":   self.opcaoAtual = "continuar"
                elif self.opcaoAtual == "configuracoes":  self.opcaoAtual = "novoJogo"
                elif self.opcaoAtual == "sair":   self.opcaoAtual = "configuracoes"
                return None
        else:
            if self.tecla == "baixo":
                if self.opcaoAtual == "novoJogo":   self.opcaoAtual = "configuracoes"
                elif self.opcaoAtual == "configuracoes":  self.opcaoAtual = "sair"
                elif self.opcaoAtual == "sair":   self.opcaoAtual = "novoJogo"
                return None
            elif self.tecla == "cima":
                if self.opcaoAtual == "novoJogo":    self.opcaoAtual = "sair"
                elif self.opcaoAtual == "configuracoes":  self.opcaoAtual = "novoJogo"
                elif self.opcaoAtual == "sair":   self.opcaoAtual = "configuracoes"
                return None

        if self.tecla == "enter" and self.opcaoAtual == "novoJogo":
            MenuPrincipal.in_game = 1
            return "cenarioTeste"
        elif self.tecla == "enter" and self.opcaoAtual == "configuracoes":
            return "menuConfig"
        elif self.tecla == "enter" and self.opcaoAtual == "sair":
            return "menuSair0"

    def atualizar(self):
        if self.opcaoAtual == "continuar" and menuSeta.posicaoY != 200:
            menuSeta.posicaoX = 200
            menuSeta.posicaoY = 200
        elif self.opcaoAtual == "novoJogo" and menuSeta.posicaoY != 280:
            menuSeta.posicaoX = 200
            menuSeta.posicaoY = 280
        elif self.opcaoAtual == "configuracoes" and menuSeta.posicaoY != 360:
            menuSeta.posicaoX = 200
            menuSeta.posicaoY = 360
        elif self.opcaoAtual == "sair" and menuSeta.posicaoY != 440:
            menuSeta.posicaoX = 200
            menuSeta.posicaoY = 440

class MenuSair0(Cena):
    def __init__(self):
        super().__init__()
        self.fundo = bkg
        self.fundo2 = bkg2
        self.opcaoAtual = "nao"

    def iniciar(self):
        if MenuPrincipal.in_game == 1:
            tela.blit(self.fundo2, (0, 0))
        else:
            tela.blit(self.fundo, (0, 0))
        tela.blit(menuTituloSair.sprite, (menuTituloSair.posicaoX, menuTituloSair.posicaoY))
        tela.blit(atencao_info.sprite, (atencao_info.posicaoX, atencao_info.posicaoY))
        tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        tela.blit(menuSim.sprite, (menuSim.posicaoX, menuSim.posicaoY))
        tela.blit(menuNao.sprite, (menuNao.posicaoX, menuNao.posicaoY))

    def eventos(self):
        if self.tecla == "esquerda":
            if self.opcaoAtual == "nao":
                self.opcaoAtual = "sim"
            elif self.opcaoAtual == "sim":
                self.opcaoAtual = "nao"
            return None
        elif self.tecla == "direita":
            if self.opcaoAtual == "nao":
                self.opcaoAtual = "sim"
            elif self.opcaoAtual == "sim":
                self.opcaoAtual = "nao"
            return None
        if self.tecla == "enter" and self.opcaoAtual == "nao":
            if MenuPrincipal.in_game == 1:
                return "menuEmJogo"
            else:
                return "menuPrincipal"
        elif self.tecla == "enter" and self.opcaoAtual == "sim":
            return "fecharJogo"

    def atualizar(self):
        if self.opcaoAtual == "nao" and menuSeta.posicaoX != 110:
            menuSeta.posicaoX = 110
            menuSeta.posicaoY = 360
        elif self.opcaoAtual == "sim" and menuSeta.posicaoX != 370:
            menuSeta.posicaoX = 370
            menuSeta.posicaoY = 360


class MenuConfig(Cena):

    def __init__(self):
        super().__init__()
        self.fundo = bkg
        self.fundo2 = bkg2
        self.opcaoAtual = "volume"

    def iniciar(self):
        if MenuPrincipal.in_game == 1:
            tela.blit(self.fundo2, (0, 0))
        else:
            tela.blit(self.fundo, (0, 0))
        tela.blit(menuTituloConfigs.sprite, (menuTituloConfigs.posicaoX, menuTituloConfigs.posicaoY))
        tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        tela.blit(menuVolume.sprite, (menuVolume.posicaoX, menuVolume.posicaoY))
        tela.blit(menuControls.sprite, (menuControls.posicaoX, menuControls.posicaoY))
        tela.blit(menuVoltar.sprite, (menuVoltar.posicaoX, menuVoltar.posicaoY))

    def eventos(self):
        if self.tecla == "baixo":
            if self.opcaoAtual == "volume":    self.opcaoAtual = "controles"
            elif self.opcaoAtual == "controles":   self.opcaoAtual = "voltar"
            elif self.opcaoAtual == "voltar":   self.opcaoAtual = "volume"
            return None
        elif self.tecla == "cima":
            if self.opcaoAtual == "volume":    self.opcaoAtual = "voltar"
            elif self.opcaoAtual == "controles":    self.opcaoAtual = "volume"
            elif self.opcaoAtual == "voltar":   self.opcaoAtual = "controles"
            return None
        elif self.tecla == "enter" and self.opcaoAtual == "voltar":
            if MenuPrincipal.in_game == 1:
                return "menuEmJogo"
            else:
                return "menuPrincipal"
        elif self.tecla == "enter" and self.opcaoAtual == "controles":
            return "menuControles"

    def atualizar(self):
        if self.opcaoAtual == "volume" and menuSeta.posicaoY != 200:
            menuSeta.posicaoY = 200
        elif self.opcaoAtual == "controles" and menuSeta.posicaoY != 280:
            menuSeta.posicaoY = 280
        elif self.opcaoAtual == "voltar" and menuSeta.posicaoY != 360:
            menuSeta.posicaoY = 360


class MenuControles(Cena):
    def __init__(self):
        super().__init__()
        self.fundo = bkg
        self.fundo2 = bkg2
        self.opcaoAtual = "voltar"

    def iniciar(self):
        if MenuPrincipal.in_game == 1:
            tela.blit(self.fundo2, (0, 0))
        else:
            tela.blit(self.fundo, (0, 0))
        tela.blit(menuTituloControles.sprite, (menuTituloControles.posicaoX, menuTituloControles.posicaoY))
        tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        tela.blit(controls_info.sprite, (controls_info.posicaoX, controls_info.posicaoY))
        tela.blit(menuVoltar2.sprite, (menuVoltar2.posicaoX, menuVoltar2.posicaoY))

    def eventos(self):
        if self.tecla == "enter" and self.opcaoAtual == "voltar":
            return "menuConfig"

    def atualizar(self):
        if self.opcaoAtual == "voltar" and menuSeta.posicaoY != 520:
            menuSeta.posicaoY = 520


class Saguao(Cena):

    def __init__(self, largura, altura):
        super().__init__()
        self.largura = largura
        self.altura = altura


class CenarioTeste(Cena):
    def __init__(self):
        super().__init__()
        self.teclaHorizontal = ""
        self.teclaVertical = ""
        self.fundo = pygame.image.load("../Assets/Sprites/cenario/chaoGrande.png")#pygame.Surface((self.largura, self.altura))
        #self.parede = pygame.Surface((204, 147))
        #self.parede.blit(pygame.image.load("../Assets/Sprites/cenario/parede.png"), (0, 0))#fill(vermelho)
        self.parede = pygame.image.load("../Assets/Sprites/cenario/parede.png")
        self.parede0rect = self.parede.get_rect(topleft=(100, 40))
        self.parede1rect = self.parede.get_rect(topleft=(100, 375))
        self.parede2rect = self.parede.get_rect(topleft=(500, 500))
        self.lista_parederect = [self.parede0rect, self.parede1rect, self.parede2rect]
    
    def iniciar(self):
        #drawGroups()
        #construtorCenario.construirChao(0, 0, 60, construtorCenario.chaoPadrao)
        print("iniciou")
        self.iniciou = True
    
    def eventos(self):
        jogador.move(self.tecla, self.teclaHorizontal, self.teclaVertical)

        for retangulo in self.lista_parederect:
            if jogador.rect.colliderect(retangulo):
                jogador.resgata_posicao()

        if jogador.rect.colliderect(inimigo.rect):
            jogador.resgata_posicao()
        controlador.movimenta()

        for retangulo in self.lista_parederect:
            if inimigo.rect.colliderect(retangulo):
                inimigo.resgata_posicao()
        
        if inimigo.movimento_falhou:
            controlador.movimenta_x()
            for retangulo in self.lista_parederect:
                if inimigo.rect.colliderect(retangulo):
                    inimigo.resgata_posicao()
        if inimigo.movimento_falhou:
            controlador.movimenta_y()
            for retangulo in self.lista_parederect:
                if inimigo.rect.colliderect(retangulo):
                    inimigo.resgata_posicao()

        if inimigo.rect.colliderect(jogador.rect):
            inimigo.resgata_posicao()

        if self.tecla == "p":
            return "menuEmJogo"
        if self.tecla == "e":
            return "inventario"

    def atualizar(self):
        tela.blit(self.fundo, (0, 0))
        #construtorCenario.drawGroups()
        #construtorCenario.updateGroups()
        tela.blit(self.parede, (100, 40))
        tela.blit(self.parede, (100, 375))
        tela.blit(self.parede, (500, 500))
        drawGroups()
        atualizarGroups()

class MenuEmJogo(Cena):

    def __init__(self):
        super().__init__()
        self.opcaoAtual = "continuar"
        self.fundo = bkg
        self.fundo2 = bkg2

    def iniciar(self):
        if MenuPrincipal.in_game == 1:
            tela.blit(self.fundo2, (0, 0))
        else:
            tela.blit(self.fundo, (0, 0))
        tela.blit(menuTituloPausa.sprite, (menuTituloPausa.posicaoX, menuTituloPausa.posicaoY))
        tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        tela.blit(menuContinuar_em_jogo.sprite, (menuContinuar_em_jogo.posicaoX, menuContinuar_em_jogo.posicaoY))
        tela.blit(menuConfiguracoesEmJogo.sprite, (menuConfiguracoesEmJogo.posicaoX, menuConfiguracoesEmJogo.posicaoY))
        tela.blit(menuSairEmJogo.sprite, (menuSairEmJogo.posicaoX, menuSairEmJogo.posicaoY))

    def eventos(self):
        if self.tecla == "baixo":
            if self.opcaoAtual == "continuar":    self.opcaoAtual = "configuracoes"
            elif self.opcaoAtual == "configuracoes":   self.opcaoAtual = "sair"
            elif self.opcaoAtual == "sair":  self.opcaoAtual = "continuar"
            return None
        elif self.tecla == "cima":
            if self.opcaoAtual == "continuar":    self.opcaoAtual = "sair"
            elif self.opcaoAtual == "configuracoes":  self.opcaoAtual = "continuar"
            elif self.opcaoAtual == "sair":   self.opcaoAtual = "configuracoes"
            return None

        if self.tecla == "enter" and self.opcaoAtual == "continuar":
            return "cenarioTeste"
        elif self.tecla == "enter" and self.opcaoAtual == "configuracoes":
            return "menuConfig"
        elif self.tecla == "enter" and self.opcaoAtual == "sair":
            return "menuSair0"
        elif self.tecla == "esc":
            return "cenarioTeste"

    def atualizar(self):
        if self.opcaoAtual == "continuar" and menuSeta.posicaoY != 200:
            menuSeta.posicaoX = 200
            menuSeta.posicaoY = 200
        elif self.opcaoAtual == "configuracoes" and menuSeta.posicaoY != 280:
            menuSeta.posicaoX = 200
            menuSeta.posicaoY = 280
        elif self.opcaoAtual == "sair" and menuSeta.posicaoY != 361:
            menuSeta.posicaoX = 200
            menuSeta.posicaoY = 361

class MenuInventario(Cena):
    def __init__(self):
        super().__init__()
        self.fundo = ibkg
        self.container = pygame.Surface((100, 100))
        self.container.fill((127, 127, 127))
        self.selectedBox = pygame.Surface((100, 100))
        self.selectedBox.fill((191, 191, 191))
        self.box_x = 150
        self.box_y = 100
        self.itemindex = 0
        self.jaMudou = False

    def iniciar(self):
        self.iniciou = True

    def eventos(self):
        if not self.jaMudou:
            if self.tecla=="esc":
                return "cenarioTeste"
            if self.tecla == "cima" and self.box_y>100:
                self.box_y = self.box_y-100
                self.itemindex = self.itemindex - 5
            if self.tecla == "baixo" and self.box_y<400:
                self.box_y = self.box_y + 100
                self.itemindex = self.itemindex + 5
            if self.tecla == "esquerda" and self.box_x>150:
                self.box_x = self.box_x - 100
                self.itemindex = self.itemindex - 1
            if self.tecla == "direita" and self.box_x<550:
                self.box_x = self.box_x + 100
                self.itemindex = self.itemindex + 1
            if self.tecla == "enter" and jogador.inventario[self.itemindex]!= None:
                if jogador.inventario[self.itemindex].usable == True:
                    jogador.aplica_efeito(self.itemindex)                               # não entendo por que não
                    jogador.remove_item(self.itemindex)                                 # funciona na mesma linha

        if self.tecla != "cima" and self.tecla != "baixo" and self.tecla != "direita" and self.tecla != "esquerda":
            self.jaMudou = False
        else:
            self.jaMudou = True

    def atualizar(self):
        tela.blit(self.fundo, (100, 50))
        for i in range(0, 4):
            for j in range(0, 5):
                tela.blit(self.container, (((j * 100) + 150), ((i * 100) + 100)))
        tela.blit(self.selectedBox, (self.box_x, self.box_y))
        for i in range(0, 4):
            for j in range(0, 5):
                if jogador.inventario[(i * 5) + j] != None:
                    tela.blit(jogador.inventario[(i * 5) + j].image, (((j * 100) + 150), ((i * 100) + 100)))


#cena = Cena()
menuPrincipal = MenuPrincipal()
cenarioTeste = CenarioTeste()
menuConfig = MenuConfig()
menuControles = MenuControles()
menuEmJogo = MenuEmJogo()
menuInventario = MenuInventario()
menuSair0 = MenuSair0()
