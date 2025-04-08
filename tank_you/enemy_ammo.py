import pygame
from pygame.sprite import Sprite

class EnemyAmmo(Sprite):
  """A class to manage ammo fired from tanks."""
  
  def __init__(self, ty_game):
    """Create a round at the player's tank current position"""
    super().__init__()
    self.screen = ty_game.screen
    self.settings = ty_game.settings
    self.color = self.settings.ammo_color

    # Create a round rect and set its correct position.
    self.rect = pygame.Rect(0, 0, self.settings.ammo_width, self.settings.ammo_height)
    self.rect.midright = ty_game.enemy.sprites()[0].rect.midright

    # Store round position as a decimal value.
    self.x = float(self.rect.x)

  def update(self):
    """Move round across the screen."""
    self.x -= self.settings.ammo_speed
    self.rect.x = self.x

  def draw_enemy_round(self):
    """Draw round to screen."""
    pygame.draw.rect(self.screen, self.color, self.rect)