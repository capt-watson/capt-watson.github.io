class Settings:
    """A class to store all the settings for Alien Invasion"""
    
    def __init__(self):
        """initialize game settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5                       ## Ship moves by 1.5 pixels on each pass through the loop.

        # self.bullet_speed = 2.0
        # self.bullet_width = 3
        # self.bullet_height = 15
        # self.bullet_color = (60, 60, 60)
        # self.bullets_allowed = 5

        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5