import pygame
from config import window
from game import game_screen
def main():
    #Função principal do jogo
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption('Castle Insper')
    
    game_screen(window)
    pygame.quit()

if __name__ == '__main__':
    main()