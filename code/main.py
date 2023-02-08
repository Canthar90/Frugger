import pygame
from settings import *
import sys
import random
from player import Player
from car import Car


# base setup
pygame.init()
clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frugger")

# groups
all_sprites = pygame.sprite.Group()

# 
player = Player((600, 400), all_sprites)
car = Car((800, 200), all_sprites)

# main game loop
while True:
    
    dt = clock.tick(120)/1000
    
    for event in pygame.event.get():
        if event.type ==    pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # draw bg
    display_surface.fill('black')
    
    # draw
    all_sprites.draw(display_surface)
    
    # update
    all_sprites.update(dt)
    
    # update the display surface
    pygame.display.update()