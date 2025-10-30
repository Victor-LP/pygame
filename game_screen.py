import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED
from assets import load_assets, PLAYER_IMG
from sprites import Player

def game_screen(window):
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    assets = load_assets()
    player = Player(all_sprites, assets)
    all_sprites.add(player)
    running = True
    keys_down = {}
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_LEFT:
                    player.image = pygame.transform.flip(assets[PLAYER_IMG], True, False)
                    player.speedx = -5
                if event.key == pygame.K_RIGHT:
                    player.image = assets[PLAYER_IMG]
                    player.speedx = 5
                if event.key == pygame.K_UP:
                    player.jump()
            if event.type == pygame.KEYUP:
                if event.key in keys_down:
                    del keys_down[event.key]
                if event.key == pygame.K_LEFT and player.speedx < 0:
                    player.speedx = 0
                if event.key == pygame.K_RIGHT and player.speedx > 0:
                    player.speedx = 0
                if event.key == pygame.K_UP and player.speedy < 0:
                    player.speedy = 0
                if event.key == pygame.K_DOWN and player.speedy > 0:
                    player.speedy = 0
        player.speedy = 5
        all_sprites.update()
        window.fill(BLACK)
        all_sprites.draw(window)
        pygame.display.flip()