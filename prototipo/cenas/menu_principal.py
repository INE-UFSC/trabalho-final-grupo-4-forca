from prototipo.cenas.cena import Cena
from prototipo.menu import *
from pathlib import Path
from prototipo.variaveisGlobais import glob
from prototipo import som
from configparser import ConfigParser
config = ConfigParser()


class MenuPrincipal(Cena):  # ----------------------------------------------
    in_game = 0

    def __init__(self):
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
            som.music_ambiente()
            for e in som.sons:  e.set_volume(glob.volume_efeitos)
            pygame.mixer.music.set_volume(glob.volume_musica)
            return "tutorial1"
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
        elif self.tecla == "enter" and self.opcaoAtual == "volume":
            return "menuVolume"

    def atualizar(self):
        if self.opcaoAtual == "volume" and menuSeta.posicaoY != 200:
            menuSeta.posicaoY = 200
        elif self.opcaoAtual == "controles" and menuSeta.posicaoY != 280:
            menuSeta.posicaoY = 280
        elif self.opcaoAtual == "voltar" and menuSeta.posicaoY != 360:
            menuSeta.posicaoY = 360


class MenuVolume(Cena):  # ----------------------------------------------
    def __init__(self):
        super().__init__()
        self.fundo = bkg
        self.fundo2 = bkg2
        self.opcaoAtual = "efeitos"
        try:
            config.read('config.ini')
            self.pos_efeitos = config.get('volume', 'posicao_efeitos')
            self.pos_musica = config.get('volume', 'posicao_musica')
        except:
            self.pos_musica = 'pos1'
            self.pos_efeitos = 'pos1'

    def iniciar(self):
        if MenuPrincipal.in_game == 1:
            glob.tela.blit(self.fundo2, (0, 0))
        else:
            glob.tela.blit(self.fundo, (0, 0))
        glob.tela.blit(menuTituloVolume.sprite, (menuTituloVolume.posicaoX, menuTituloVolume.posicaoY))
        glob.tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        glob.tela.blit(volume_efeitos.sprite, (volume_efeitos.posicaoX, volume_efeitos.posicaoY))
        glob.tela.blit(barra_efeitos.sprite, (barra_efeitos.posicaoX, barra_efeitos.posicaoY))
        glob.tela.blit(slider.sprite, (slider.posicaoX, slider.posicaoY))
        glob.tela.blit(volume_musica.sprite, (volume_musica.posicaoX, volume_musica.posicaoY))
        glob.tela.blit(barra_musica.sprite, (barra_musica.posicaoX, barra_musica.posicaoY))
        glob.tela.blit(slider2.sprite, (slider2.posicaoX, slider2.posicaoY))
        glob.tela.blit(menuVoltar2.sprite, (menuVoltar2.posicaoX, menuVoltar2.posicaoY))


    def eventos(self):
        if self.tecla == "baixo":
            if self.opcaoAtual == "efeitos":    self.opcaoAtual = "musica"
            elif self.opcaoAtual == "musica":   self.opcaoAtual = "voltar"
            elif self.opcaoAtual == "voltar":   self.opcaoAtual = "efeitos"
            return None
        elif self.tecla == "cima":
            if self.opcaoAtual == "efeitos":    self.opcaoAtual = "voltar"
            elif self.opcaoAtual == "musica":    self.opcaoAtual = "efeitos"
            elif self.opcaoAtual == "voltar":   self.opcaoAtual = "musica"
            return None
        if self.opcaoAtual == "efeitos":
            if self.tecla == "direita":
                if self.pos_efeitos == "pos0":
                    glob.volume_efeitos = 0.1
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos1"
                elif self.pos_efeitos == "pos1":
                    glob.volume_efeitos = 0.2
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos2"
                elif self.pos_efeitos == "pos2":
                    glob.volume_efeitos = 0.3
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos3"
                elif self.pos_efeitos == "pos3":
                    glob.volume_efeitos = 0.4
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos4"
                elif self.pos_efeitos == "pos4":
                    glob.volume_efeitos = 0.5
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos5"
                elif self.pos_efeitos == "pos5":
                    glob.volume_efeitos = 0.6
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos6"
                elif self.pos_efeitos == "pos6":
                    glob.volume_efeitos = 0.7
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos7"
                elif self.pos_efeitos == "pos7":
                    glob.volume_efeitos = 0.8
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos8"
                elif self.pos_efeitos == "pos8":
                    glob.volume_efeitos = 0.9
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos9"
                elif self.pos_efeitos == "pos9":
                    glob.volume_efeitos = 1
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos10"
                return None
            elif self.tecla == "esquerda":
                if self.pos_efeitos == "pos10":
                    glob.volume_efeitos = 0.9
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos9"
                elif self.pos_efeitos == "pos9":
                    glob.volume_efeitos = 0.8
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos8"
                elif self.pos_efeitos == "pos8":
                    glob.volume_efeitos = 0.7
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos7"
                elif self.pos_efeitos == "pos7":
                    glob.volume_efeitos = 0.6
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos6"
                elif self.pos_efeitos == "pos6":
                    glob.volume_efeitos = 0.5
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos5"
                elif self.pos_efeitos == "pos5":
                    glob.volume_efeitos = 0.4
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos4"
                elif self.pos_efeitos == "pos4":
                    glob.volume_efeitos = 0.3
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos3"
                elif self.pos_efeitos == "pos3":
                    glob.volume_efeitos = 0.2
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos2"
                elif self.pos_efeitos == "pos2":
                    glob.volume_efeitos = 0.1
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos1"
                elif self.pos_efeitos == "pos1":
                    glob.volume_efeitos = 0
                    for e in som.sons:  e.set_volume(glob.volume_efeitos)
                    self.pos_efeitos = "pos0"
                return None

        elif self.opcaoAtual == "musica":
            if self.tecla == "direita":
                if self.pos_musica == "pos0":
                    glob.volume_musica = 0.1
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos1"
                elif self.pos_musica == "pos1":
                    glob.volume_musica = 0.2
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos2"
                elif self.pos_musica == "pos2":
                    glob.volume_musica = 0.3
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos3"
                elif self.pos_musica == "pos3":
                    glob.volume_musica = 0.4
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos4"
                elif self.pos_musica == "pos4":
                    glob.volume_musica = 0.5
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos5"
                elif self.pos_musica == "pos5":
                    glob.volume_musica = 0.6
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos6"
                elif self.pos_musica == "pos6":
                    glob.volume_musica = 0.7
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos7"
                elif self.pos_musica == "pos7":
                    glob.volume_musica = 0.8
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos8"
                elif self.pos_musica == "pos8":
                    glob.volume_musica = 0.9
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos9"
                elif self.pos_musica == "pos9":
                    glob.volume_musica = 1
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos10"
                return None
            elif self.tecla == "esquerda":
                if self.pos_musica == "pos10":
                    glob.volume_musica = 0.9
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos9"
                elif self.pos_musica == "pos9":
                    glob.volume_musica = 0.8
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos8"
                elif self.pos_musica == "pos8":
                    glob.volume_musica = 0.7
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos7"
                elif self.pos_musica == "pos7":
                    glob.volume_musica = 0.6
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos6"
                elif self.pos_musica == "pos6":
                    glob.volume_musica = 0.5
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos5"
                elif self.pos_musica == "pos5":
                    glob.volume_musica = 0.4
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos4"
                elif self.pos_musica == "pos4":
                    glob.volume_musica = 0.3
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos3"
                elif self.pos_musica == "pos3":
                    glob.volume_musica = 0.2
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos2"
                elif self.pos_musica == "pos2":
                    glob.volume_musica = 0.1
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos1"
                elif self.pos_musica == "pos1":
                    glob.volume_musica = 0
                    pygame.mixer.music.set_volume(glob.volume_musica)
                    self.pos_musica = "pos0"
                return None

        if self.tecla == "enter" and self.opcaoAtual == "voltar":
            config['volume'] = {'volume_musica': str(glob.volume_musica),
                                'volume_efeitos': str(glob.volume_efeitos),
                                'posicao_efeitos': self.pos_efeitos,
                                'posicao_musica': self.pos_musica}
            with open('config.ini', 'w') as f:
                config.write(f)
            return "menuConfig"

    def atualizar(self):
        # EFEITOS -----
        if self.pos_efeitos == "pos0" and slider.posicaoX != 292:
            slider.posicaoX = 292
        elif self.pos_efeitos == "pos1" and slider.posicaoX != 337:
            slider.posicaoX = 337
        elif self.pos_efeitos == "pos2" and slider.posicaoX != 382:
            slider.posicaoX = 382
        elif self.pos_efeitos == "pos3" and slider.posicaoX != 429:
            slider.posicaoX = 429
        elif self.pos_efeitos == "pos4" and slider.posicaoX != 474:
            slider.posicaoX = 474
        elif self.pos_efeitos == "pos5" and slider.posicaoX != 520:
            slider.posicaoX = 520
        elif self.pos_efeitos == "pos6" and slider.posicaoX != 565:
            slider.posicaoX = 565
        elif self.pos_efeitos == "pos7" and slider.posicaoX != 610:
            slider.posicaoX = 610
        elif self.pos_efeitos == "pos8" and slider.posicaoX != 655:
            slider.posicaoX = 655
        elif self.pos_efeitos == "pos9" and slider.posicaoX != 700:
            slider.posicaoX = 700
        elif self.pos_efeitos == "pos10" and slider.posicaoX != 745:
            slider.posicaoX = 745

        #MUSICA ------
        if self.pos_musica == "pos0" and slider2.posicaoX != 292:
            slider2.posicaoX = 292
        elif self.pos_musica == "pos1" and slider2.posicaoX != 337:
            slider2.posicaoX = 337
        elif self.pos_musica == "pos2" and slider2.posicaoX != 382:
            slider2.posicaoX = 382
        elif self.pos_musica == "pos3" and slider2.posicaoX != 429:
            slider2.posicaoX = 429
        elif self.pos_musica == "pos4" and slider2.posicaoX != 474:
            slider2.posicaoX = 474
        elif self.pos_musica == "pos5" and slider2.posicaoX != 520:
            slider2.posicaoX = 520
        elif self.pos_musica == "pos6" and slider2.posicaoX != 565:
            slider2.posicaoX = 565
        elif self.pos_musica == "pos7" and slider2.posicaoX != 610:
            slider2.posicaoX = 610
        elif self.pos_musica == "pos8" and slider2.posicaoX != 655:
            slider2.posicaoX = 655
        elif self.pos_musica == "pos9" and slider2.posicaoX != 700:
            slider2.posicaoX = 700
        elif self.pos_musica == "pos10" and slider2.posicaoX != 745:
            slider2.posicaoX = 745

        if self.opcaoAtual == "efeitos" and menuSeta.posicaoY != 100:
            menuSeta.posicaoX = 10
            menuSeta.posicaoY = 200

        elif self.opcaoAtual == "musica" and menuSeta.posicaoY != 280:
            menuSeta.posicaoX = 10
            menuSeta.posicaoY = 280
        if self.opcaoAtual == "voltar" and menuSeta.posicaoY != 520:
            menuSeta.posicaoY = 520
            menuSeta.posicaoX = 210


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
