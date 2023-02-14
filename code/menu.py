import pygame


class DeathMenu:
    """Creates simple death screen menu"""
    def __init__(self, player, WINDOW_WIDTH, WINDOW_HEIGTH):
        self.font = pygame.font.Font(None, 50)
        
        text = "You have been struck by a car"
        self.loose = self.font.render(text, True, (255, 255, 255))
        self.loose_rect = self.loose.get_rect(WINDOW_WIDTH/2, WINDOW_HEIGTH/2)
        
        replay_text = "Retry?"
        self.replay = self.font.render(replay_text, True, (255, 255, 255))
        self.replay_rect = self.replay.get_rect(WINDOW_WIDTH/2, WINDOW_HEIGTH/2 + 300)
        
        exit_text = "Exit"
        self.exit = self.font.render(exit_text, True, (255, 255, 255))
        self.exit_rect = self.exit.get_rect(WINDOW_WIDTH/2, WINDOW_HEIGTH + 600)
    
    def click_detection(self):
        pass
    
    def draw(self):
        pass
    
    def update(self):
        pass
    
    
    
    