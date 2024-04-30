class Settings:
    """A class to store all the settings for Alien Invasion"""

    def __init__(self):
        """initialize game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5                       ## Ship moves by 1.5 pixels on each pass through the loop.

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        ## fleet_direction of:   1 represents right; -1 represents left.
        self.fleet_direction = 1
