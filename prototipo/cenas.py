from menu import *
from variaveisGlobais import *
from jogador import *
from controladorInimigo import *
from pathlib import Path

class Cena:

    def __init__(self):
        self.largura = largura
        self.altura = altura
        self.fundo = ""
        self.tecla = ""
        self.proximaCena = "nenhuma"

    def iniciar(self):
        pass

    def atualizar(self):
        pass


class MenuPrincipal(Cena):

    def __init__(self):
        save = Path("saves/save.txt")
        exist = 0
        if save.is_file():
            exist = 1
        super().__init__()
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
            return "cenarioTeste"
        elif self.tecla == "enter" and self.opcaoAtual == "configuracoes":
            return "menuConfig"
        elif self.tecla == "enter" and self.opcaoAtual == "sair":
            return "fecharJogo"

    def atualizar(self):
        if self.opcaoAtual == "continuar" and menuSeta.posicaoY != 200:
            menuSeta.posicaoY = 200
        elif self.opcaoAtual == "novoJogo" and menuSeta.posicaoY != 280:
            menuSeta.posicaoY = 280
        elif self.opcaoAtual == "configuracoes" and menuSeta.posicaoY != 360:
            menuSeta.posicaoY = 360
        elif self.opcaoAtual == "sair" and menuSeta.posicaoY != 440:
            menuSeta.posicaoY = 440


class MenuConfig(Cena):

    def __init__(self):
        super().__init__()
        self.fundo = bkg
        self.opcaoAtual = "volume"

    def iniciar(self):
        tela.blit(self.fundo, (0, 0))
        tela.blit(menuTitulo.sprite, (menuTitulo.posicaoX, menuTitulo.posicaoY))
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
        self.opcaoAtual = "voltar"

    def iniciar(self):
        tela.blit(self.fundo, (0, 0))
        tela.blit(menuTitulo.sprite, (menuTitulo.posicaoX, menuTitulo.posicaoY))
        tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        tela.blit(controls_info.sprite, (controls_info.posicaoX, controls_info.posicaoY))
        tela.blit(menuVoltar2.sprite, (menuVoltar2.posicaoX, menuVoltar2.posicaoY))

    def eventos(self):
        if self.tecla == "enter" and self.opcaoAtual == "voltar":
            return "menuConfig"

    def atualizar(self):
        if self.opcaoAtual == "voltar" and menuSeta.posicaoY != 440:
            menuSeta.posicaoY = 440


class Saguao(Cena):

    def __init__(self, largura, altura):
        super().__init__()
        self.largura = largura
        self.altura = altura


class CenarioTeste(Cena):
    def __init__(self):
        super().__init__()
        self.fundo = pygame.Surface((self.largura, self.altura))
        self.parede = pygame.Surface((200,100))
        self.parede.fill(vermelho)
        self.parede0rect = self.parede.get_rect(topleft = (100, 100))
        self.parede1rect = self.parede.get_rect(topleft = (100, 300))
        self.parede2rect = self.parede.get_rect(topleft = (100, 500))
        self.lista_parederect = [self.parede0rect, self.parede1rect, self.parede2rect]
    
    def iniciar(self):
        tela.blit(self.fundo, (0,0))
        tela.blit(self.parede, (100,100))
        tela.blit(self.parede, (100, 300))
        tela.blit(self.parede, (100, 500))
        tela.blit(jogador.surf, jogador.rect)
        tela.blit(inimigo.surf, inimigo.rect)
    
    def eventos(self):
        jogador.move(self.tecla)
        for retangulo in self.lista_parederect:
            if jogador.rect.colliderect(retangulo):
                jogador.resgata_posicao()
        if jogador.rect.colliderect(inimigo.rect):
            jogador.resgata_posicao()
        controlador.movimenta()
        for retangulo in self.lista_parederect:
            if inimigo.rect.colliderect(retangulo):
                inimigo.resgata_posicao()
        if inimigo.rect.colliderect(jogador.rect):
            inimigo.resgata_posicao()
        if self.tecla=="e":
            return "inventario"
    def atualizar(self):
        pass


class MenuInventario(Cena):
    def __init__(self):
        super().__init__()
        self.fundo = pygame.Surface((self.largura, self.altura))
        self.container = pygame.Surface((100, 100))
        self.container.fill((127, 127, 127))
        self.selectedBox = pygame.Surface((100, 100))
        self.selectedBox.fill((191, 191, 191))
        self.box_x = 150
        self.box_y = 100
        self.itemindex = 0

    def iniciar(self):
        tela.blit(self.fundo, (0, 0))
        for i in range (0, 4):
            for j in range (0, 5):
                tela.blit(self.container, (((j*100)+150), ((i*100)+100)))
        tela.blit(self.selectedBox, (self.box_x, self.box_y))
        for i in range (0, 4):
            for j in range (0, 5):
                if jogador.inventario[(i * 5) + j] != None:
                    tela.blit(jogador.inventario[(i * 5) + j].image, (((j * 100) + 150), ((i * 100) + 100)))

    def eventos(self):
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

    def atualizar(self):
        pass


cena = Cena()
menuPrincipal = MenuPrincipal()
cenarioTeste = CenarioTeste()
menuConfig = MenuConfig()
menuControles = MenuControles()
menuInventario = MenuInventario()
