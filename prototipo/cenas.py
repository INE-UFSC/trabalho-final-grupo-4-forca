from menu import *
from variaveisGlobais import *
from jogador import *
from controladorInimigo import *


class Cena:

    def __init__(self):
        self.largura = 800
        self.altura = 600
        self.fundo = ""
        self.tecla = ""
        self.proximaCena = "nenhuma"

    def iniciar(self):
        pass

    def atualizar(self):
        pass


class MenuPrincipal(Cena):

    def __init__(self):
        super().__init__()
        self.fundo = pygame.image.load("../Assets/menuPrincipal/fundo.jpg")
        self.opcaoAtual = "continuar"

#   Evitar que os elementos sejam desenhados mais que uma vez.
    def iniciar(self):
        tela.blit(self.fundo, (0, 0))
        tela.blit(menuTitulo.sprite, (menuTitulo.posicaoX, menuTitulo.posicaoY))
        tela.blit(menuSeta.sprite, (menuSeta.posicaoX, menuSeta.posicaoY))
        tela.blit(menuContinuar.sprite, (menuContinuar.posicaoX, menuContinuar.posicaoY))
        tela.blit(menuNovoJogo.sprite, (menuNovoJogo.posicaoX, menuNovoJogo.posicaoY))
        tela.blit(menuConfiguracoes.sprite, (menuConfiguracoes.posicaoX, menuConfiguracoes.posicaoY))
        tela.blit(menuSair.sprite, (menuSair.posicaoX, menuSair.posicaoY))

    def eventos(self):
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
        elif self.tecla == "enter" and self.opcaoAtual == "novoJogo":
            return "cenarioTeste"
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


cena = Cena()
menuPrincipal = MenuPrincipal()
cenarioTeste = CenarioTeste()
