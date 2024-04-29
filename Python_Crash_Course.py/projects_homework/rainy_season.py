import sys
import pygame                                  ## pygame contains functionality to create a game.
from settings1 import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien



class AlienInvasion:
    """Overall class to manager game assets and behavior"""

    def __init__(self):
        pygame.init()                          ## stores all the variables, methods into the memory.

        self.clock = pygame.time.Clock()       ## creating instance from Clock class of pygame.time module
        self.settings = Settings()             ## Instance of settings class.

        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet() 

    def run_game(self):

        while True:
            self._check_events()               ## A helper method created after breaking the run_game() method (refactoring)
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)                ## while loop will run at 60 times per second.

    def _check_events(self):
        """respond to keyboard & mouse events"""
        for event in pygame.event.get():        ## Watch for the keyboard and mouse events.
            if event.type == pygame.QUIT:
                sys.exit()               
            if event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """respond to key presses"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        
    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)                      ## in Instance of Bullet() class is created which creates new bullet
            self.bullets.add(new_bullet)                   ## add new bullets to group bullets using add() method

    def _check_keyup_events(self, event):
        """respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False            
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _update_bullets(self):
        """update position of bullets and get rid of old bullets"""
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                
    def _update_aliens(self):
        """update positions of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()                        ## calls alien's update method to add aliens in the aliens group.

    def _create_fleet(self):
        """create the fleet of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size  ## We get alien's width and height using alien rect's size attribute.
        alien_width = alien.rect.width   ## It is the width of the rectangle around the alien ship

        current_x, current_y = alien_width, alien_height  ## The current_x is representing horizontal position of alien ship width.
        while current_y < (self.settings.screen_height -3* alien_height):        
            while current_x < (self.settings.screen_width -2*alien_width): ## ttl scrn width - (1 a. ship + 1 a.ship rect width)
                self._create_alien(current_x, current_y)
                current_x += 2*alien_width      ## new current_x position now will be ahead of newly created alien object
                
            current_x = alien_width             ## Finished a row, reset x value and increment y value
            current_y += 2*alien_height
            
    def _check_fleet_edges(self):
        """Respond if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """draw entire fleet and change fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed      ## drop the fleet at drop_speed
        self.settings.fleet_direction *= -1                     ## change the direction of fleet

    def _create_alien(self, x_position, y_position):
        """create an alien and place it in the fleet"""
        new_alien = Alien(self)         ## create a new alien object
        new_alien.x = x_position         ## current_x represents new alien on x axis
        new_alien.rect.x = x_position  ## current_x rectangle also is of the same width as the alien ship
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)      ## new_alien ship gets appended to the self.aliens group

    def _update_screen(self):
        """update images on the screen and flip to the new screen"""        
        self.screen.fill(self.settings.bg_color)    ## Redraw the screen during each pass through the loop.
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()                       ## Make the most recently drawn screen visible.

if __name__ == "__main__":                          #! checks if the interpreter is running source files as main program.    
    ai = AlienInvasion()                            ## make a game instance and run the game.
    ai.run_game()
