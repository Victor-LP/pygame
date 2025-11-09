import pygame
from config import WIDTH, HEIGHT, window
from game import game_screen

pygame.init()
pygame.mixer.init()
pygame.display.set_caption('Casatle Insper')

game_screen(window)

pygame.quit() 