import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED, GRAY
from assets import load_assets, PLAYER_IMG
from sprites import Player, Zombie

def game_screen(window):
    clock = pygame.time.Clock()
    all_sprites = pygame.sprite.Group()
    assets = load_assets()
    player = Player(all_sprites, assets)
    zombie = Zombie(all_sprites, assets)
    all_sprites.add(player, zombie)
    running = True
    keys_down = {}
    pygame.key.set_repeat(1, 10)
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
                if event.key == pygame.K_a:
                    player.image = pygame.transform.flip(assets[PLAYER_IMG], True, False)
                    player.speedx = -5
                if event.key == pygame.K_d:
                    player.image = assets[PLAYER_IMG]
                    player.speedx = 5
                if event.key == pygame.K_w:
                    player.jump()
            if event.type == pygame.KEYUP:
                if event.key in keys_down:
                    del keys_down[event.key]
                if event.key == pygame.K_a and player.speedx < 0:
                    player.speedx = 0
                if event.key == pygame.K_d and player.speedx > 0:
                    player.speedx = 0
                if event.key == pygame.K_w and player.speedy < 0:
                    player.speedy = 0
        player.speedy = 5
        all_sprites.update()
        zombie.move_towards_player(player,assets)
        window.fill(GRAY)
        all_sprites.draw(window)
        pygame.display.flip()