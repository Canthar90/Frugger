import pygame
from settings import *
import sys
import random


# base setup
pygame.init()
clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frugger")



# main game loop
while True:
    
    dt = clock.tick(120)/1000
    
    for event in pygame.event.get():
        if event.type ==    pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
    # game window
    
    
    # update the display surface
    pygame.display.update()