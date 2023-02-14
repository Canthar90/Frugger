import pygame
import sys


class Menu:
    """Creates simple death screen menu"""
    def __init__(self, player, WINDOW_WIDTH, WINDOW_HEIGTH, display):
        self.font = pygame.font.Font(None, 50)
        
        text = "You have been struck by a car"
        self.loose = self.font.render(text, True, (255, 255, 255))
        self.loose_rect = self.loose.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGTH/2))
        
        replay_text = "Retry?"
        self.replay = self.font.render(replay_text, True, (255, 255, 255))
        self.replay_rect = self.replay.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGTH/2 + 50))
        
        exit_text = "Exit"
        self.exit = self.font.render(exit_text, True, (255, 255, 255))
        self.exit_rect = self.exit.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGTH/2 + 100))
        
        self.win = self.font.render("You won!", True, (255, 255, 255))
        self.win_rect = self.win.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGTH/2))
        
        self.player = player
        self.display = display
        self.flag = False
        self.type = ""
    
    def click_detection(self):
        mouse = pygame.mouse.get_pos()
        
        if self.replay_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            self.player.hittbox.center = (2062, 3274)
            self.player.rect.center = (2062, 3274)
            self.player.directionx = 2062
            self.player.directiony = 3274
            self.player.pos = pygame.math.Vector2(2062, 3274)
            self.flag = False
        elif self.exit_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            pygame.quit()
            sys.exit
        else:
            return True
        
    
    def draw(self):
        if self.type == "loose":
            self.display.fill("teal")
            self.display.blit(self.loose, self.loose_rect)
            self.display.blit(self.exit, self.exit_rect)
            self.display.blit(self.replay, self.replay_rect)
            
        elif self.type == "win":
            self.display.fill("teal")
            self.display.blit(self.win, self.win_rect)
            self.display.blit(self.replay, self.replay_rect)
            self.display.blit(self.exit, self.exit_rect)
    
    def update(self):
        self.click_detection()
        
        
    
    
    
    