import pygame
import os

from config import IMG_DIR, SND_DIR, FNT_DIR, PLAYER_SCALE, ZOMBIE_SCALE, ATTACK_SCALE, BLOCK
PLAYER_IMG = 'playerteste1'
ZOMBIE_IMG = 'zumbiteste1'
ATTACK_IMG = 'attackteste1'
def load_assets():
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR,'playerteste1.png')).convert_alpha()
    assets[PLAYER_IMG] = pygame.transform.scale_by(assets[PLAYER_IMG], PLAYER_SCALE)
    assets[ZOMBIE_IMG] = pygame.image.load(os.path.join(IMG_DIR,'zumbiteste1.png')).convert_alpha()
    assets[ZOMBIE_IMG] = pygame.transform.scale_by(assets[ZOMBIE_IMG], ZOMBIE_SCALE)
    assets[BLOCK] = pygame.image.load(os.path.join(IMG_DIR,'blocoteste.png')).convert_alpha()
    assets[BLOCK] = pygame.transform.scale_by(assets[BLOCK],0.15)
    assets[ATTACK_IMG] = pygame.image.load(os.path.join(IMG_DIR,'attackteste1.png')).convert_alpha()
    assets[ATTACK_IMG] = pygame.transform.scale_by(assets[ATTACK_IMG], ATTACK_SCALE)
    return assets