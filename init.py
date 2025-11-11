import pygame
from config import WIDTH, HEIGHT, FPS, INIT, GAME, QUIT, TUTORIAL
from assets import load_assets, START_IMG, BACKGROUND_IMG, GAME_OVER_IMG, GAME_WON_IMG

def _draw_button(surface, rect, hovered):
    borda = (32, 43, 53) if hovered else (165, 23, 16)
    pygame.draw.rect(surface, borda, rect, width=4, border_radius=8)

def title_screen(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    pygame.mixer.music.stop()
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.load('assets/snd/menu_music.wav')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)


    start_img = assets.get(START_IMG) or assets.get(BACKGROUND_IMG)
    bg = pygame.transform.scale(start_img, (WIDTH, HEIGHT))

    btn_w, btn_h = 395, 120
    btn_rect = pygame.Rect(0, 0, btn_w, btn_h)
    btn_rect.center = (WIDTH // 2.05, int(HEIGHT * 0.645))

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return GAME
                if event.key == pygame.K_ESCAPE:
                    return QUIT
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_rect.collidepoint(pygame.mouse.get_pos()):
                    return TUTORIAL

        window.blit(bg, (0, 0))
        hovered = btn_rect.collidepoint(pygame.mouse.get_pos())
        _draw_button(window, btn_rect, hovered)
        pygame.display.flip()

def game_over_screen(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    pygame.mixer.music.stop()
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.load('assets/snd/game_over.wav')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)

    bg = pygame.transform.scale(assets[GAME_OVER_IMG], (WIDTH, HEIGHT))

    btn_w, btn_h = 325, 120
    btn_rect = pygame.Rect(0, 0, btn_w, btn_h)
    btn_rect.center = (WIDTH // 2.042, int(HEIGHT * 0.628))

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return GAME
                if event.key == pygame.K_ESCAPE:
                    return QUIT
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_rect.collidepoint(pygame.mouse.get_pos()):
                    return GAME

        window.blit(bg, (0, 0))
        hovered = btn_rect.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(window, (255, 0, 0), btn_rect, width=4 if hovered else 2, border_radius=8)
        pygame.display.flip()

def tutorial_screen(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    
    bg = pygame.transform.scale(assets[BACKGROUND_IMG], (WIDTH, HEIGHT))
    
    font = pygame.font.Font(None, 48)
    text_lines = [
        "CONTROLES:",
        "A/D   - Andar esquerda/direita",
        "W     - Pular",
        "SPACE - Atacar",
        "M     - Menu",
        "ESC   - Fechar Jogo",
        "",
        "Pressione ENTER para continuar"
    ]
    
    rendered_lines = [font.render(line, True, (255, 255, 255)) for line in text_lines]
    pygame.mixer.music.fadeout(500)
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return GAME
                if event.key == pygame.K_ESCAPE:
                    return QUIT
        
        window.blit(bg, (0, 0))
        
        y = HEIGHT * 0.25
        for line in rendered_lines:
            rect = line.get_rect(center=(WIDTH // 2, y))
            window.blit(line, rect)
            y += 60
        
        pygame.display.flip()

def game_won_screen(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    pygame.mixer.music.stop()
    pygame.mixer.music.fadeout(1000)
    pygame.mixer.music.load('assets/snd/game_over.wav')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)

    bg = pygame.transform.scale(assets[GAME_WON_IMG], (WIDTH, HEIGHT))

    btn_w, btn_h = 325, 120
    btn_rect = pygame.Rect(0, 0, btn_w, btn_h)
    btn_rect.center = (WIDTH // 2.042, int(HEIGHT * 0.))
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return QUIT
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                    return GAME
                if event.key == pygame.K_ESCAPE:
                    return QUIT
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if btn_rect.collidepoint(pygame.mouse.get_pos()):
                    return GAME

        window.blit(bg, (0, 0))
        hovered = btn_rect.collidepoint(pygame.mouse.get_pos())
        pygame.draw.rect(window, (255, 0, 0), btn_rect, width=4 if hovered else 2, border_radius=8)
        pygame.display.flip()
