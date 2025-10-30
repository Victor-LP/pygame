import pygame
import os
from config import PLAYER_WIDTH, PLAYER_HEIGHT, SKELETON_WIDTH, SKELETON_HEIGHT, ZOMBIE_WIDTH, ZOMBIE_HEIGHT, BATS_WIDTH, BATS_HEIGHT, BOSS_WIDTH, BOSS_HEIGHT, IMG_DIR, SND_DIR, FNT_DIR
PLAYER_IMG = 'idle1'
def load_assets():
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR,'idle1.png')).convert_alpha()
    assets[PLAYER_IMG] = pygame.transform.scale(assets[PLAYER_IMG], (PLAYER_WIDTH, PLAYER_HEIGHT))
    return assets