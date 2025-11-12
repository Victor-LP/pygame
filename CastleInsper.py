import pygame
from config import window, INIT, QUIT, GAME, GAME_OVER, TUTORIAL, GAME_WON
from game import game_screen
from init import title_screen, game_over_screen, tutorial_screen, game_won_screen
def main():
    #Função principal do jogo
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Castle Insper')
    state = GAME_OVER
    while state != QUIT:
        if state == INIT:
            state = title_screen(window)
        elif state == GAME:
            pygame.mixer.music.stop()
            state = game_screen(window)
        elif state == GAME_OVER:
            state = game_over_screen(window)
        elif state == TUTORIAL:
            state = tutorial_screen(window)
        elif state == GAME_WON:
            state = game_won_screen(window)
        else:
            state = QUIT
    pygame.quit()

main()