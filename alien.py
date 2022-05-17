import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Dfine an alien ship."""

    def __init__(self, ai_game):
        """Initialize aliens ships."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien and set its rect atribute
        self.image = self.settings.image
        self.rect = self.image.get_rect()

        # Start each alien near top left if the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def update_aliens():
        """Move aliens down the screen."""
        

   