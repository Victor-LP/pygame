import pygame
from config import IMG_DIR, BLACK, FPS, GAME, QUIT
from os import path
def init_screen(window):
    clock = pygame.time.Clock()
    background = pygame.image.load(path.join(IMG_DIR,'tela_inicial.png')).convert()
    background_rect = background.get_rect()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    state = QUIT
                    running = False
                else:
                    state = GAME
                    running = False
                    
        window.fill(BLACK)
        window.blit(background, background_rect)
        pygame.display.flip()
    return state