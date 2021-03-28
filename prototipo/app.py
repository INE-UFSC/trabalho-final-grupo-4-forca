from fases import *

faseAtual = menuPrincipal

#   Loop que mantém o jogo aberto.
while jogoAberto:

#   Verificação constante de eventos.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAberto = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                faseAtual.tecla = "baixo"
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                faseAtual.tecla = "cima"
            else:
                faseAtual.tecla = "outra"

            faseAtual.eventos()

    faseAtual.iniciar()
    faseAtual.atualizar()

#   Atualizar os elementos na tela.
    pygame.display.flip()

#   Limitar o FPS do jogo.
    clock.tick(60)

pygame.quit()
