import pygame
import os
from os import walk
import sys


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, colision_sprites, menu):
        
        # image
        super().__init__(groups)
        self.import_assets()
        self.frame_index = 0
        self.status = "down"
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=(pos))
        
        # float based movement
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.speed = 200
        
        # collisions
        self.collisions_sprites = colision_sprites
        self.hittbox = self.rect.inflate(0, -self.rect.height/2)
        
        self.menu = menu
        
    def collision(self, direction):
        """Checking if any object from self.collision_sprites colide with Player sprite"""
        if direction == "horizontal":
            for sprite in self.collisions_sprites.sprites():
                if sprite.hittbox.colliderect(self.hittbox):
                    if hasattr(sprite, 'name') and sprite.name =="car":
                        self.menu.flag = True
                        self.menu.type = "loose"
                    if self.direction.x > 0: # moving right
                        self.hittbox.right = sprite.hittbox.left
                        self.pos.x = self.hittbox.centerx
                        self.rect.centerx = self.hittbox.centerx
                    if self.direction.x < 0: # moving left
                        self.hittbox.left = sprite.hittbox.right
                        self.pos.x =  self.hittbox.centerx
                        self.rect.centerx = self.hittbox.centerx
        else:
            for sprite in self.collisions_sprites.sprites():
                if sprite.hittbox.colliderect(self.hittbox):
                    if hasattr(sprite, 'name') and sprite.name =="car":
                        self.menu.flag = True
                        self.menu.type = "loose"
                    if self.direction.y > 0: # move down
                        self.hittbox.bottom = sprite.hittbox.top
                        self.pos.y = self.hittbox.centery
                        self.rect.centery = self.hittbox.centery
                    if self.direction.y < 0: # move up
                        self.hittbox.top = sprite.hittbox.bottom
                        self.pos.y = self.hittbox.centery
                        self.rect.centery = self.hittbox.centery
        
    def import_assets(self):
        self.animations = {}
        for index, folder in enumerate(walk("graphics\player")):
            if index == 0:
                for name in folder[1]:
                    self.animations[name] = []
                    
            elif index > 0:
                for file_name in folder[2]:
                    path = folder[0].replace('\\', '/') + "/" + file_name
                    surf = pygame.image.load(path).convert_alpha()
                    key = folder[0].split('\\')[2]
                    self.animations[key].append(surf)
                    
            
    def move(self, dt):
        # normalize a vector -> vector should have length of 1
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        # hotizotal movement + collision
        self.pos.x += self.direction.x * self.speed * dt
        self.hittbox.centerx = round(self.pos.x)
        self.rect.centerx = self.hittbox.centerx
        self.collision("horizontal")
        
        # vertical movement + collision
        self.pos.y += self.direction.y * self.speed *dt
        self.hittbox.centery = round(self.pos.y)
        self.rect.centery =  self.hittbox.centery
        self.collision("vertical")

    def restrict(self):
        if self.rect.left < 640:
            self.pos.x = 640 + self.rect.width / 2
            self.hittbox.left = 640
            self.rect.left = 640
        if self.rect.right > 2560:
            self.pos.x = 2560 - self.rect.width / 2
            self.hittbox.right = 2560 
            self.rect.right = 2560
        if self.rect.bottom > 3500:
            self.pos.y = 3500 - self.rect.height / 2
            self.rect.bottom = 3500
            self.hittbox.centery = self.rect.centery
        
    def input(self):
        keys = pygame.key.get_pressed()
        
        # horizontal input
        if keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = "left"
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = "right"
        else:
            self.direction.x = 0
        
        # vertical input
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = "up"
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = "down"
        else:
            self.direction.y = 0
            
    def animate(self, dt):
        current_animation =  self.animations[self.status]
        if self.direction.magnitude() != 0:
            self.frame_index += 6 * dt 
            if self.frame_index >= len(current_animation):
                self.frame_index = 0
        else:
            self.frame_index = 0
        self.image = current_animation[int(self.frame_index)]       
            
    def update(self, dt): 
        self.input()
        self.move(dt)
        self.animate(dt)
        self.restrict()
