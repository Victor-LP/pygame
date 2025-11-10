import pygame
from config import window, INIT, QUIT, GAME
from game import game_screen
from init import title_screen
def main():
    #Função principal do jogo
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Castle Insper')
    state = INIT
    while state != QUIT:
        if state == INIT:
            state = title_screen(window)
        elif state == GAME:
            state = game_screen(window)
        else:
            state = QUIT
    pygame.quit()

main()