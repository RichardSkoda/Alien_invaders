import pygame

class Background:
    """Set a background of the game."""

    def __init__(self, ai_game):
        """Initialize background settings"""
        self.screen = ai_game.screen                            
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.bg_picture = self.settings.bg_picture
        self.rect = self.bg_picture.get_rect()

        self.rect.center = self.screen_rect.center

    def blit_back(self):
        """Draw the background"""
        self.screen.blit(self.bg_picture ,self.rect)