#definindo as classes do jogo
import game_screen
import pygame
assets = {}
assets['idle_jogador'] = pygame.transform.scale(pygame.image.load('assets/img/jogador/idle1.png'),(200,200))
class Jogador(pygame.sprite.Sprite):
    def __init__(self,groups,assets,nome):
        pygame.sprite.Sprite.__init__(self)
        self.image = assets['idle_jogador']
        self.rect = self.image.get_rect()
        self.rect.centerx = 200
        self.rect.bottom = 200
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.assets = assets

        def update(self):
            # Atualização da posição da nave
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            # Mantem dentro da tela
            if self.rect.right > game_screen.WIDTH:
                self.rect.right = game_screen.WIDTH
            if self.rect.left < 0:
                self.rect.left = 0

        self.nome = nome
        self.vida = 100
        self.ataque = 5
        self.estamina = 50
        self.velocidade = 5
        self.pontuacao = 0
    def atacar(self,Inimigo):
        Inimigo.vida -= self.ataque

class Zumbi:
    def __init__(self,nivel):
        self.nivel = nivel
        #os atributos são proporcionais ao nível, os níveis variam de 0 a 6, o zumbi é focado em vida e ataque.
        self.vida = round(15*(1+(nivel*3/10)))
        self.ataque = round(5*(1+(nivel*3/10)))
        self.velocidade = round(2*(1+(nivel*2/10)))
    def atacar(self,Jogador):
        Jogador.vida -= self.ataque

class Esqueleto:
    def __init__(self,nivel):
        self.nivel = nivel
        #o esqueleto é focado em ataque e velocidade
        self.vida = round(10*(1+(nivel*2/10)))
        self.ataque = round(5*(1+(nivel*3/10)))
        self.velocidade = round(3*(1+(nivel*3/10)))
    def atacar(self,Jogador):
        Jogador.vida -= self.ataque

class Morcego:
    def __init__(self,nivel):
        self.nivel = nivel
        #o morcego é focado em velocidade
        self.vida = round(3*(1+(nivel*2/10)))
        self.ataque = round(3*(1+(nivel*2/10)))
        self.velocidade = round(5*(1+(nivel*4/10)))
    def atacar(self,Jogador):
        Jogador.vida -= self.ataque

class Chefao:
    def __init__(self,dificuldade):
        #o Boss possui acressimos fixos baseados na dificuldade escolhida
        self.dificuldade = dificuldade
        self.vida = 100 + dificuldade * 20
        self.ataque = 15 + dificuldade * 5
        self.velocidade = 4 + dificuldade
    def atacar(self,Jogador):
        Jogador.vida -= self.ataque