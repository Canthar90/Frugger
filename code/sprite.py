import pygame


class SimpleSprite(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.hittbox = self.rect.inflate(0,-self.rect.height/2)
        
                
class LongSprite(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.hittbox = self.rect.inflate(-self.rect.width * 0.8, -self.rect.height/2)
        self.hittbox.bottom = self.rect.bottom - 10