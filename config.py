import pygame
from os import path

# ========== DIRETÓRIOS DE ASSETS ==========
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fnt')

# ========== CONFIGURAÇÕES DE JANELA ==========
pygame.init()
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
FPS = 60

# ========== CONFIGURAÇÕES DE FÍSICA ==========
GRAVITY = 0.6
JUMP_SIZE = -20

# ========== CONFIGURAÇÕES DE SPRITES ==========
PLAYER_SCALE = 4
ZOMBIE_SCALE = 4
SKELETON_SCALE = 4
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

# ========== ESTADOS DO PERSONAGEM ==========
STILL = 0
JUMPING = 1
FALLING = 2

# ========== TIPOS DE TILE ==========
BLOCK = 1
EMPTY = -1

# ========== GERAÇÃO DO MAPA ==========
MAP = []
height = 200
width = 18

for y in range(height):
    row = [EMPTY] * width
    
    # Plataformas principais
    if y % 6 == 0 and y < height - 6:
        level = y // 6
        
        if level % 5 == 0:
            # Buracos no meio
            for x in range(4, width - 4):
                if x < 7 or x > 10:
                    row[x] = BLOCK
        elif level % 5 == 1:
            # Buracos alternados
            for x in range(4, width - 4):
                if x % 2 == 0:
                    row[x] = BLOCK
        elif level % 5 == 2:
            # Dois segmentos separados
            for x in range(4, 8):
                row[x] = BLOCK
            for x in range(10, 14):
                row[x] = BLOCK
        elif level % 5 == 3:
            # Plataforma quebrada
            row[4] = BLOCK
            row[5] = BLOCK
            row[7] = BLOCK
            row[8] = BLOCK
            row[10] = BLOCK
            row[11] = BLOCK
            row[13] = BLOCK
            row[14] = BLOCK
        else:
            # Buraco grande no centro
            for x in range(4, width - 4):
                if x != 8 and x != 9 and x != 10:
                    row[x] = BLOCK
    
    # Plataformas de apoio
    elif (y - 3) % 6 == 0 and y < height - 3:
        level = y // 6
        if level % 3 == 0:
            row[6] = BLOCK
            row[7] = BLOCK
        elif level % 3 == 1:
            row[10] = BLOCK
            row[11] = BLOCK
        else:
            row[4] = BLOCK
            row[13] = BLOCK
    
    # Plataformas flutuantes extras
    elif (y - 1) % 3 == 0 and y > 10 and y < height - 10:
        level = y // 3
        if level % 4 == 0:
            row[2] = BLOCK
            row[15] = BLOCK
        elif level % 4 == 1:
            row[5] = BLOCK
            row[6] = BLOCK
        elif level % 4 == 2:
            row[11] = BLOCK
            row[12] = BLOCK
    
    # Chão sólido
    if y >= height - 5:
        row = [BLOCK] * width
    
    MAP.append(row)