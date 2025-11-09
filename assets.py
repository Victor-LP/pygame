import pygame
import os
from config import IMG_DIR, PLAYER_SCALE, ZOMBIE_SCALE, BAT_SCALE, SKELETON_SCALE, ATTACK_SCALE, BLOCK_HEIGHT, BLOCK_WIDTH

# ========== CONSTANTES DE IMAGENS ==========
PLAYER_IMG = 'player'
ZOMBIE_IMG = 'zombie'
BAT_IMG1 = 'bat1'
BAT_IMG2 = 'bat2'
BAT_IMG3 = 'bat3'
SKELETON_IMG = 'skeleton'
ATTACK_IMG = 'attack'
BLOCK_IMG = 'block'
BACKGROUND_IMG = 'background'

def load_assets():
    #Carrega e escala todos os assets do jogo
    assets = {}
    
    # ========== CARREGAMENTO DE IMAGENS ==========
    # Player
    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'playerteste1.png')).convert_alpha()
    assets[PLAYER_IMG] = pygame.transform.scale_by(assets[PLAYER_IMG], PLAYER_SCALE)
    
    # Inimigos
    assets[ZOMBIE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'zumbiteste1.png')).convert_alpha()
    assets[ZOMBIE_IMG] = pygame.transform.scale_by(assets[ZOMBIE_IMG], ZOMBIE_SCALE)
    
    assets[SKELETON_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'esqueletoteste1.png')).convert_alpha()
    assets[SKELETON_IMG] = pygame.transform.scale_by(assets[SKELETON_IMG], SKELETON_SCALE)
    
    # Morcegos (animação)
    assets[BAT_IMG1] = pygame.image.load(os.path.join(IMG_DIR, 'morcegoteste1.png')).convert_alpha()
    assets[BAT_IMG1] = pygame.transform.scale_by(assets[BAT_IMG1], BAT_SCALE)
    
    assets[BAT_IMG2] = pygame.image.load(os.path.join(IMG_DIR, 'morcegoteste2.png')).convert_alpha()
    assets[BAT_IMG2] = pygame.transform.scale_by(assets[BAT_IMG2], BAT_SCALE)
    
    assets[BAT_IMG3] = pygame.image.load(os.path.join(IMG_DIR, 'morcegoteste3.png')).convert_alpha()
    assets[BAT_IMG3] = pygame.transform.scale_by(assets[BAT_IMG3], BAT_SCALE)
    
    # Ataque
    assets[ATTACK_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'attackteste1.png')).convert_alpha()
    assets[ATTACK_IMG] = pygame.transform.scale_by(assets[ATTACK_IMG], ATTACK_SCALE)
    
    # Blocos e cenário
    assets[BLOCK_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'blocoteste.png')).convert_alpha()
    assets[BLOCK_IMG] = pygame.transform.scale(assets[BLOCK_IMG], (BLOCK_WIDTH, BLOCK_HEIGHT))
    
    assets[BACKGROUND_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'background.png')).convert_alpha()
    
    return assets