import sys
import pygame
from settings import Settings
from ship import Ship
from background import Background
from bullets import Bullet
from alien import Alien

class AlienInvasion:
    """Overal class ti manage game assets behavior."""

    def __init__(self):
        """Initialize the game and create resources."""
        pygame.init()
        self.settings = Settings()          # make an instance from Setting class in settings.py and place it to variable self.settings

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)       # call screen_width and height from self.settins instance
        self.settings.screen_width = self.screen.get_rect().width           # FUNGUJE I BEZ TOHO. ZJISTIT, K CEMU JE TO VLASTNE DOBRE!!!!
        self.settings.screen_height = self.screen.get_rect().height         # FUNGUJE I BEZ TOHO. ZJISTIT, K CEMU JE TO VLASTNE DOBRE!!!!
        pygame.display.set_caption("Alien Invasion")                        # name a window with game screen

        self.ship = Ship(self)                                              # make an instance from Ship class and place it to self.ship variable
        self.background = Background(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        while True:                                                         # repeatedly display a screen
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._create_fleet()
            self._update_screen()
            
    def _check_events(self):
        """Respond to keypress and mouse events."""
        # Watch for keyboard and mouse events
        for event in pygame.event.get():                                # make changes in a screen acording list of event collected by event.get() function (list of events)
            if event.type == pygame.QUIT:                               # if event is QUIT, system exit the game
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type == pygame.K_q:
                sys.exit()

    def _check_keydown_event(self, event):
        """Respond to keypress."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_event(self, event):
        """Respond to key release."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to a bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)           # make an instance of Bullet class and assign it to new_bullet variable
            self.bullets.add(new_bullet)        # add is similar to append but it is special for pygame groups

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet position
        self.bullets.update()

        # Get rid bullets out of screen
        for bullet in self.bullets.copy():      # you can't remove item from original list, so I used copy function
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """Create a fleet of aliens."""
        # Create an alien andfindthe number of aliens in a row.
        # Spacing between two aliens is one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine how many rows of alien fit on screen.
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height -(4 * alien_height) - ship_height
        number_rows = available_space_y // (3 * alien_height)
        
        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        # Create an alien and find the number of aliens in a row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self):
        """Updating images on the screen anf flip to the new screen."""
    # Redraw the screen during each pass trough the loop.
        self.screen.fill(self.settings.bg_color)                    # fill game screen by set collor in Settings class
        self.background.blit_back()
        self.ship.blitme()                                          # display the space ship on screen from Ship class
        for bullet in self.bullets.sprites():                       # bullets.sprites return list of bullets
            bullet.draw_bullet()
        self.aliens.draw(self.screen)


        # Make the most recently drawn screen visible.
        pygame.display.flip()     # continualy updates the display to show the new positions of game elements and hides the old ones (illusion of smooth movement)



if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()