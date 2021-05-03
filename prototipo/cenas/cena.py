from ..variaveisGlobais import glob


class Cena:

    def __init__(self):
        self.largura = glob.tamanhoTela[0]
        self.altura = glob.tamanhoTela[1]
        self.fundo = ""
        self.tecla = ""
        self.proximaCena = "nenhuma"
        self.iniciou = False

    def iniciar(self):
        pass

    def atualizar(self):
        pass
        #atualizarGroups()