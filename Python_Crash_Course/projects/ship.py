import pygame

class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and see its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()       ## creates an invisible as a boundary around screen's edge

        self.image = pygame.image.load('images/ship.bmp')  ## Load the ship's image
        self.rect = self.image.get_rect()                  ## creates an invisible rectangle around ship

        self.rect.midbottom = self.screen_rect.midbottom   ## centered horizontally & aligned with bottom center

        self.x = float(self.rect.x)                   ## self.rect.x represents x-coord of the upper left corner of rectangle.  To move ship by a dist less than a pixel, self.rect.x is converted to float.

        self.moving_right = False                           ## Sets the ship's movement to right as not moving at start
        self.moving_left = False                            ## Sets the ship's movement to left as not moving at start
        
    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


    def update(self):
        """update the ship's position based on the movement flag"""
        #! Update the ship's X value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:  ## if self.moving_right flag is true
            self.x += self.settings.ship_speed                      ## control the ship's speed on x axis to the right side
        if self.moving_left and self.rect.left > 0:                 ## if self.moving_left flag is true
            self.x -= self.settings.ship_speed

        self.rect.x = self.x


    def blitme(self):
        """ Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
