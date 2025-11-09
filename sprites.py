import pygame
import random
from config import WIDTH, HEIGHT, GRAVITY, BLOCK_HEIGHT, BLOCK_WIDTH, JUMP_SIZE, STILL, JUMPING, FALLING, ATTACKING
from assets import PLAYER_JUMP_IMG,PLAYER_ATTACK_IMG,PLAYER_IMG

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
                    # só marca STILL se NÃO estivermos atacando, para não atrapalhar a animação
                    if self.state != ATTACKING:
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

        # Controle de ataque
        self.last_attack = 0            # tempo do último ataque (cooldown)
        self.attack_cooldown = 500     # ms entre ataques (cooldown)
        self.attack_timer = 0          # tempo em que começou o ataque atual
        self.attack_duration = 200     # ms que a animação de ataque permanece (duracao visual)

    def update(self):
        # Atualiza física
        self.apply_physics()

        now = pygame.time.get_ticks()

        # Se estiver em ATTACKING, verifique se a duração do ataque acabou
        if self.state == ATTACKING:
            if now - self.attack_timer >= self.attack_duration:
                self.state = STILL  # volta ao normal quando o timer expirar

        # --- Escolha de imagem com prioridade: ATTACKING > JUMPING/FALLING > STILL ---
        if self.state == ATTACKING:
            img = self.assets[PLAYER_ATTACK_IMG]
        elif not self.on_ground:
            img = self.assets[PLAYER_JUMP_IMG]
        else:
            img = self.assets[PLAYER_IMG]

        # aplica flip conforme direção olhando
        if self.looking == -1:
            img = pygame.transform.flip(img, True, False)

        # atribui imagem e máscara atualizadas
        self.image = img
        self.mask = pygame.mask.from_surface(self.image)


    def attack(self):
        now = pygame.time.get_ticks()
        # só inicia um novo ataque se não estiver em cooldown
        if now - self.last_attack >= self.attack_cooldown:
            self.state = ATTACKING
            self.attack_timer = now
            self.last_attack = now

            # cria o sprite de ataque (ajuste spawn x/y para posicionar corretamente)
            if self.looking == 1:
                spawn_x = self.rect.centerx + 10
            else:
                spawn_x = self.rect.left - 10
            spawn_y = self.rect.centery

            new_attack = Attack(self.assets, spawn_x, spawn_y, self.looking)
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
        self.duration = 300  # Duração em milissegundos (quanto tempo o sprite de ataque fica ativo)

    def update(self):
        # movimento
        self.rect.x += self.speedx
        # duração
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