import pygame
from config import WIDTH, HEIGHT, FPS, INIT, GAME, QUIT, TUTORIAL
from assets import load_assets, START_IMG, BACKGROUND_IMG, GAME_OVER_IMG, GAME_WON_IMG, FONTE

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

    btn_w, btn_h = 409, 122
    btn_rect = pygame.Rect(0, 0, btn_w, btn_h)
    btn_rect.center = (WIDTH // 2.035, int(HEIGHT * 0.649))

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

    btn_w, btn_h = 315, 120
    btn_rect = pygame.Rect(0, 0, btn_w, btn_h)
    btn_rect.center = (WIDTH // 2.027, int(HEIGHT * 0.634))

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
    
    text_lines = [
        "CONTROLES",
        "A e D para se Mover para esquerda ou direita",
        "W para Pular",
        "SPACE para Atacar",
        "M para Abrir o Menu",
        "ESC para Fechar o Jogo",
        "",
        "Pressione ENTER para continuar"
    ]
    
    rendered_lines = [assets[FONTE].render(line, True, (255, 255, 255)) for line in text_lines]
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

    btn_w, btn_h = 495, 95
    #PLAY AGAIN
    btn_play_rect = pygame.Rect(0, 0, btn_w, btn_h)
    btn_play_rect.center = (WIDTH // 2, int(HEIGHT * 0.775))
    #QUIT
    btn_rect = pygame.Rect(0, 0, btn_w, btn_h)
    btn_rect.center = (WIDTH // 2, int(HEIGHT * 0.90))

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
                if btn_play_rect.collidepoint(pygame.mouse.get_pos()):
                    return GAME
                elif btn_rect.collidepoint(pygame.mouse.get_pos()):
                    return QUIT


        window.blit(bg, (0, 0))
        hovered_play = btn_play_rect.collidepoint(pygame.mouse.get_pos())
        hovered_quit = btn_rect.collidepoint(pygame.mouse.get_pos())

        pygame.draw.rect(window, (255, 0, 0) if hovered_play else (165, 23, 16), btn_play_rect, width=4, border_radius=8)
        pygame.draw.rect(window, (255, 0, 0) if hovered_quit else (165, 23, 16), btn_rect, width=4, border_radius=8)

        pygame.display.flip()
