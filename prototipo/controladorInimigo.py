#from personagens import inimigo
from personagens import *
import math


class ControladorInimigo:
    def __init__(self, enemy, caminho):
        self.inimigo = enemy
        self.jogador = jogador
        self.caminho = caminho
        self.posicao_caminho = 1
        self.ultimo_movimento = ""
        self.distancia_percepcao = 300  # pixels
    
    def movimenta(self):
        if self.inimigo.estado == "caminho":
            if math.dist(self.inimigo.rect.center, self.caminho[self.posicao_caminho]) <= self.inimigo.velocidade:
                vetor_movimento = (self.caminho[self.posicao_caminho][0] - self.inimigo.rect.centerx, self.caminho[self.posicao_caminho][1] - self.inimigo.rect.centery)
            else:
                vetor_movimento = self.melhor_caminho(self.caminho[self.posicao_caminho])
            self.inimigo.move(vetor_movimento[0], vetor_movimento[1])
            if abs(vetor_movimento[0]) >= abs(vetor_movimento[1]):
                if vetor_movimento[0] >= 0:
                    self.ultimo_movimento = "direita"
                else:
                    self.ultimo_movimento = "esquerda"
            else:
                if vetor_movimento[1] >= 0:
                    self.ultimo_movimento = "baixo"
                else:
                    self.ultimo_movimento = "cima"
            teste = self.visao()
            if teste:
                self.inimigo.estado_setter("perseguindo")
            else:
                if self.inimigo.rect.center == self.caminho[self.posicao_caminho]:
                    self.posicao_caminho = (self.posicao_caminho + 1) % len(self.caminho)

        elif self.inimigo.estado == "perseguindo":
            vetor_movimento = self.melhor_caminho(self.jogador.rect.center)
            self.inimigo.move(vetor_movimento[0], vetor_movimento[1])
            if math.dist(self.inimigo.rect.center, self.jogador.rect.center) > self.distancia_percepcao:
                self.inimigo.estado_setter("confuso")

        elif self.inimigo.estado == "confuso":
            menor_dist = math.dist(self.inimigo.rect.center, self.caminho[0])
            for i in range(len(self.caminho)):
                dist = math.dist(self.caminho[i], self.inimigo.rect.center)
                if dist < menor_dist:
                    menor_dist = dist
                    self.posicao_caminho = i
            self.inimigo.estado = "caminho"
    
    def movimenta_x(self):
        vetor_movimento = self.melhor_caminho(self.jogador.rect.center)
        self.inimigo.move(vetor_movimento[0], 0)
    
    def movimenta_y(self):
        vetor_movimento = self.melhor_caminho(self.jogador.rect.center)
        self.inimigo.move(0, vetor_movimento[1])

    def melhor_caminho(self, ponto_objetivo):
        vetor_diferenca = (ponto_objetivo[0] - self.inimigo.rect.centerx, ponto_objetivo[1] - self.inimigo.rect.centery)
        modulo_vetor_diferenca = (vetor_diferenca[0]**2 + vetor_diferenca[1]**2)**0.5
        fator = self.inimigo.velocidade / modulo_vetor_diferenca
        vetor_movimento = (round(fator*vetor_diferenca[0]), round(fator*vetor_diferenca[1]))
        return vetor_movimento

    def visao(self):  # coordenadas mudadas para o plano cartesiano padrão
        if math.dist(self.inimigo.rect.center, self.jogador.rect.center) < 1.2 * self.inimigo.raio_de_visao:
            if self.ultimo_movimento == "direita":
                olho = (self.inimigo.rect.right, -self.inimigo.rect.centery) 
                angulo_reta1 = self.inimigo.angulo_de_visao / 2
                angulo_reta2 = 180 - self.inimigo.angulo_de_visao / 2
                reta1 = self.encontra_reta(angulo_reta1, olho)
                reta2 = self.encontra_reta(angulo_reta2, olho)
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.topleft[0], -self.jogador.rect.topleft[1]))
                if (resp1 == "baixo") and (resp2 == "cima"):
                    return True
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.topright[0], -self.jogador.rect.topright[1]))
                if (resp1 == "baixo") and (resp2 == "cima"):
                    return True
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.bottomleft[0], -self.jogador.rect.bottomleft[1]))
                if (resp1 == "baixo") and (resp2 == "cima"):
                    return True
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.bottomright[0], -self.jogador.rect.bottomright[1]))
                if (resp1 == "baixo") and (resp2 == "cima"):
                    return True
                return False
            
            elif self.ultimo_movimento == "esquerda":
                olho = (self.inimigo.rect.left, -self.inimigo.rect.centery) 
                angulo_reta1 = 180 - self.inimigo.angulo_de_visao / 2
                angulo_reta2 = self.inimigo.angulo_de_visao / 2
                reta1 = self.encontra_reta(angulo_reta1, olho)
                reta2 = self.encontra_reta(angulo_reta2, olho)
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.topleft[0], -self.jogador.rect.topleft[1]))
                if (resp1 == "baixo") and (resp2 == "cima"):
                    return True
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.topright[0], -self.jogador.rect.topright[1]))
                if (resp1 == "baixo") and (resp2 == "cima"):
                    return True
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.bottomleft[0], -self.jogador.rect.bottomleft[1]))
                if (resp1 == "baixo") and (resp2 == "cima"):
                    return True
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.bottomright[0], -self.jogador.rect.bottomright[1]))
                if (resp1 == "baixo") and (resp2 == "cima"):
                    return True
                return False

            elif self.ultimo_movimento == "baixo":
                olho = (self.inimigo.rect.centerx, -self.inimigo.rect.bottom)
                angulo_reta1 = 90 - self.inimigo.angulo_de_visao / 2
                angulo_reta2 = 90 + self.inimigo.angulo_de_visao / 2
                reta1 = self.encontra_reta(angulo_reta1, olho)
                reta2 = self.encontra_reta(angulo_reta2, olho)
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.topleft[0], -self.jogador.rect.topleft[1]))
                if (resp1 == "baixo") and (resp2 == "baixo"):
                    return True
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.topright[0], -self.jogador.rect.topright[1]))
                if (resp1 == "baixo") and (resp2 == "baixo"):
                    return True
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.bottomleft[0], -self.jogador.rect.bottomleft[1]))
                if (resp1 == "baixo") and (resp2 == "baixo"):
                    return True
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.bottomright[0], -self.jogador.rect.bottomright[1]))
                if (resp1 == "baixo") and (resp2 == "baixo"):
                    return True
                return False

            elif self.ultimo_movimento == "cima":
                olho = (self.inimigo.rect.centerx, -self.inimigo.rect.top)
                angulo_reta1 = 90 - self.inimigo.angulo_de_visao
                angulo_reta2 = 90 + self.inimigo.angulo_de_visao / 2
                reta1 = self.encontra_reta(angulo_reta1, olho)
                reta2 = self.encontra_reta(angulo_reta2, olho)
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.topleft[0], -self.jogador.rect.topleft[1]))
                if (resp1 == "cima") and (resp2 == "cima"):
                    return True
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.topright[0], -self.jogador.rect.topright[1]))
                if (resp1 == "cima") and (resp2 == "cima"):
                    return True
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.bottomleft[0], -self.jogador.rect.bottomleft[1]))
                if (resp1 == "cima") and (resp2 == "cima"):
                    return True
                resp1, resp2 = self.verifica_ponto_entre_retas(reta1, reta2, (self.jogador.rect.bottomright[0], -self.jogador.rect.bottomright[1]))
                if (resp1 == "cima") and (resp2 == "cima"):
                    return True
                return False
        return False

    def verifica_ponto_entre_retas(self, r1, r2, ponto):
        ponto_relacao_r1 = r1[0]*ponto[0] + r1[1]*ponto[1] + r1[2]
        ponto_relacao_r2 = r2[0]*ponto[0] + r2[1]*ponto[1] + r2[2]
        if ponto_relacao_r1 >= 0:
            resp1 = "cima"
        else:
            resp1 = "baixo"
        if ponto_relacao_r2 >= 0:
            resp2 = "cima"
        else:
            resp2 = "baixo"
        return resp1, resp2
    
    def encontra_reta(self, angulo, ponto):
        angulo_radiano = math.radians(angulo)
        reta = (-math.tan(angulo_radiano), 1)
        c = (-1)*(reta[0]*ponto[0] + reta[1]*ponto[1])
        return (reta[0], reta[1], c)
    

controlador = ControladorInimigo(inimigo, [(100, 250), (350, 250), (350, 450), (350, 250)])
'''
se o caminho não for fechado ele deve ter a seguinte forma:
sejam p1,p2,p3,p4,p5 os ponto pelos quais o inimigo deve passsar
então a definição do caminho fica: [p1,p2,p3,p4,p5,p4,p3,p2]
ou seja todos os pontos entre o último e o primeiro devem ser colocados
de trás para frente no final.
'''
