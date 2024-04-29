import pygame

class Ship:
    def __init__(self, ai_game):
        """Initialize the ship and see its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()       ## creates an invisible as a boundary around screen's edge
        
        self.image = pygame.image.load('images/ship_r.bmp')  ## Load the ship's image
        self.rect = self.image.get_rect()                  ## creates an invisible rectangle around ship
        
        self.rect.midleft = self.screen_rect.midleft   ## centered horizontally & aligned with bottom center
    
        self.y = float(self.rect.y)                   ## self.rect.y represents y-coord of the upper left corner of rectangle.  To move ship by a dist less than a pixel, self.rect.x is converted to float.
        
        self.moving_up = False                           ## Sets the ship's movement to right as not moving at start
        self.moving_down = False                            ## Sets the ship's movement to left as not moving at start

        
    def update(self):
        """update the ship's position based on the movement flag"""
        #! Update the ship's X value, not the rect.
        if self.moving_up and self.rect.top > 0:                    ## if self.moving_right flag is true
            self.y -= self.settings.ship_speed                      ## control the ship's speed on x axis to the right side
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:                 ## if self.moving_left flag is true
            self.y += self.settings.ship_speed

        self.rect.y = self.y
            
    def blitme(self):
        """ Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
