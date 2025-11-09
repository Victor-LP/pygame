# game_screen.py (versão com mapa centralizado)

import pygame
from config import FPS, BLACK, YELLOW, RED, WIDTH,HEIGHT,GRAY, BLOCK_WIDTH, BLOCK_HEIGHT, MAP, BLOCK
from assets import load_assets, PLAYER_IMG, BLOCK_IMG, BACKGROUND_IMG
from sprites import Player, Zombie, Bat, Skeleton, Tile

def game_screen(window):
    clock = pygame.time.Clock()
    assets = load_assets()
    background = assets[BACKGROUND_IMG]
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    groups = {}
    all_sprites = pygame.sprite.Group()
    all_blocks = pygame.sprite.Group()
    all_enemies = pygame.sprite.Group()
    all_attacks = pygame.sprite.Group()
    all_players = pygame.sprite.Group()
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
    groups['all_players'] = all_players

#Player
    player = Player(groups, assets, all_blocks)
    all_players.add(player)
#Zombies
    zombie1 = Zombie(groups, assets, all_blocks)
    zombie2 = Zombie(groups, assets, all_blocks)
    zombie3 = Zombie(groups, assets, all_blocks)

    all_sprites.add(player, zombie1, zombie2, zombie3)
    all_enemies.add(zombie1,zombie2,zombie3)
#Bats
    bat1 = Bat(groups, assets)
    bat2 = Bat(groups, assets)
    all_sprites.add(bat1, bat2)
    all_enemies.add(bat1, bat2)
#Skeleton
    skeleton1 = Skeleton(groups, assets)
    skeleton2 = Skeleton(groups, assets)
    all_sprites.add(skeleton1, skeleton2)
    all_enemies.add(skeleton1, skeleton2)

    running = True
    keys_down = {}
    pygame.key.set_repeat(1, 10)
    camera_y = 0
    while running:
        clock.tick(FPS)
        hits = pygame.sprite.groupcollide(all_enemies, all_attacks, True, True, pygame.sprite.collide_mask)
        hits = pygame.sprite.groupcollide(all_players, all_enemies,True,True, pygame.sprite.collide_mask)
        for hit in hits:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_a:
                    player.direction = -1
                    player.looking = -1
                if event.key == pygame.K_d:
                    player.direction = 1
                    player.looking = 1
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
                    player.direction = 0
                if event.key == pygame.K_d:
                    player.direction = 0
        all_sprites.update()
        camera_y = -player.rect.centery + HEIGHT // 2
        for enemy in all_enemies:
            enemy.move_to_player(player, assets)

        window.fill(GRAY)
        window.blit(background,(0,0))
        for sprite in all_sprites:
            window.blit(sprite.image, (sprite.rect.x, sprite.rect.y + camera_y))
        pygame.display.flip()