import pygame
import random
from config import WIDTH, HEIGHT
from assets import PLAYER_IMG, ZOMBIE_IMG
gavity = 0.6
class Player(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[PLAYER_IMG]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.jump_strength = -20
        self.vel_y = 0
        self.gravity = gavity

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.vel_y += self.gravity
        self.rect.y += self.vel_y
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.bottom >= HEIGHT:
            self.on_ground = True
        else:
            self.on_ground = False

    def jump(self):
        if self.on_ground:
            self.vel_y = self.jump_strength
            self.on_ground = False
class Zombie(pygame.sprite.Sprite):
    def __init__(self,groups,assets):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets[ZOMBIE_IMG]
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = random.randint(0, WIDTH)
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.vel_y = 0
        self.gravity = gavity
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        self.vel_y += self.gravity
        self.rect.y += self.vel_y
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.bottom >= HEIGHT:
            self.on_ground = True
        else:
            self.on_ground = False
    def move_towards_player(self, player,assets):
        if self.rect.x < player.rect.x:
            self.speedx = 2
            self.image = assets[ZOMBIE_IMG]
        elif self.rect.x > player.rect.x:
            self.speedx = -2
            self.image = pygame.transform.flip(assets[ZOMBIE_IMG], True, False)
        else:
            self.speedx = 0
# class Jogador(pygame.sprite.Sprite):
#     def __init__(self,groups,assets,nome):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = assets['idle_jogador']
#         self.rect = self.image.get_rect()
#         self.rect.centerx = 200
#         self.rect.bottom = 200
#         self.speedx = 0
#         self.speedy = 0
#         self.groups = groups
#         self.assets = assets

#         def update(self):
#             # Atualização da posição da nave
#             self.rect.x += self.speedx
#             self.rect.y += self.speedy
#             # Mantem dentro da tela
#             if self.rect.right > game_screen.WIDTH:
#                 self.rect.right = game_screen.WIDTH
#             if self.rect.left < 0:
#                 self.rect.left = 0
#         self.nome = nome
#         self.vida = 100
#         self.ataque = 5
#         self.estamina = 50
#         self.velocidade = 5
#         self.pontuacao = 0
#     def atacar(self,Inimigo):
#         Inimigo.vida -= self.ataque

# class Zumbi:
#     def __init__(self,nivel):
#         self.nivel = nivel
#         #os atributos são proporcionais ao nível, os níveis variam de 0 a 6, o zumbi é focado em vida e ataque.
#         self.vida = round(15*(1+(nivel*3/10)))
#         self.ataque = round(5*(1+(nivel*3/10)))
#         self.velocidade = round(2*(1+(nivel*2/10)))
#     def atacar(self,Jogador):
#         Jogador.vida -= self.ataque

# class Esqueleto:
#     def __init__(self,nivel):
#         self.nivel = nivel
#         #o esqueleto é focado em ataque e velocidade
#         self.vida = round(10*(1+(nivel*2/10)))
#         self.ataque = round(5*(1+(nivel*3/10)))
#         self.velocidade = round(3*(1+(nivel*3/10)))
#     def atacar(self,Jogador):
#         Jogador.vida -= self.ataque

# class Morcego:
#     def __init__(self,nivel):
#         self.nivel = nivel
#         #o morcego é focado em velocidade
#         self.vida = round(3*(1+(nivel*2/10)))
#         self.ataque = round(3*(1+(nivel*2/10)))
#         self.velocidade = round(5*(1+(nivel*4/10)))
#     def atacar(self,Jogador):
#         Jogador.vida -= self.ataque

# class Chefao:
#     def __init__(self,dificuldade):
#         #o Boss possui acressimos fixos baseados na dificuldade escolhida
#         self.dificuldade = dificuldade
#         self.vida = 100 + dificuldade * 20
#         self.ataque = 15 + dificuldade * 5
#         self.velocidade = 4 + dificuldade
#     def atacar(self,Jogador):
#         Jogador.vida -= self.ataque