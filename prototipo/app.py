from cenas import *

cenaAtual = menuPrincipal
p = None
cenarioAtual = "menu"
#   Loop que mantém o jogo aberto.
while jogoAberto:
    cenaAtual.tecla = "outra"

#   Verificação constante de eventos.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAberto = False
        elif cenarioAtual == "menu" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                cenaAtual.tecla = "baixo"
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                cenaAtual.tecla = "cima"
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                cenaAtual.tecla = "esquerda"
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                cenaAtual.tecla = "direita"
            elif event.key == pygame.K_RETURN:
                cenaAtual.tecla = "enter"

    if cenarioAtual == "jogo":
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_s] or pressed[pygame.K_DOWN]:
            cenaAtual.tecla = "baixo"
        elif pressed[pygame.K_w] or pressed[pygame.K_UP]:
            cenaAtual.tecla = "cima"
        elif pressed[pygame.K_a] or pressed[pygame.K_LEFT]:
            cenaAtual.tecla = "esquerda"
        elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            cenaAtual.tecla = "direita"
        elif pressed[pygame.K_RETURN]:
            cenaAtual.tecla = "enter"
                       

    p = cenaAtual.eventos()

    cenaAtual.iniciar()
    cenaAtual.atualizar()

#   Atualizar os elementos na tela.
    pygame.display.flip()
    if p == "cenarioteste":
        cenaAtual = cenarioteste
        cenarioAtual = "jogo"

#   Limitar o FPS do jogo.
    clock.tick(60)

pygame.quit()
