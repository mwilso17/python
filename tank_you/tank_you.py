import sys

import pygame

from settings import Settings
from tank import Tank

class TankYou:
  """Class to manage game."""

  def __init__(self):
    """Initialize game."""
    pygame.init()
    self.settings = Settings()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Tank You")

    self.tank = Tank(self)

  def run_game(self):
    """Start game main loop."""
    while True:
      self._check_events()
      self.tank.update()
      self._update_screen()

  def _check_events(self):
    """Respond to key and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()

        elif event.type == pygame.KEYDOWN:
          self._check_keydown_events(event)
        elif event.type == pygame.KEYUP:
          self._check_keyup_events(event)
          

  def _check_keydown_events(self, event):
    """Respond to keypresses."""
    if event.key == pygame.K_UP:
      self.tank.moving_up = True
    if event.key == pygame.K_DOWN:
      self.tank.moving_down = True
    if event.key == pygame.K_q:
      sys.exit()

  def _check_keyup_events(self, event):
    """Respond to keyreleases."""
    if event.key == pygame.K_UP:
      self.tank.moving_up = False
    if event.key == pygame.K_DOWN:
      self.tank.moving_down = False

  def _update_screen(self):
    """Update images on screen and flip to new screen."""
    self.screen.fill(self.settings.bg_color)
    self.tank.blitme()

    # Makes current render visible.
    pygame.display.flip()

if __name__ == '__main__':
  ty = TankYou()
  ty.run_game()