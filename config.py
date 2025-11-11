import pygame
from os import path
import random
# ========== DIRETÓRIOS DE ASSETS ==========
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fnt')

# ========== CONFIGURAÇÕES DE JANELA ==========
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
FPS = 60

# ========== CONFIGURAÇÕES DE FÍSICA ==========
GRAVITY = 0.6
JUMP_SIZE = -20
WALK_ANIM_INTERVAL = 200

# ========== CONFIGURAÇÕES DE SPRITES ==========
STD_SCALE = WIDTH/9000
PLAYER_SCALE = STD_SCALE
ZOMBIE_SCALE = 4
GHOST_SCALE = STD_SCALE
BAT_SCALE = 3
ATTACK_SCALE = 4
BLOCK_WIDTH = WIDTH // 17.5
BLOCK_HEIGHT = HEIGHT // 9.72

# ========== CORES ==========
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)

# ========== ESTADOS DO JOGO ==========
INIT = 0
GAME = 1
QUIT = 2
GAME_OVER = 3

# ========== ESTADOS DO PERSONAGEM ==========
STILL = 0
JUMPING = 1
FALLING = 2
ATTACKING = 3
# ========== TIPOS DE TILE ==========
BLOCK = 1
EMPTY = -1

# ========== GERAÇÃO DO MAPA ==========
MAP_WIDTH = 30
MAP_HEIGHT = 200

def generate_map():
    # Cria um mapa vazio
    game_map = [[EMPTY for _ in range(MAP_HEIGHT)] for _ in range(MAP_WIDTH)]
    
    # Cria paredes nas bordas
    for x in range(MAP_WIDTH):
        game_map[x][0] = BLOCK  # Parede superior
        game_map[x][MAP_HEIGHT-1] = BLOCK  # Parede inferior
    
    for y in range(MAP_HEIGHT):
        game_map[0][y] = BLOCK  # Parede esquerda
        game_map[MAP_WIDTH-1][y] = BLOCK  # Parede direita
    
    # Cria chão básico
    for x in range(1, MAP_WIDTH-1):
        game_map[x][MAP_HEIGHT-2] = BLOCK  # Chão principal
    
    # Adiciona plataformas aleatórias
    num_platforms = random.randint(8, 15)
    for _ in range(num_platforms):
        platform_width = random.randint(3, 8)
        platform_height = 1
        platform_x = random.randint(2, MAP_WIDTH - platform_width - 2)
        platform_y = random.randint(5, MAP_HEIGHT - 10)
        
        # Verifica se há espaço suficiente para a plataforma
        valid_position = True
        for x in range(platform_x, platform_x + platform_width):
            if game_map[x][platform_y] != EMPTY:
                valid_position = False
                break
        
        if valid_position:
            for x in range(platform_x, platform_x + platform_width):
                game_map[x][platform_y] = BLOCK
    
    # Adiciona paredes aleatórias
    num_walls = random.randint(5, 10)
    for _ in range(num_walls):
        wall_width = 1
        wall_height = random.randint(2, 6)
        wall_x = random.randint(2, MAP_WIDTH - 3)
        wall_y = random.randint(2, MAP_HEIGHT - wall_height - 2)
        
        # Verifica se há espaço para a parede
        valid_position = True
        for y in range(wall_y, wall_y + wall_height):
            if game_map[wall_x][y] != EMPTY:
                valid_position = False
                break
        
        if valid_position:
            for y in range(wall_y, wall_y + wall_height):
                game_map[wall_x][y] = BLOCK
    
    # Garante que o jogador tenha espaço para começar
    for x in range(1, 5):
        for y in range(MAP_HEIGHT-5, MAP_HEIGHT-1):
            game_map[x][y] = EMPTY
    
    return game_map
MAP = generate_map()