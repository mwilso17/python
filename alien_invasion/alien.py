import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  """A class to represent one alien."""

  def __init__(self, ai_game):
    """Initialize the alien and set its start point."""
    super().__init__()
    self.screen = ai_game
    self.settings = ai_game.settings

    # Load alien image and set its rect attribute.
    self.image = pygame.image.load('alien_invasion\images\\alien.bmp')
    self.rect = self.image.get_rect()

    # Start each new alien in the top left corner.
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    # Store alien's horizontal position.
    self.x = float(self.rect.x)

  def update(self):
    """Move alien to the right."""
    self.x += self.settings.alien_speed
    self.rect.x = self.x