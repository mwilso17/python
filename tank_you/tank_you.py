import sys

import pygame

from settings import Settings
from tank import Tank
from ammo import Ammo
from enemy import Enemy

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
    self.enemy = pygame.sprite.Group()

    self._create_enemy()

  def run_game(self):
    """Start game main loop."""
    while True:
      self._check_events()
      self.tank.update()
      self._update_rounds()
      self._update_enemy()
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
      self._fire_round()

  def _check_keyup_events(self, event):
    """Respond to keyreleases."""
    if event.key == pygame.K_UP:
      self.tank.moving_up = False
    if event.key == pygame.K_DOWN:
      self.tank.moving_down = False

  def _fire_round(self):
    """Create a new round and add it to the group."""
    if len(self.rounds) < self.settings.ammo_limit:
      new_round = Ammo(self)
      self.rounds.add(new_round)

  def _update_rounds(self):
    """Update position of rounds and delete off screen ones."""
    self.rounds.update()

    # Get rid of off screen rounds.
    for round in self.rounds.copy():
      if round.rect.left >= self.screen.get_rect().right:
        self.rounds.remove(round)

  def _create_enemy(self):
    """Create enemy tank."""
    enemy = Enemy(self)
    self.enemy.add(enemy)

  def _check_enemy_edges(self):
    """See if enemy has hit edge."""
    for enemy in self.enemy.sprites():
      if enemy.check_for_edges():
        self._change_enemy_direction()
        break

  def _change_enemy_direction(self):
    """Change enemy direction if it hits an edge."""
    self.settings.enemy_direction *= -1
  
  def _update_enemy(self):
    """Update position of enemy."""
    self._check_enemy_edges()
    self.enemy.update()

  def _update_screen(self):
    """Update images on screen and flip to new screen."""
    self.screen.fill(self.settings.bg_color)
    self.tank.blitme()
    for round in self.rounds.sprites():
      round.draw_round()
    self.enemy.draw(self.screen)

    # Makes current render visible.
    pygame.display.flip()

if __name__ == '__main__':
  ty = TankYou()
  ty.run_game()