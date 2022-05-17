import pygame

class Settings():
    """A class to store all settings for Alien Invasion."""


    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1800
        self.screen_height = 900
        self.bg_color = (200, 230, 230)     # set a color of screen

        # Background settings
        self.bg_picture = pygame.image.load('/home/richi/Documents/Python/Aliens_crash/images/desert_surface.bmp')

        # Ship settings
        self.ship_speed = 5
        self.ship_color = pygame.image.load('/home/richi/Documents/Python/Aliens_crash/images/space_ship.bmp')

        # Bullet settings
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (200, 0, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed = 1
        self.image = pygame.image.load('/home/richi/Documents/Python/Aliens_crash/images/alien.bmp')
