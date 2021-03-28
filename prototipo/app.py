from menu import *
from variaveisGlobais import *

#   Loop que mantém o jogo aberto.
while jogoAberto:

#   Verificação constante de eventos.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogoAberto = False

#   Evitar que os elementos sejam desenhados mais que uma vez.
    if not menu.elementosMostrados:
        tela.blit(menu.sprite, (menu.posicaoX, menu.posicaoY))

        tela.blit(menuContinuar.sprite, (menuContinuar.posicaoX, menuContinuar.posicaoY))
        tela.blit(menuNovoJogo.sprite, (menuNovoJogo.posicaoX, menuNovoJogo.posicaoY))
        tela.blit(menuConfiguracoes.sprite, (menuConfiguracoes.posicaoX, menuConfiguracoes.posicaoY))
        tela.blit(menuSair.sprite, (menuSair.posicaoX, menuSair.posicaoY))
        menu.elementosMostrados = True

#   Atualizar os elementos na tela.
    pygame.display.flip()

#   Limitar o FPS do jogo.
    clock.tick(60)

pygame.quit()
