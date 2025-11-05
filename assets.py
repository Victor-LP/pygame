import pygame
import os

from config import IMG_DIR, SND_DIR, FNT_DIR, PLAYER_SCALE, ZOMBIE_SCALE, BAT_SCALE, ATTACK_SCALE, BLOCK_HEIGHT, BLOCK_WIDTH
PLAYER_IMG = 'playerteste1'
ZOMBIE_IMG = 'zumbiteste1'
BAT_IMG = 'morcegoteste1'
ATTACK_IMG = 'attackteste1'
BLOCK_IMG = 'blocoteste'
def load_assets():
    assets = {}
    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR,'playerteste1.png')).convert_alpha()
    assets[PLAYER_IMG] = pygame.transform.scale_by(assets[PLAYER_IMG], PLAYER_SCALE)
    assets[ZOMBIE_IMG] = pygame.image.load(os.path.join(IMG_DIR,'zumbiteste1.png')).convert_alpha()
    assets[ZOMBIE_IMG] = pygame.transform.scale_by(assets[ZOMBIE_IMG], ZOMBIE_SCALE)
    assets[BLOCK_IMG] = pygame.image.load(os.path.join(IMG_DIR,'blocoteste.png')).convert_alpha()
    assets[BLOCK_IMG] = pygame.transform.scale(assets[BLOCK_IMG], (BLOCK_WIDTH,BLOCK_HEIGHT))
    assets[ATTACK_IMG] = pygame.image.load(os.path.join(IMG_DIR,'attackteste1.png')).convert_alpha()
    assets[ATTACK_IMG] = pygame.transform.scale_by(assets[ATTACK_IMG], ATTACK_SCALE)
    assets[BAT_IMG] = pygame.image.load(os.path.join(IMG_DIR,'morcegoteste1.png')).convert_alpha()
    assets[BAT_IMG] = pygame.transform.scale_by(assets[BAT_IMG], BAT_SCALE)
    return assets