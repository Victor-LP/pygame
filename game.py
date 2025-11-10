# game_screen.py (versão com mapa centralizado)

import pygame
from config import FPS, GRAY, WIDTH, HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT, MAP, BLOCK
from assets import load_assets,BACKGROUND_IMG
from sprites import Tile, Player, Zombie, Bat, Ghost

def game_screen(window):
    clock = pygame.time.Clock()
    assets = load_assets()

    # Carrega o fundo do jogo
    background = assets[BACKGROUND_IMG]
    # Redimensiona o fundo
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    groups = {}
    all_sprites = pygame.sprite.Group()
    all_blocks = pygame.sprite.Group()
    all_enemies = pygame.sprite.Group()
    all_attacks = pygame.sprite.Group()
    all_players = pygame.sprite.Group()
    
    groups = {
        'all_sprites': all_sprites,
        'all_blocks': all_blocks,
        'all_enemies': all_enemies,
        'all_attacks': all_attacks,
        'all_players': all_players
    }
    
    # ========== CARREGAMENTO DO MAPA ==========
    
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

    # ========== CRIAÇÃO DE ENTIDADES ==========
    # Player
    player = Player(groups, assets, all_blocks)
    all_players.add(player)
    all_sprites.add(player)
    
    # Inimigos
    zombies = [
        Zombie(groups, assets, all_blocks),
        Zombie(groups, assets, all_blocks),
        Zombie(groups, assets, all_blocks)
    ]
    
    bats = [
        Bat(groups, assets),
        Bat(groups, assets)
    ]
    
    ghosts = [
        Ghost(groups, assets, all_blocks),
        Ghost(groups, assets, all_blocks)
    ]
    
    # Adiciona todos os inimigos aos grupos
    for enemy in zombies + bats + ghosts:
        all_sprites.add(enemy)
        all_enemies.add(enemy)

    running = True
    keys_down = {}
    pygame.key.set_repeat(1, 10)

    while running:
        clock.tick(FPS)
        hits = pygame.sprite.groupcollide(all_enemies, all_attacks, True, True, pygame.sprite.collide_mask)
        for hit in hits:
            zombie = Zombie(groups, assets)
            all_sprites.add(zombie)
            all_enemies.add(zombie)
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
        for enemy in all_enemies:
            enemy.move_to_player(player, assets)

        window.fill(GRAY)
        window.blit(background,(0,0))
        all_sprites.draw(window)
        pygame.display.flip()