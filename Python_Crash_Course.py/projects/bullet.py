import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship"""

    def __init__(self, ai_game):  
        """create a bullet object at the ship's current position"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height) ## create a bullet
        self.rect.midtop = ai_game.ship.rect.midtop       ## align bullet's midtop position with the ship's midtop.


        ## store the bullet's position in a decimal value
        self.y = float(self.rect.y)  ## Bullet's coordinates are converted to float for finer adjustments later


    def update(self):
        """move bullet up the screen"""
        self.y -= self.settings.bullet_speed


        """update the rect position"""
        self.rect.y = self.y
 

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
