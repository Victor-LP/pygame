import pygame
import os
from config import IMG_DIR, PLAYER_SCALE, ZOMBIE_SCALE, BAT_SCALE, GHOST_SCALE, ATTACK_SCALE, BLOCK_HEIGHT, BLOCK_WIDTH

# ========== CONSTANTES DE IMAGENS E EFEITOS SONOROS ==========
PLAYER_IMG = 'player'
PLAYER_JUMP_IMG = 'player_jump'
PLAYER_ATTACK_IMG = 'player_attack'
PLAYER_WALK1_IMG = 'player_walk1'
PLAYER_WALK2_IMG = 'player_walk2'
PLAYER_WALK3_IMG = 'player_walk3'
ZOMBIE_IMG = 'zombie'
ZOMBIE_IMG2 = 'zombie2'
BAT_IMG1 = 'bat1'
BAT_IMG2 = 'bat2'
BAT_IMG3 = 'bat3'
GHOST_IMG = 'ghost'
ATTACK_IMG = 'attack'
BLOCK_IMG = 'block'
BACKGROUND_IMG = 'background'
SOM_ESPADA = 'som_espada'
SOM_PULO = 'som_pulo'
SOM_DANO = 'som_dano'
START_IMG = 'startimage'
GAME_OVER_IMG = 'game_over'
def load_assets():
    #Carrega e escala todos os assets do jogo
    assets = {}
    
    # ========== CARREGAMENTO DE IMAGENS ==========
    # Player
    assets[PLAYER_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'player.png')).convert_alpha()
    assets[PLAYER_IMG] = pygame.transform.scale_by(assets[PLAYER_IMG], PLAYER_SCALE)
    assets[PLAYER_JUMP_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'playerjump.png')).convert_alpha()
    assets[PLAYER_JUMP_IMG] = pygame.transform.scale_by(assets[PLAYER_JUMP_IMG], PLAYER_SCALE)
    assets[PLAYER_ATTACK_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'playerattack.png')).convert_alpha()
    assets[PLAYER_ATTACK_IMG] = pygame.transform.scale_by(assets[PLAYER_ATTACK_IMG], PLAYER_SCALE)
    assets[PLAYER_WALK1_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'playerwalk1.png'))
    assets[PLAYER_WALK1_IMG] = pygame.transform.scale_by(assets[PLAYER_WALK1_IMG], PLAYER_SCALE)
    assets[PLAYER_WALK2_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'playerwalk2.png'))
    assets[PLAYER_WALK2_IMG] = pygame.transform.scale_by(assets[PLAYER_WALK2_IMG], PLAYER_SCALE)
    assets[PLAYER_WALK3_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'playerwalk3.png'))
    assets[PLAYER_WALK3_IMG] = pygame.transform.scale_by(assets[PLAYER_WALK3_IMG], PLAYER_SCALE)
    
    # Inimigos
    assets[ZOMBIE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'zombie.png')).convert_alpha()
    assets[ZOMBIE_IMG] = pygame.transform.scale_by(assets[ZOMBIE_IMG], ZOMBIE_SCALE)
    assets[ZOMBIE_IMG2] = pygame.image.load(os.path.join(IMG_DIR, 'zombie2.png')).convert_alpha()
    assets[ZOMBIE_IMG2] = pygame.transform.scale_by(assets[ZOMBIE_IMG2], ZOMBIE_SCALE)
    
    assets[GHOST_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'ghost.png')).convert_alpha()
    assets[GHOST_IMG] = pygame.transform.scale_by(assets[GHOST_IMG], GHOST_SCALE)
    
    # Morcegos (animação)
    assets[BAT_IMG1] = pygame.image.load(os.path.join(IMG_DIR, 'morcegoteste1.png')).convert_alpha()
    assets[BAT_IMG1] = pygame.transform.scale_by(assets[BAT_IMG1], BAT_SCALE)
    
    assets[BAT_IMG2] = pygame.image.load(os.path.join(IMG_DIR, 'morcegoteste2.png')).convert_alpha()
    assets[BAT_IMG2] = pygame.transform.scale_by(assets[BAT_IMG2], BAT_SCALE)
    
    assets[BAT_IMG3] = pygame.image.load(os.path.join(IMG_DIR, 'morcegoteste3.png')).convert_alpha()
    assets[BAT_IMG3] = pygame.transform.scale_by(assets[BAT_IMG3], BAT_SCALE)
    
    # Ataque
    assets[ATTACK_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'attack.png')).convert_alpha()
    assets[ATTACK_IMG] = pygame.transform.scale_by(assets[ATTACK_IMG], ATTACK_SCALE)
    
    # Blocos e cenário
    assets[BLOCK_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'block.png')).convert_alpha()
    assets[BLOCK_IMG] = pygame.transform.scale(assets[BLOCK_IMG], (BLOCK_WIDTH, BLOCK_HEIGHT))
    
    assets[BACKGROUND_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'background.png')).convert_alpha()
    assets[BACKGROUND_IMG] = pygame.image.load(os.path.join(IMG_DIR,'background.png')).convert_alpha()
    assets[BACKGROUND_IMG] = pygame.transform.scale_by(assets[BACKGROUND_IMG], BAT_SCALE)
    assets[GAME_OVER_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'game_over.png')).convert_alpha()
    assets[GAME_OVER_IMG] = pygame.image.load(os.path.join(IMG_DIR,'game_over.png')).convert_alpha()
    assets[GAME_OVER_IMG] = pygame.transform.scale_by(assets[GAME_OVER_IMG], BAT_SCALE)
    assets[START_IMG] = pygame.image.load(os.path.join(IMG_DIR,'tela_inicial.png')).convert_alpha()
    assets[START_IMG] = pygame.transform.scale_by(assets[START_IMG], BAT_SCALE)

    pygame.mixer.music.load('assets/snd/musicamedieval3min.wav')
    pygame.mixer.music.set_volume(0.4)
    musica_medieval = pygame.mixer.Sound('assets/snd/musicamedieval3min.wav')
    assets[SOM_ESPADA] = pygame.mixer.Sound('assets/snd/somespada.wav')
    assets[SOM_ESPADA].set_volume(0.4)
    assets[SOM_PULO] = pygame.mixer.Sound('assets/snd/flapsound.wav')
    assets[SOM_PULO].set_volume(0.7)
    assets[SOM_DANO] = pygame.mixer.Sound('assets/snd/hurt1.wav')
    assets[SOM_DANO].set_volume(0.3)
    return assets