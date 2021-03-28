from cenas import *

cenaAtual = menuPrincipal

#   Loop que mantém o jogo aberto.
while jogoAberto:

#   Verificação constante de eventos.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAberto = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                cenaAtual.tecla = "baixo"
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                cenaAtual.tecla = "cima"
            else:
                cenaAtual.tecla = "outra"

            cenaAtual.eventos()

    cenaAtual.iniciar()
    cenaAtual.atualizar()

#   Atualizar os elementos na tela.
    pygame.display.flip()

#   Limitar o FPS do jogo.
    clock.tick(60)

pygame.quit()
