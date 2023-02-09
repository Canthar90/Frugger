import pygame
from settings import *
import sys
import random
from player import Player
from car import Car
from sprite import SimpleSprite, LongSprite


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2()
        self.bg = pygame.image.load("graphics\main\map.png").convert()
        self.fg = pygame.image.load("graphics\main\overlay.png").convert_alpha()
        
    def customize_draw(self):
        # change the offset vector
        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2
        # blit the bg
        display_surface.blit(self.bg, -self.offset)
        
        
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            display_surface.blit(sprite.image, offset_pos)
            
        display_surface.blit(self.fg, -self.offset)

# base setup
pygame.init()
clock = pygame.time.Clock()
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frugger")

# groups
all_sprites = AllSprites()
obsticle_sprites = pygame.sprite.Group()

# 
player = Player((2062, 3274), all_sprites, obsticle_sprites)

# timer
car_timer = pygame.event.custom_type()
pygame.time.set_timer(car_timer, 50)
pos_list = []

# Sprite setup
for file_name, pos_list in SIMPLE_OBJECTS.items():
    path = f"graphics\objects\simple\{file_name}.png"
    surf = pygame.image.load(path).convert_alpha()
    for pos in pos_list:
        sprite = SimpleSprite(surf=surf, pos=pos, groups=[all_sprites, obsticle_sprites])
        
for file_name, pos_list in LONG_OBJECTS.items():
    path = f"graphics\objects\long\{file_name}.png"
    surf = pygame.image.load(path).convert_alpha()
    for pos in pos_list:
        sprite = LongSprite(surf=surf, pos=pos, groups=[all_sprites, obsticle_sprites])

# main game loop
while True:
    
    dt = clock.tick(120)/1000
    
    for event in pygame.event.get():
        if event.type ==    pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == car_timer:
            random_pos = random.choice(CAR_START_POSITIONS)
            if random_pos not in pos_list:
                pos_list.append(random_pos)
                pos = (random_pos[0], random_pos[1]+ random.randint(-8, 8))
                car = Car((pos), [all_sprites, obsticle_sprites])
            if len(pos_list) > 5:
                del pos_list[0]
    
    # draw bg
    display_surface.fill('black')
    
    # draw
    # all_sprites.draw(display_surface)
    all_sprites.customize_draw()
    
    # update
    all_sprites.update(dt)
    
    # update the display surface
    pygame.display.update()