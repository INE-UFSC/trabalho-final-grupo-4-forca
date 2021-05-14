from variaveisGlobais import glob
import pygame
import menu

porta_som = pygame.mixer.Sound("../Assets/sons/porta.mp3")
porta_som.set_volume(glob.volume_efeitos)

passos = pygame.mixer.Sound("../Assets/sons/passos.wav")
passos.set_volume(glob.volume_efeitos)

monstro1 = pygame.mixer.Sound("../Assets/sons/monstro.mp3")
monstro1.set_volume(glob.volume_efeitos)

monstro2 = pygame.mixer.Sound("../Assets/sons/rugido.mp3")
monstro2.set_volume(glob.volume_efeitos)

puzzle_cozinha = pygame.mixer.Sound("../Assets/sons/puzzle_porta.ogg")
puzzle_cozinha.set_volume(glob.volume_efeitos)

vela = pygame.mixer.Sound("../Assets/sons/vela.wav")
vela.set_volume(glob.volume_efeitos)

pegar_item = pygame.mixer.Sound("../Assets/sons/pegar_item.wav")
pegar_item.set_volume(glob.volume_efeitos)

sons = [porta_som, passos, monstro1, monstro2, vela, pegar_item]

def music_ambiente():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("../Assets/musicas/ambiente.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(glob.volume_musica)

def music_fugir():
    pygame.mixer.music.stop()
    pygame.mixer.music.load("../Assets/musicas/fugir.ogg")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(glob.volume_musica)

