from ..variaveisGlobais import glob


class Cena:

    def __init__(self):
        self.largura = glob.tamanhoTela[0]
        self.altura = glob.tamanhoTela[1]
        self.fundo = ""
        self.tecla = ""
        self.cenaJogavel = False
        self.proximaCena = "nenhuma"
        self.iniciou = False
        self.delay = 10

    def iniciar(self):
        pass

    def eventos(self):
        pass

    def atualizar(self):
        pass