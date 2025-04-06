import sys

import pygame

from settings import Settings
from tank import Tank
from ammo import Ammo

class TankYou:
  """Class to manage game."""

  def __init__(self):
    """Initialize game."""
    pygame.init()
    self.settings = Settings()

    self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Tank You")

    self.tank = Tank(self)
    self.rounds = pygame.sprite.Group()

  def run_game(self):
    """Start game main loop."""
    while True:
      self._check_events()
      self.tank.update()
      self.rounds.update()
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
    if event.key == pygame.K_SPACE:
      self._fire_bullet()

  def _check_keyup_events(self, event):
    """Respond to keyreleases."""
    if event.key == pygame.K_UP:
      self.tank.moving_up = False
    if event.key == pygame.K_DOWN:
      self.tank.moving_down = False

  def _fire_bullet(self):
    """Create a new round and add it to the group."""
    new_round = Ammo(self)
    self.rounds.add(new_round)

  def _update_screen(self):
    """Update images on screen and flip to new screen."""
    self.screen.fill(self.settings.bg_color)
    self.tank.blitme()
    for round in self.rounds.sprites():
      round.draw_round()

    # Makes current render visible.
    pygame.display.flip()

if __name__ == '__main__':
  ty = TankYou()
  ty.run_game()