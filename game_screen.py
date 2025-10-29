import sprites
import pygame
from config import *
pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("CastleInsper")

clock = pygame.time.Clock()
FPS = 60

DONE = 0
PLAYING = 1
EXPLODING = 2
state = PLAYING
score = 0
keys_down = {}

jogador = sprites.Jogador()
while state != DONE:
    clock.tick(FPS)
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            state = DONE
        # Só verifica o teclado se está no estado de jogo
        if state == PLAYING:
            # Verifica se apertou alguma tecla.
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_LEFT:
                    sprites.Jogador.speedx -= 8
                if event.key == pygame.K_RIGHT:
                    sprites.Jogador.speedx += 8
                if event.key == pygame.K_UP:
                    sprites.Jogador.speedy +=3
    sprites.Jogador.update()
pygame.quit()