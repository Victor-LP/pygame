import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR, PLAYER_SCALE, ZOMBIE_SCALE
PLAYER_IMG = 'playerteste1'
ZOMBIE_IMG = 'zumbiteste1'
def load_assets():
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR,'playerteste1.png')).convert_alpha()
    assets[PLAYER_IMG] = pygame.transform.scale_by(assets[PLAYER_IMG], PLAYER_SCALE)
    assets[ZOMBIE_IMG] = pygame.image.load(os.path.join(IMG_DIR,'zumbiteste1.png')).convert_alpha()
    assets[ZOMBIE_IMG] = pygame.transform.scale_by(assets[ZOMBIE_IMG], ZOMBIE_SCALE)
    return assets