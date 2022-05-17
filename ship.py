import pygame

class Ship:
    """A class to manage a ship."""

    def __init__(self, ai_game):                                # ai_game is reference to current instance of the AlienInvasion class- acces to all the game resources form AlienInvasion class
        """Initialize the ship and its starting position."""
        self.screen = ai_game.screen                            # add screen from AlienInvasion class to variable self.screen
        self.screen_rect = ai_game.screen.get_rect()            # add screen from AlienInvasion class to variable self.screen_rect and make it reactangle by get_rect function
        self.settings = ai_game.settings

        # Load the ship image and set its rect.
        self.image = ai_game.settings.ship_color
        self.rect = self.image.get_rect()                       # make reactangle from image of the ship

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom        # place the ship to middle bottom of the game screen

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False           # variable is used in main code alien_invasion.py to set default value False (when no side key is not pressed)
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:   # move by ship when right key is pressed and ship is not on the right side of the screen
            self.x += self.settings.ship_speed                               # change ship position by ship speed settings value
        if self.moving_left and self.rect.left > 0:             # move by ship when left key is pressed and ship is not on the left side of the screen
            self.x -= self.settings.ship_speed

        # Update rect object from self.x
        self.rect.x = self.x                    # control the position of the ship                                  

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)                 # draw the image to the screen at the position specified by self.rect

