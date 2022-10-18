class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        #Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 255)

        #Ship settings
        self.ship_speed = 1.5

        #Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 9
        self.bullet_height = 15
        self.bullet_color = (3, 252, 23)
