from prototipo.cenas.cena import Cena
from prototipo.menu import *
from pathlib import Path
from prototipo.variaveisGlobais import glob


class MenuPrincipal(Cena):  # ----------------------------------------------

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
        glob.tela.blit(self.fundo, (0, 0))
        glob.tela.blit(menuTitulo.sprite, (menuTitulo.posicaoX, menuTitulo.posicaoY))
        glob.tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        glob.tela.blit(menuNovoJogo.sprite, (menuNovoJogo.posicaoX, menuNovoJogo.posicaoY))
        glob.tela.blit(menuConfiguracoes.sprite, (menuConfiguracoes.posicaoX, menuConfiguracoes.posicaoY))
        glob.tela.blit(menuSair.sprite, (menuSair.posicaoX, menuSair.posicaoY))
        if exist == 1:
            glob.tela.blit(menuContinuar.sprite, (menuContinuar.posicaoX, menuContinuar.posicaoY))
        else:
            glob.tela.blit(menuContinuar2.sprite, (menuContinuar2.posicaoX, menuContinuar2.posicaoY))

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
            return "saguao"
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


class MenuSair0(Cena):  # ----------------------------------------------
    def __init__(self):
        super().__init__()
        self.fundo = bkg
        self.fundo2 = bkg2
        self.opcaoAtual = "nao"

    def iniciar(self):
        if MenuPrincipal.in_game == 1:
            glob.tela.blit(self.fundo2, (0, 0))
        else:
            glob.tela.blit(self.fundo, (0, 0))
        glob.tela.blit(menuTituloSair.sprite, (menuTituloSair.posicaoX, menuTituloSair.posicaoY))
        glob.tela.blit(atencao_info.sprite, (atencao_info.posicaoX, atencao_info.posicaoY))
        glob.tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        glob.tela.blit(menuSim.sprite, (menuSim.posicaoX, menuSim.posicaoY))
        glob.tela.blit(menuNao.sprite, (menuNao.posicaoX, menuNao.posicaoY))

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


class MenuConfig(Cena):  # ----------------------------------------------

    def __init__(self):
        super().__init__()
        self.fundo = bkg
        self.fundo2 = bkg2
        self.opcaoAtual = "volume"

    def iniciar(self):
        if MenuPrincipal.in_game == 1:
            glob.tela.blit(self.fundo2, (0, 0))
        else:
            glob.tela.blit(self.fundo, (0, 0))
        glob.tela.blit(menuTituloConfigs.sprite, (menuTituloConfigs.posicaoX, menuTituloConfigs.posicaoY))
        glob.tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        glob.tela.blit(menuVolume.sprite, (menuVolume.posicaoX, menuVolume.posicaoY))
        glob.tela.blit(menuControls.sprite, (menuControls.posicaoX, menuControls.posicaoY))
        glob.tela.blit(menuVoltar.sprite, (menuVoltar.posicaoX, menuVoltar.posicaoY))

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


class MenuControles(Cena):  # ----------------------------------------------
    def __init__(self):
        super().__init__()
        self.fundo = bkg
        self.fundo2 = bkg2
        self.opcaoAtual = "voltar"

    def iniciar(self):
        if MenuPrincipal.in_game == 1:
            glob.tela.blit(self.fundo2, (0, 0))
        else:
            glob.tela.blit(self.fundo, (0, 0))
        glob.tela.blit(menuTituloControles.sprite, (menuTituloControles.posicaoX, menuTituloControles.posicaoY))
        glob.tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        glob.tela.blit(controls_info.sprite, (controls_info.posicaoX, controls_info.posicaoY))
        glob.tela.blit(menuVoltar2.sprite, (menuVoltar2.posicaoX, menuVoltar2.posicaoY))

    def eventos(self):
        if self.tecla == "enter" and self.opcaoAtual == "voltar":
            return "menuConfig"

    def atualizar(self):
        if self.opcaoAtual == "voltar" and menuSeta.posicaoY != 520:
            menuSeta.posicaoY = 520