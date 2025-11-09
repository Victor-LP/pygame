import pygame
import random
from config import WIDTH, HEIGHT, GRAVITY, BLOCK_HEIGHT, BLOCK_WIDTH, JUMP_SIZE, STILL, JUMPING, FALLING

# ========== CLASSE MÃE PARA ENTIDADES COM FÍSICA ==========
class PhysicsEntity(pygame.sprite.Sprite):
    def __init__(self, groups, assets, image_key, all_blocks=None):
        super().__init__()
        self.image_key = image_key  # Armazena a chave da imagem
        self.image = assets[image_key]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect()
        self.groups = groups
        self.assets = assets
        self.blocks = all_blocks
        self.speedx = 0
        self.speedy = 0
        self.direction = 0
        self.state = STILL
        self.on_ground = False

    def apply_physics(self):
        # Aplica física de gravidade e colisões
        # Movimento horizontal
        if self.blocks:  # Verifica se há blocos para colidir
            self.rect.x += self.speedx * self.direction
            collisions = pygame.sprite.spritecollide(self, self.blocks, False)
            
            for collision in collisions:
                move_x = self.speedx * self.direction
                if move_x > 0:
                    self.rect.right = collision.rect.left
                elif move_x < 0:
                    self.rect.left = collision.rect.right
        else:
            self.rect.x += self.speedx * self.direction

        # Movimento vertical
        self.speedy += GRAVITY
        self.rect.y += self.speedy
        
        if self.blocks:  # Verifica se há blocos para colidir
            collisions = pygame.sprite.spritecollide(self, self.blocks, False)
            
            self.on_ground = False
            for collision in collisions:
                if self.speedy > 0:  # Caindo
                    self.rect.bottom = collision.rect.top
                    self.speedy = 0
                    self.state = STILL
                    self.on_ground = True
                elif self.speedy < 0:  # Subindo
                    self.rect.top = collision.rect.bottom
                    self.speedy = 0
                    self.state = FALLING

    def jump(self):
        # Faz a entidade pular se estiver no chão
        if self.on_ground:
            self.speedy = JUMP_SIZE
            self.state = JUMPING
            self.on_ground = False

# ========== CLASSE DO JOGADOR ==========
class Player(PhysicsEntity):
    def __init__(self, groups, assets, all_blocks):
        super().__init__(groups, assets, 'player', all_blocks)
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT * 10
        self.speedx = 5
        self.looking = 1  # 1 = direita, -1 = esquerda
        self.last_attack = 0
        self.attack_ticks = 300

    def update(self):
        # Atualiza o estado do jogador
        self.apply_physics()
        
        # Atualiza direção da imagem
        if self.looking == -1:
            self.image = pygame.transform.flip(self.assets[self.image_key], True, False)
        else:
            self.image = self.assets[self.image_key]

    def attack(self):
        # Executa um ataque
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_attack

        if elapsed_ticks > self.attack_ticks:
            self.last_attack = now
            if self.looking == 1:
                new_attack = Attack(self.assets, self.rect.centerx, self.rect.y, 1)
            else:
                new_attack = Attack(self.assets, self.rect.x, self.rect.y, -1)
            
            self.groups['all_sprites'].add(new_attack)
            self.groups['all_attacks'].add(new_attack)

# ========== CLASSE DOS INIMIGOS TERRESTRES ==========
class GroundEnemy(PhysicsEntity):
    def __init__(self, groups, assets, image_key, all_blocks, speed=2):
        super().__init__(groups, assets, image_key, all_blocks)
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT * 10
        self.speedx = speed

    def update(self):
        # Atualiza a física do inimigo
        self.apply_physics()

    def move_to_player(self, player, assets):
        # Move o inimigo em direção ao jogador
        if self.rect.x + 100 <= player.rect.x and player.rect.y <= self.rect.y:
            self.direction = 1
            self.image = assets[self.image_key]
        elif self.rect.x - 100 > player.rect.x and player.rect.y <= self.rect.y:
            self.direction = -1
            self.image = pygame.transform.flip(assets[self.image_key], True, False)

class Zombie(GroundEnemy):
    def __init__(self, groups, assets, all_blocks):
        super().__init__(groups, assets, 'zombie', all_blocks, speed=2)

class Skeleton(GroundEnemy):
    def __init__(self, groups, assets, all_blocks):
        super().__init__(groups, assets, 'skeleton', all_blocks, speed=2)
        
    def move_to_player(self, player, assets):
        #Move o esqueleto em direção ao jogador com pulo
        super().move_to_player(player, assets)
        if abs(self.rect.x - player.rect.x) < 100 and self.on_ground:
            self.jump()

# ========== CLASSE DO MORCEGO ==========
class Bat(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        super().__init__()
        self.image = assets['bat1']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect()
        self.rect.centerx = random.randint(0, WIDTH)
        self.rect.y = random.randint(40, HEIGHT // 3)
        self.groups = groups
        self.assets = assets
        self.direction = 1
        self.speed = 2
        self.switch_interval = 1500
        self.last_switch = pygame.time.get_ticks()

    def update(self):
        # Atualiza o movimento do morcego
        now = pygame.time.get_ticks()
        if now - self.last_switch >= self.switch_interval:
            self.direction *= -1
            self.last_switch = now

        self.rect.x += self.speed * self.direction

        # Atualiza animação baseada na direção
        if self.direction == -1:
            self.image = pygame.transform.flip(self.assets['bat2'], True, False)
        else:
            self.image = self.assets['bat3']

        # Mantém dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.direction = -1
            self.last_switch = now
        if self.rect.left < 0:
            self.rect.left = 0
            self.direction = 1
            self.last_switch = now

# ========== CLASSE DO ATAQUE ==========
class Attack(pygame.sprite.Sprite):
    def __init__(self, assets, x, y, looking):
        super().__init__()
        if looking == -1:
            self.image = pygame.transform.flip(assets['attack'], True, False)
        else:
            self.image = assets['attack']
        
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 15 * looking
        self.spawn_time = pygame.time.get_ticks()
        self.duration = 100  # Duração em milissegundos

    def update(self):
        # Atualiza o movimento e verifica duração do ataque
        self.rect.x += self.speedx
        elapsed = pygame.time.get_ticks() - self.spawn_time
        if elapsed > self.duration:
            self.kill()

# ========== CLASSE DO BLOCO ==========
class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, assets, row, column):
        super().__init__()
        self.image = assets['block']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.groups = groups
        self.rect.x = column * BLOCK_WIDTH
        self.rect.y = row * BLOCK_HEIGHT