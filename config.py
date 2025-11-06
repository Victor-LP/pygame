from os import path
#assets path
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'fnt')
#dados gerais
WIDTH = 1000
HEIGHT = 715
FPS = 60
GRAVITY = 0.6
#tamanhos dos sprites
PLAYER_SCALE = 4
ZOMBIE_SCALE = 4
SKELETON_SCALE = 4
BAT_SCALE = 3
ATTACK_SCALE = 4
BLOCK_HEIGHT = 45
BLOCK_WIDTH = 45
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
BLOCK = 1
EMPTY = -1