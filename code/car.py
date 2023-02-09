import pygame
from os import walk
from random import choice



class Car(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.name = "car"
        
        images = list(walk("graphics\cars"))
        car = choice(images[0][2])
        path = images[0][0].replace('\\', '/') + "/" + car
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        
        self.pos = pygame.math.Vector2(self.rect.center)
        
        if pos[0] < 200:
            self.direction = pygame.math.Vector2(1,0)
        else :
            self.direction = pygame.math.Vector2(-1,0)
            self.image = pygame.transform.flip(self.image, True, False)
            
        
        # float based movement
        self.speed = 300
        self.hittbox = self.rect.inflate(0, -self.rect.height/2)
        
    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        self.hittbox.center = (round(self.pos.x), round(self.pos.y))
        self.rect.center = self.hittbox.center
        
        if not -200 < self.rect.x < 3400:
            self.kill()