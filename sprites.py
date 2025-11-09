import pygame
import random
from config import WIDTH, HEIGHT, GRAVITY, BLOCK_HEIGHT, BLOCK_WIDTH, JUMP_SIZE,JUMPING,STILL,FALLING
from assets import PLAYER_IMG, ZOMBIE_IMG, ATTACK_IMG, BLOCK_IMG, BAT_IMG1, BAT_IMG2, BAT_IMG3, SKELETON_IMG

class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, assets, row, column):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[BLOCK_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.groups = groups
        self.rect.x = column * BLOCK_WIDTH
        self.rect.y = row * BLOCK_HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self,groups,assets, all_blocks):
        #método construtor
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[PLAYER_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect()
        self.rect.centerx = 0
        self.rect.bottom = HEIGHT*10
        self.speedx = 5
        self.speedy = 0
        self.last_attack = 0
        self.attack_ticks = 300
        self.groups = groups
        self.assets = assets
        self.direction = 0
        self.looking = 0
        self.blocks = all_blocks
        self.state = STILL

    def update(self):
        self.rect.x += self.speedx*self.direction
        if self.looking == -1:
            self.image = pygame.transform.flip(self.assets[PLAYER_IMG], True, False)
        else:
            self.image = self.assets[PLAYER_IMG]
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for collision in collisions:
            move_x = self.speedx * self.direction
            if move_x > 0:
                self.rect.right = collision.rect.left
            elif move_x < 0:
                self.rect.left = collision.rect.right
        self.speedy += GRAVITY
        self.rect.y += self.speedy
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        self.on_ground = False
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        self.on_ground = False
        for collision in collisions:
            if self.speedy > 0: 
                self.rect.bottom = collision.rect.top
                self.speedy = 0
                self.state = STILL
                self.on_ground = True
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom + 1
                self.speedy = 0
                self.state = FALLING

    def jump(self):
        if self.on_ground:
            self.speedy = JUMP_SIZE
            self.state = JUMPING
            self.on_ground = False

    def attack(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_attack

        # Se já pode atirar novamente...
        if elapsed_ticks > self.attack_ticks:
            # Marca o tick da nova imagem.
            self.last_attack = now
            if self.looking==1:
                new_attack = Attack(self.assets, self.rect.centerx, self.rect.y, 1)
            else:
                new_attack = Attack(self.assets, self.rect.x, self.rect.y, -1)
            self.groups['all_sprites'].add(new_attack)
            self.groups['all_attacks'].add(new_attack)

class Zombie(pygame.sprite.Sprite):
    def __init__(self,groups,assets,all_blocks):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[ZOMBIE_IMG]
        self.assets = assets
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect()
        self.rect.centerx = random.randint(0, WIDTH)
        self.rect.bottom = 100
        self.speedx = 0
        self.speedy = 0
        self.blocks = all_blocks
        self.direction = 1
    def update(self):
        self.rect.x += self.speedx*self.direction
        if self.direction == -1:
            self.image = pygame.transform.flip(self.assets[PLAYER_IMG], True, False)
        else:
            self.image = self.assets[ZOMBIE_IMG]
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        for collision in collisions:
            move_x = self.speedx * self.direction
            if move_x > 0:
                self.rect.right = collision.rect.left
            elif move_x < 0:
                self.rect.left = collision.rect.right
        self.speedy += GRAVITY
        self.rect.y += self.speedy
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        self.on_ground = False
        collisions = pygame.sprite.spritecollide(self, self.blocks, False)
        self.on_ground = False
        for collision in collisions:
            if self.speedy > 0: 
                self.rect.bottom = collision.rect.top
                self.speedy = 0
                self.state = STILL
                self.on_ground = True
            elif self.speedy < 0:
                self.rect.top = collision.rect.bottom + 1
                self.speedy = 0
                self.state = FALLING
        
    def move_to_player(self, player,assets):
        if self.rect.x < player.rect.x and player.rect.y <= self.rect.y:
            self.speedx = 2
            self.image = assets[ZOMBIE_IMG]
        elif self.rect.x > player.rect.x and player.rect.y <= self.rect.y:
            self.speedx = -2
            self.image = pygame.transform.flip(assets[ZOMBIE_IMG], True, False)
        else:
            self.speedx = 0

class Bat(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[BAT_IMG1]
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
        now = pygame.time.get_ticks()
        if now - self.last_switch >= self.switch_interval:
            self.direction *= -1
            self.last_switch = now

        self.rect.x += self.speed * self.direction

        if self.direction == -1:
            self.image = pygame.transform.flip(self.assets[BAT_IMG2], True, False)
        else:
            self.image = self.assets[BAT_IMG3]

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
            self.direction = -1
            self.last_switch = now
        if self.rect.left < 0:
            self.rect.left = 0
            self.direction = 1
            self.last_switch = now

    def move_to_player(self, player, assets):
        return

class Skeleton(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        pygame.sprite.Sprite.__init__(self)
        self.assets = assets
        self.image = assets[SKELETON_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.mask.get_rect()
        self.rect.centerx = random.randint(0, WIDTH)
        self.rect.bottom = 100
        self.speedx = 10
        self.speedy = 0
        self.on_ground = False

        self.groups = groups
        self.blocks = groups["all_blocks"]
        self.direction = 0
        self.looking = 1

        self.run_speed = 4
        self.jump_power = -18

        self.skeleton_aggro = 150
        self.min_jump_range = 30
        self.jump_cooldown = 1250
        self.last_jump = 0

    def update(self):
        self.rect.x += self.speedx * self.direction
        
            
        if self.direction == -1:
            self.image = pygame.transform.flip(self.assets[SKELETON_IMG], True, False)
        else:
            self.image = self.assets[SKELETON_IMG]

    def move_to_player(self, player, assets):
        now = pygame.time.get_ticks()

        dx = player.rect.centerx - self.rect.centerx
        adx = abs(dx)

        can_pounce = (
            self.on_ground
            and (self.min_jump_range < adx <= self.skeleton_aggro)
            and (now - self.last_jump >= self.jump_cooldown)
        )

        if can_pounce:
            if dx > 0:
                self.direction = 1
            else:
                self.direction = -1
            self.speedx = self.run_speed * self.direction
            self.speedy = self.jump_power
            self.last_jump = now
        else:
            if self.on_ground and abs(self.speedx) < 0.4:
                self.speedx = 0


class Attack(pygame.sprite.Sprite):
    def __init__(self, assets, x, y, looking):
        pygame.sprite.Sprite.__init__(self)
        if looking == -1:
            self.image = pygame.transform.flip(assets[ATTACK_IMG], True, False)
        else:
            self.image = assets[ATTACK_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speedx = 10*looking
        spawn_time = pygame.time.get_ticks()
        self.spawn_time = spawn_time
        self.duration = 100  # Duração em milissegundos
    def update(self):
        self.rect.x += self.speedx
        now = pygame.time.get_ticks()
        elapsed = now - self.spawn_time
        if elapsed > self.duration:
            self.kill()