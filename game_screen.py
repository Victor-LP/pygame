# game_screen.py (versão com mapa centralizado)

import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, GRAY, BLOCK_WIDTH, BLOCK_HEIGHT
from assets import load_assets, PLAYER_IMG, BLOCK_IMG
from sprites import Player, Zombie, Tile, MAP, BLOCK

def game_screen(window):
    clock = pygame.time.Clock()
    assets = load_assets()

    groups = {}
    all_sprites = pygame.sprite.Group()
    all_blocks = pygame.sprite.Group()
    all_enemies = pygame.sprite.Group()
    all_attacks = pygame.sprite.Group()

    map_cols = len(MAP[0])
    map_rows = len(MAP)
    map_width_px = map_cols * BLOCK_HEIGHT
    map_height_px = map_rows * BLOCK_WIDTH

    offset_x = (WIDTH - map_width_px) // 2
    offset_y = (HEIGHT - map_height_px) // 2

    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            tile_type = MAP[row][column]
            if tile_type == BLOCK:
                tile = Tile(groups, assets, row, column)
                tile.rect.x += offset_x
                tile.rect.y += offset_y
                all_sprites.add(tile)
                all_blocks.add(tile)

    groups['all_blocks'] = all_blocks
    groups['all_sprites'] = all_sprites
    groups['all_enemies'] = all_enemies
    groups['all_attacks'] = all_attacks

    player = Player(groups, assets)
    zombie = Zombie(groups, assets)
    all_sprites.add(player, zombie)

    running = True
    keys_down = {}
    pygame.key.set_repeat(1, 10)

    while running:
        clock.tick(FPS)
        hits = pygame.sprite.groupcollide(all_enemies, all_attacks, True, True, pygame.sprite.collide_mask)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_a:
                    player.direction = -1
                    player.speedx = 5
                if event.key == pygame.K_d:
                    player.direction = 1
                    player.speedx = 5
                if event.key == pygame.K_w:
                    player.jump()
                if event.key == pygame.K_SPACE:
                    player.attack()
                if event.key == pygame.K_ESCAPE:
                    running = False
            if event.type == pygame.KEYUP:
                if event.key in keys_down:
                    del keys_down[event.key]
                if event.key == pygame.K_a:
                    player.speedx = 0
                if event.key == pygame.K_d:
                    player.speedx = 0
                if event.key == pygame.K_w and player.speedy < 0:
                    player.direction = 0
                    player.speedx = 0

        player.speedy = 5
        all_sprites.update()
        zombie.move_to_player(player, assets)

        window.fill(GRAY)
        all_sprites.draw(window)
        pygame.display.flip()