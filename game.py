import pygame
from config import FPS, GRAY, WIDTH, HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT, MAP, BLOCK, GAME_OVER
from assets import load_assets
from sprites import Tile, Player, Zombie, Bat, Ghost
import random

def game_screen(window):
    # ========== INICIALIZAÇÃO ==========
    clock = pygame.time.Clock()
    assets = load_assets()
    background = pygame.transform.scale(assets['background'], (WIDTH, HEIGHT))
    player_alive = True
    # ========== GRUPOS DE SPRITES ==========
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
    map_width_px = map_cols * BLOCK_WIDTH  # Corrigido: era BLOCK_HEIGHT
    map_height_px = map_rows * BLOCK_HEIGHT  # Corrigido: era BLOCK_WIDTH
    offset_x = (WIDTH - map_width_px) // 2
    offset_y = (HEIGHT - map_height_px) // 2

    for row in range(len(MAP)):
        for column in range(len(MAP[row])):
            if MAP[row][column] == BLOCK:
                tile = Tile(groups, assets, row, column)
                tile.rect.x += offset_x
                tile.rect.y += offset_y
                all_sprites.add(tile)
                all_blocks.add(tile)

    # ========== CRIAÇÃO DE ENTIDADES ==========
    # Player - POSICIONADO NO CANTO INFERIOR ESQUERDO DO MAPA
    player = Player(groups, assets, all_blocks)
    
    # Posiciona o player no canto inferior esquerdo do mapa (dentro da área jogável)
    player_start_x = offset_x + BLOCK_WIDTH * 2  # 2 blocos a partir da borda esquerda
    player_start_y = offset_y + map_height_px - BLOCK_HEIGHT * 2  # 2 blocos acima do fundo
    
    player.rect.x = player_start_x
    player.rect.bottom = player_start_y  # Usa bottom para alinhar com o "chão"
    
    all_players.add(player)
    all_sprites.add(player)

    # ==== MUITOS INIMIGOS NO TOPO ====
    for i in range(20):  # ajuste a quantidade
        enemy = random.choice([Zombie(groups, assets, all_blocks),
                           Ghost(groups, assets, all_blocks),
                           Bat(groups, assets, all_blocks)])
    # posição aleatória no topo
        enemy.rect.x = random.randint(0, WIDTH)
        enemy.rect.y = random.randint(0, HEIGHT)  # topo da tela
        all_sprites.add(enemy)
        all_enemies.add(enemy)

    # ========== LOOP PRINCIPAL ==========
    running = True
    keys_down = {}
    pygame.key.set_repeat(1, 10)
    pygame.mixer.music.play(loops=-1)
    while running:
        # ===== CÂMERA =====
        camera_x = -player.rect.centerx + WIDTH // 2
        camera_y = -player.rect.centery + HEIGHT // 2
        clock.tick(FPS)
        
        # ========== PROCESSAMENTO DE EVENTOS ==========
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                
                if event.key == pygame.K_a:
                    player.direction = -1
                    player.looking = -1
                elif event.key == pygame.K_d:
                    player.direction = 1
                    player.looking = 1
                elif event.key == pygame.K_w:
                    player.jump()
                elif event.key == pygame.K_SPACE:
                    player.attack(assets)
                elif event.key == pygame.K_ESCAPE:
                    running = False
            
            elif event.type == pygame.KEYUP:
                if event.key in keys_down:
                    del keys_down[event.key]
                if event.key in (pygame.K_a, pygame.K_d):
                    player.direction = 0

        # ========== ATUALIZAÇÃO DO JOGO ==========
        all_sprites.update()
        
        # Movimento dos inimigos em direção ao jogador
        for enemy in all_enemies:
            enemy.move_to_player(player, assets)
        
        # Detecção de colisões
        pygame.sprite.groupcollide(all_enemies, all_attacks, True, True, pygame.sprite.collide_mask)
        hits = pygame.sprite.groupcollide(all_enemies, all_players, False, False, pygame.sprite.collide_mask)
        if hits:
            player_alive = player.hit()
        if not player_alive:
            return GAME_OVER

        # ========== RENDERIZAÇÃO ==========
        window.fill(GRAY)
        window.blit(background, (0, 0))
        
        # Câmera segue o jogador
        camera_x = -player.rect.centerx + WIDTH // 2
        camera_y = -player.rect.centery + HEIGHT // 2
        
        for sprite in all_sprites:
            window.blit(sprite.image, (sprite.rect.x + camera_x, sprite.rect.y + camera_y))
        font = pygame.font.Font(None, 36)
        hp_text = font.render(f"HP: {player.hp}", True, (255, 0, 0))
        window.blit(hp_text, (10, 10))
        pygame.display.flip()
    return GAME_OVER