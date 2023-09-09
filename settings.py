class Setting:
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's static settings."""        #screen
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(120,120,120)
        #Ship speed
        self.ship_speed=1.5
        self.ship_limit=3
        #Bullet Setting
        self.bullet_speed=0.1
        self.bullet_width=6
        self.bullet_height=25
        self.bullet_color=(255,165,0)
        self.bullets_allowed=5
        self.alien_speed=8.0
        self.fleet_drop_speed=10
        #fleet_direction of 1 represents right;-1 represents left.
        self.fleet_direction = 1
        # How quickly the game speeds up
        self.speedup_scale  = 1.1
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0 
        self.alien_speed = 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        #scoring
        self.alien_points = 50
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale