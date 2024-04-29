import pygame

class Fred:
    def __init__(self, ai_game):
        """initialize fred and set starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        
        ## load the rectangular fred image
        
        self.image = pygame.image.load('images/Fred.bmp')
        self.rect = self.image.get_rect()
        
        ## start new fred at the bottom center of the screen
        
        self.rect.midbottom = self.screen_rect.midbottom
        
    def blitme(self):
        """draw fred at his current location"""
        self.screen.blit(self.image, self.rect)
        