from os import path
#assets path
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fnt')
#dados gerais
WIDTH = 1000
HEIGHT = 600
FPS = 60
#tamanhos dos sprites
# PLAYER_WIDTH = 200
# PLAYER_HEIGHT = 200
# SKELETON_WIDTH = 200
# SKELETON_HEIGHT = 200
# ZOMBIE_WIDTH = 200
# ZOMBIE_HEIGHT = 200
# BATS_WIDTH = 100
# BATS_HEIGHT = 100
# BOSS_WIDTH = 300
# BOSS_HEIGHT = 300
PLAYER_SCALE = 4
ZOMBIE_SCALE = 4
ATTACK_SCALE = 4
#cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)
#estados de jogo
INIT = 0
GAME = 1
QUIT = 2


BLOCK = 0
EMPTY = -1