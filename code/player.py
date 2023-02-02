import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.Surface((50,50))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=(pos))
    
    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            print("left arrrow pressed")
        if keys[pygame.K_RIGHT]:
            print("right arrow pressed")
        if keys[pygame.K_UP]:
            print("up arrow is pressed")
        if keys[pygame.K_DOWN]:
            print("down arrow is pressed")
        
    def update(self):
        self.input()